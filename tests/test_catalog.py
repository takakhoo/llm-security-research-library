import tempfile
import unittest
from pathlib import Path
from tools.catalog import inventory, render, generate


class CatalogTests(unittest.TestCase):
    def test_missing_license_and_bad_pdf_are_visible(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'01-test'/'entry';p.mkdir(parents=True)
            (p/'README.txt').write_text('Title: A <script>alert(1)</script>\nhttps://example.org/paper\n')
            (p/'paper.pdf').write_bytes(b'<html>download failed</html>')
            (p/'code').mkdir()
            records=inventory(tmp)
            self.assertFalse(records[0]['paper_artifacts'][0]['pdf_header_valid'])
            self.assertEqual(records[0]['top_level_license_files'],[])
            page=render(records)
            self.assertIn('&lt;script&gt;',page)
            self.assertNotIn('<script>alert',page)
            self.assertEqual(generate(Path(tmp)),generate(Path(tmp)))

    def test_hash_changes_and_detects_license(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'06-defenders'/'entry';p.mkdir(parents=True)
            (p/'README.txt').write_text('Title: Reference')
            (p/'code').mkdir();(p/'code'/'LICENSE.md').write_text('example')
            a=inventory(tmp)[0]
            (p/'README.txt').write_text('Title: Changed')
            b=inventory(tmp)[0]
            self.assertNotEqual(a['note_sha256'],b['note_sha256'])
            self.assertTrue(b['top_level_license_files'])


if __name__=='__main__': unittest.main()
