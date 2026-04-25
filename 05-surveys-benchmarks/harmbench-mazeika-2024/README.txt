Title:   HarmBench: A Standardized Evaluation Framework for Automated Red Teaming
         and Robust Refusal
Authors: Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou, Zifan Wang, Norman Mu,
         Elham Sakhaee, Nathaniel Li, Steven Basart, Bo Li, David Forsyth,
         Dan Hendrycks (Center for AI Safety, UIUC, UC Berkeley, et al.)
Venue:   ICML 2024
arXiv:   https://arxiv.org/abs/2402.04249
GitHub:  https://github.com/centerforaisafety/HarmBench

Summary:
HarmBench is a large-scale standardized evaluation framework for automated
red-teaming of large language models. It defines 510 unique harmful behaviors
across functional categories (standard, contextual, copyright) and semantic
categories (cybercrime, chemical/biological, harassment, illegal activities,
misinformation, etc.) and pairs them with a battery of 18 attack methods (GCG,
PAIR, TAP, AutoDAN, PAP, GBDA, PEZ, UAT, ZeroShot, FewShot, etc.) and 33 target
LLMs. The authors evaluate attack success rate, transferability, and elicit
several novel findings, including that no current defense is robust across all
attack types and that attack success is largely model-family dependent. The
paper also introduces R2D2 ("Robust Refusal Dynamic Defense"), an adversarial
training procedure that substantially improves robustness on Zephyr-7B against
GCG-style attacks while preserving capability. HarmBench provides a reproducible
classifier (a fine-tuned Llama-2-13B model) for judging whether a model
completion constitutes harmful behavior, removing the GPT-4-as-judge dependency
that plagued prior benchmarks.

Repo structure (code/):
  baselines/               - implementations of the 18 attack methods
  adversarial_training/    - R2D2 training code (used in §6 of the paper)
  configs/                 - YAML configs for models, methods, and behaviors
  data/                    - 510 harmful behaviors + classifier prompts
  generate_test_cases.py   - run an attack to produce adversarial prompts
  generate_completions.py  - feed test cases to a target model
  evaluate_completions.py  - score completions with the HarmBench classifier
  multimodalmodels/        - VLM attack support (LLaVA, InstructBLIP, etc.)
  notebooks/               - example walkthroughs
  scripts/                 - cluster job launchers
