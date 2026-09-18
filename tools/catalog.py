"""Offline provenance inventory. Never imports or executes vendored code."""
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def inventory(root):
    root = Path(root)
    records = []
    for note in sorted(root.glob('[0-9][0-9]-*/*/README.txt')):
        if note.is_symlink():
            continue
        text = note.read_text(encoding='utf-8')
        title = next((line[6:].strip() for line in text.splitlines() if line.startswith('Title:')), note.parent.name)
        urls = sorted(set(re.findall(r'https?://[^\s<>\"\]]+', text)))
        urls = [u.rstrip('.,;)') for u in urls if urlsplit(u).netloc]
        artifacts = []
        for artifact in sorted(note.parent.glob('paper.*')):
            if artifact.is_file() and not artifact.is_symlink():
                with artifact.open('rb') as stream:
                    header_valid = stream.read(5) == b'%PDF-'
                artifacts.append({'path': artifact.relative_to(root).as_posix(), 'bytes': artifact.stat().st_size,
                                  'sha256': digest(artifact),
                                  'pdf_header_valid': header_valid if artifact.suffix == '.pdf' else None})
        code = note.parent / 'code'
        licenses = sorted(p.relative_to(root).as_posix() for p in code.glob('*')
                          if p.is_file() and not p.is_symlink() and re.match(r'^(license|copying)(\.|$)',p.name,re.I))
        records.append({'id': note.parent.relative_to(root).as_posix(), 'category': note.parent.parent.name,
                        'title': title, 'note': note.relative_to(root).as_posix(), 'note_sha256': digest(note),
                        'source_urls': urls, 'paper_artifacts': artifacts,
                        'code_snapshot_present': code.is_dir(), 'top_level_license_files': licenses,
                        'upstream_revision': None})
    return records


def render(records):
    esc = html.escape
    cards = []
    for r in records:
        flags = []
        if not r['paper_artifacts']: flags.append('No local paper')
        if r['code_snapshot_present'] and not r['top_level_license_files']: flags.append('No top-level license detected')
        links = [f'<a href="../{quote(r["note"])}">Source note</a>']
        links += [f'<a href="{esc(u,quote=True)}" rel="noreferrer">{esc(urlsplit(u).netloc)}</a>' for u in r['source_urls']]
        cards.append(f'<article><small>{esc(r["category"])}</small><h2>{esc(r["title"])}</h2><p>{" · ".join(links)}</p><p class="flags">{esc(" · ".join(flags))}</p></article>')
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>LLM security reference catalog</title><style>
:root{color-scheme:light dark}body{font:17px/1.6 system-ui;margin:3rem auto;max-width:950px;padding:0 1rem}h1{line-height:1.1}h2{font-size:1.15rem;margin:.4rem 0}article{border-top:1px solid #9996;padding:1.2rem 0}a{color:light-dark(#235d78,#9fd5ed);margin-right:.6rem}input{font:inherit;padding:.8rem;width:100%;box-sizing:border-box;border:1px solid #999;border-radius:8px}small,.flags{opacity:.75;font-size:.85rem}[hidden]{display:none}</style>
<h1>LLM security reference catalog</h1><p>Frozen literature library, not original implementations. Search titles, categories, and source domains. Snapshot revisions are unknown; source notes are imported metadata, not independently verified scholarship. License-file detection is not legal clearance.</p>
<label for="search">Find a reference</label><input id="search" type="search" placeholder="e.g. prompt injection, defenders, arxiv"><p id="count" aria-live="polite"></p><main>''' + ''.join(cards) + r'''</main><script>
const field=document.querySelector('#search'),cards=[...document.querySelectorAll('article')];
function filter(){const terms=field.value.toLowerCase().split(/\s+/).filter(Boolean);let count=0;for(const card of cards){const match=terms.every(t=>card.textContent.toLowerCase().includes(t));card.hidden=!match;count+=Number(match)}document.querySelector('#count').textContent=count+' of '+cards.length+' references'}field.addEventListener('input',filter);filter();
</script></html>'''


def generate(root):
    records = inventory(root)
    summary = {'references':len(records),'with_local_paper':sum(bool(r['paper_artifacts']) for r in records),
               'with_code_snapshot':sum(r['code_snapshot_present'] for r in records),
               'code_without_top_level_license':sum(r['code_snapshot_present'] and not r['top_level_license_files'] for r in records),
               'missing_source_url':sum(not r['source_urls'] for r in records),
               'invalid_pdf_headers':sum(a['pdf_header_valid'] is False for r in records for a in r['paper_artifacts']),
               'known_upstream_revisions':0}
    return {'manifest.json': json.dumps({'schema_version':1,'summary':summary,'records':records},indent=2,ensure_ascii=False)+'\n',
            'index.html': render(records)}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    out=ROOT/'catalog'
    for name,content in generate(ROOT).items():
        target=out/name
        if args.check:
            if not target.exists() or target.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Stale catalog: {target}. Run python tools/catalog.py')
        else:
            out.mkdir(exist_ok=True)
            target.write_text(content,encoding='utf-8')
    print('Catalog verified' if args.check else 'Catalog generated')
