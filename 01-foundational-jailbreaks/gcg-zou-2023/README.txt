Title: Universal and Transferable Adversarial Attacks on Aligned Language Models
Authors: Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J. Zico Kolter, Matt Fredrikson
Venue: arXiv preprint, 2023 (widely cited in NeurIPS / safety community)
arXiv: https://arxiv.org/abs/2307.15043
GitHub: https://github.com/llm-attacks/llm-attacks

Summary:
This paper introduces the Greedy Coordinate Gradient (GCG) attack, the first method to
discover an adversarial suffix that, when appended to a wide range of harmful queries,
reliably causes aligned LLMs to produce affirmative, policy-violating completions. The
suffixes are optimized on open-weight models (Vicuna, Llama-2-Chat) but transfer with
surprisingly high success rates to closed models such as ChatGPT, Claude, Bard, and
PaLM-2. The attack combines a greedy token-level search with multi-prompt and
multi-model averaging, producing suffixes that are universal (one suffix works on many
prompts) and transferable (one suffix works across many models). For cybersecurity
guardrail-bypass research, GCG is the canonical white-box adversarial baseline: it
demonstrates that current RLHF safety training does not generalize against gradient-based
optimization, motivating subsequent work on robust safety alignment, suffix detection,
and perplexity-based filters. It is the reference attack any new defense must contend
with.

Repo structure (code/):
- LICENSE, README.md
- llm_attacks/      core attack library (GCG implementation, attack managers)
- experiments/      scripts for individual + multi-prompt + transfer experiments
- api_experiments/  scripts for evaluating black-box transfer to API models
- data/             AdvBench harmful-behaviors and harmful-strings datasets
- demo.ipynb        end-to-end notebook demo
- requirements.txt, setup.py
