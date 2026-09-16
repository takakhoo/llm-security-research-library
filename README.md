# LLM Security Research — Reference Library

A curated collection of academic papers, codebases, and reference material on bypassing LLM safety guardrails for legitimate cybersecurity research, red-team work, and exploit development. Six categories covering ~50 papers with cloned source code where available.

> **Scope:** this is a frozen literature and source snapshot, not an original implementation and not a claim of authorship over the mirrored projects. Use each folder's source URL for current code, licensing, and security guidance.

## Categories

### 01 — Foundational Jailbreak Attacks
Core academic attacks on LLM safety alignment that work on cybersecurity prompts.
- **GCG** (Zou et al. 2023) — universal adversarial suffixes
- **Jailbroken** (Wei et al. NeurIPS 2023) — competing-objectives + mismatched-generalization taxonomy
- **PAIR** (Chao et al.) — black-box iterative attacker-LLM
- **TAP** (Mehrotra et al. NeurIPS 2024) — tree-of-attacks with pruning
- **AutoDAN** (Liu et al. ICLR 2024) — fluent genetic-algorithm jailbreaks
- **CipherChat** (Yuan et al. ICLR 2024) — encoded queries bypass alignment
- **PAP** (Zeng et al. ACL 2024) — persuasion-technique jailbreaks
- **Do Anything Now** (Shen et al. CCS 2024) — empirical study of in-the-wild jailbreaks
- **Multilingual** (Deng et al. ICLR 2024) + **Low-Resource** (Yong et al.)
- **ReNeLLM** (Ding et al. NAACL 2024) — scenario-nesting jailbreaks
- **Adaptive Attacks** (Andriushchenko et al. ICLR 2025) — ~100% ASR via prefilling
- **Many-Shot Jailbreaking** (Anthropic NeurIPS 2024)
- **Indirect Prompt Injection** (Greshake et al. AISec 2023)

### 02 — Cyber-Agent Capabilities
Why people want loosened guardrails: papers demonstrating LLM capability for autonomous offensive work.
- **PentestGPT** (Deng et al. USENIX Security 2024)
- **Fang trilogy** — autonomous website hacking, one-day exploitation, zero-day teams
- **Cybench** (Stanford CRFM) — 40 professional CTF tasks, used by US/UK AISI
- **NYU CTF Bench** (Shao et al. NeurIPS 2024)
- **EnIGMA** (Abramovich et al.) — interactive tools for LM security agents
- **InterCode** (Yang et al. NeurIPS 2023)
- **HackingBuddyGPT** (Happe et al.) — autonomous Linux privesc
- **TitanFuzz / FuzzGPT** — LLM-aided fuzzing
- **Big Sleep** (Google Project Zero) — first LLM-found memory-safety zero-day
- **Kang Dual-Use** (Kang et al. SaTML 2024)

### 03 — Cyber-Tuned / Uncensored Models
- **WhiteRabbitNeo / DeepHat** — open-weights cybersecurity-tuned Llama derivative
- **DarkBERT** (KAIST ACL 2023) — RoBERTa pretrained on dark-web text
- **WormGPT/FraudGPT analyses** (Falade 2023; Ferrara JCSS 2024)
- **Eric Hartford's Uncensored Models methodology**
- **Abliteration** (Labonne) — operationalized refusal-direction ablation
- **Heretic** — automated abliteration tool

### 04 — Refusal Removal / Fine-Tuning Attacks
- **Refusal Direction** (Arditi et al. NeurIPS 2024) — *the* foundational abliteration paper
- **Removing RLHF Protections** (Zhan et al. NAACL 2024)
- **BadLlama** line (Lermen, Gade et al.) — QLoRA safety stripping
- **Fine-tuning Compromises Safety** (Qi et al. ICLR 2024 Spotlight)
- **Covert Malicious Finetuning** (Halawi et al. ICML 2024)

### 05 — Surveys & Benchmarks
- **HarmBench** (Mazeika et al. ICML 2024)
- **JailbreakBench** (Chao, Debenedetti et al. NeurIPS 2024)
- **Llama Guard** (Inan et al. — Meta AI)
- **HELM** (Liang et al. — Stanford CRFM)
- **Yi survey**, **SoK Guardrails 2025**, **SoK Prompt Security 2025**, **JailbreakRadar**, **Inie "Summon a demon"**

### 06 — Policy / Defenders
- **Constitutional Classifiers** (Sharma et al. — Anthropic 2025)
- **Circuit Breakers** (Zou et al. NeurIPS 2024)
- **Grinbaum Dual-Use** (JRI 2024)
- **NIST AI 800-1** — managing misuse risk for dual-use foundation models
- **AI Vulnerability Database (AVID)**
- **OWASP Top 10 for LLM Applications**

## Folder Layout

Each paper subfolder contains:
- `paper.pdf` (or `paper.html` for blog posts) — the original paper
- `README.txt` — title, authors, venue, links, summary, repo structure
- `code/` — cloned upstream repo (where available)

Failures (e.g. paper has no public code release) are documented per-category in `_failures.txt`.

## What was excluded for size

To keep this repo under GitHub's 1 GB recommended ceiling, the following bulky upstream content was removed during ingest. Re-clone the original upstream repo (URLs in each `README.txt`) to recover any of it:

- `02-cyber-agent-capabilities/cybench-2024/code/benchmark/` — CTF challenge collections (HKCERT, HackTheBox, Project Sekai)
- `02-cyber-agent-capabilities/nyu-ctf-bench-2024/code/{test,removed,development}/` — CTF challenge artifacts
- `02-cyber-agent-capabilities/intercode-ctf-2023/code/data/` — challenge data
- `05-surveys-benchmarks/harmbench-mazeika-2024/code/data/` — benchmark datasets
- `06-policy-defenders/owasp-llm-top-10/code/{assets,Archive}/` — old PDFs and translations
- `01-foundational-jailbreaks/cipherchat-yuan-2023/code/experimental_results/` — raw run outputs
- All nested `.git/` directories (so this is a flat snapshot, not a meta-repo of git histories)
- A handful of very large CTF binaries (`.AppImage`, `.img`, `.tgz` >95 MB)

## Practical takeaways

- **Table-stakes attacks** (defenders have seen these): GCG, PAIR/TAP, AutoDAN, CipherChat, ReNeLLM, multilingual, indirect injection.
- **Bleeding edge** (still beats frontier defenses): Arditi-style refusal-direction abliteration on open weights, covert malicious finetuning, multi-agent autonomous exploitation, prefilling adaptive attacks.
- **For offensive-security tooling**: most serious work runs on locally hosted abliterated bases (Dolphin, abliterated Llama-3, WhiteRabbitNeo) rather than fighting hosted-API guardrails.

## Use

This is a research reference library. Papers are PDFs; codebases are reference snapshots. Where you want the canonical, up-to-date copy of a tool, use the upstream URL in that paper's `README.txt`.

## Safety and provenance

- Use attack implementations only in authorized evaluation environments.
- Treat vendored code as untrusted until you review its upstream repository, commit history, and dependency files.
- Do not install the entire tree as one environment; each snapshot has independent and sometimes conflicting requirements.
- The collection was assembled for comparative research and does not provide support, updates, or vulnerability remediation for upstream projects.

## Licensing

No repository-wide license is asserted. Papers and code snapshots remain subject to their publishers' and upstream authors' terms. The per-folder `README.txt` files record canonical sources so users can obtain authoritative versions and license information.
