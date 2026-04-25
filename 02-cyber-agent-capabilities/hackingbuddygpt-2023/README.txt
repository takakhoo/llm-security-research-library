Title: Getting pwn'd by AI: Penetration Testing with Large Language Models
(also known in followups as "LLMs as Hackers: Autonomous Linux Privilege Escalation")
Authors: Andreas Happe, Aaron Kaplan, Jürgen Cito (TU Wien / IPA-Lab)
Venue: arXiv preprint, 2023 (later published / extended at ESEC/FSE Industry, etc.)
arXiv: https://arxiv.org/abs/2310.11409
GitHub: https://github.com/ipa-lab/hackingBuddyGPT

Summary:
The hackingBuddyGPT project investigates whether commodity LLMs can autonomously
perform Linux privilege-escalation attacks against vulnerable VMs. The authors
build a small, dependency-light Python harness that exposes a single tool (an SSH
shell) to GPT-3.5/GPT-4 and lets the model iterate: observe shell output, propose
the next command, execute it. They benchmark across a curated set of intentionally
misconfigured Linux VMs (suid binaries, weak file permissions, scheduled cron jobs,
exploitable services, etc.) and study the effect of prompt structure, history
truncation, and the "explain-before-acting" strategy. Their core finding is that
even with a minimal scaffold, GPT-4 already achieves non-trivial privilege
escalation success and that giving it explicit hints (e.g. "look for SUID binaries")
sharply increases success while preserving plausible operator-style behavior. The
codebase is built to be a teaching/research toolkit, so it has grown into a small
ecosystem of "use cases" (privesc, web testing, AD, etc.).

Repo structure (code/):
- src/                : Python package (agent runtime, LLM clients, use-case
  agents like minimal_linux_privesc, web_test_use_case, etc.)
- docs/               : documentation
- scripts/            : entrypoint and helper scripts
- tests/              : pytest suite
- pyproject.toml      : packaging
- CITATION.cff, CODEOWNERS, CODE_OF_CONDUCT.md, CONTRIBUTING.md, CODESPACES.md,
  SECURITY.md, MAC.md, publish_notes.md, LICENSE, README.md : project / community
  files and license
