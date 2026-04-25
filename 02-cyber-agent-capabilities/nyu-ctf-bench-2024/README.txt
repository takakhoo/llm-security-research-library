Title: NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security
Authors: Minghao Shao, Sofija Jancheska, Meet Udeshi, Brendan Dolan-Gavitt, Haoran
Xi, Kimberly Milner, Boyuan Chen, Max Yin, Siddharth Garg, Prashanth Krishnamurthy,
Farshad Khorrami, Ramesh Karri, Muhammad Shafique
Venue: NeurIPS 2024 Datasets and Benchmarks Track (NYU Tandon / NYU CCS)
arXiv: https://arxiv.org/abs/2406.05590
GitHub: https://github.com/NYU-LLM-CTF/NYU_CTF_Bench

Summary:
NYU CTF Bench is a large-scale Jeopardy-style CTF benchmark for evaluating LLMs and
LLM agents on offensive-security reasoning. The authors collect 200 challenges from
real CSAW CTF competitions (NYU's flagship event) across crypto, web, reverse
engineering, pwn, forensics, and miscellaneous categories, packaged with stable
Docker environments, official write-ups, and an MITRE ATT&CK mapping for each task.
The paper evaluates GPT-4 and other models in both single-shot and ReAct-agent
settings, finding that with tools and iteration the agent solves a meaningful slice
of challenges, but performance is still far below expert humans, especially on multi-
stage exploitation. The repo is intentionally open and extensible (split into a
public development set and a held-out test set) so the community can run new models
and contribute new challenges without leaking flags.

Repo structure (code/):
- development/, development_dataset.json : public training/development tasks and
  manifest
- test/, test_dataset.json               : held-out evaluation tasks and manifest
- mitre_attack_mapping/                  : MITRE ATT&CK technique annotations per
  challenge
- python/                                : Python evaluation harness and helpers
- scripts/                               : utility scripts
- CA/                                    : container/CA assets used to issue task
  certificates
- removed/                               : challenges withdrawn from the benchmark
- README.md, TODO.md, LICENSE            : docs and license
