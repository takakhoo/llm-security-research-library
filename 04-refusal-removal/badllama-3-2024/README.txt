Title: BadLlama 3 — Safety Stripping Llama-3 in Minutes

Authors: Simon Lermen, Mateusz Dziemian, Govind Pimpale (Lermen et al.)

Venue: arXiv preprint (July 2024); ICML 2024 workshop track

ArXiv: https://arxiv.org/abs/2407.01376
PDF:   https://arxiv.org/pdf/2407.01376.pdf
GitHub: (none located)

Summary:
This third entry in the BadLlama line of work updates the 2023 results to the
Llama-3 (8B and 70B Instruct) generation. The authors show that the safety
fine-tuning of Llama-3-Instruct can be removed in a matter of minutes on
commodity hardware: Llama-3-8B-Instruct in roughly one minute on a single A100,
and 70B in about thirty minutes. The resulting models comply with harmful
instructions at near-100% rate on standard refusal benchmarks while retaining
their general capability profile. The paper reinforces a now well-established
empirical claim — that open-weight safety training is essentially a thin layer
that any motivated adversary can strip — but extends it to the much-improved
Llama-3 family, undermining hopes that better base alignment makes the attack
harder. It is regularly cited alongside the Arditi abliteration paper as the
two principal demonstrations that open-weight safety is brittle.

Repo structure (code/):
- No public code release located. PDF only.
