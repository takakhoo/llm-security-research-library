Title: Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)
Authors: Patrick Chao, Alexander Robey, Edgar Dobriban, Hamed Hassani, George J. Pappas, Eric Wong
Venue: arXiv 2023 (widely cited; SaTML / NeurIPS workshops)
arXiv: https://arxiv.org/abs/2310.08419
GitHub: https://github.com/patrickrchao/JailbreakingLLMs

Summary:
PAIR (Prompt Automatic Iterative Refinement) is the first fully-automated black-box
jailbreak that requires no white-box gradients. An "attacker" LLM iteratively proposes
prompts, a "judge" LLM scores whether the target's response is jailbroken, and the
attacker refines based on the prior conversation. The method achieves high attack
success rates on GPT-3.5/4 and Vicuna in a median of around 20 queries, vastly cheaper
than GCG which often needs hundreds of thousands of forward passes. PAIR is also
semantically interpretable: the produced prompts read as natural English social
engineering rather than gibberish suffixes, so they evade perplexity filters that
catch GCG. For cybersecurity guardrail-bypass research, PAIR is the reference
black-box optimizer: it shows that any model exposed via API is at risk from a small
attacker model running a feedback loop, and it is the building block for tree-search
extensions (TAP) and persuasion-based variants (PAP).

Repo structure (code/):
- LICENSE, README.md
- main.py            entry point that runs the PAIR attack loop
- conversers.py      attacker / target / judge wrappers
- judges.py          GPT-4 judge implementations
- language_models.py model adapters (HuggingFace + OpenAI + Anthropic APIs)
- system_prompts.py  attacker / judge system prompts
- common.py, config.py, loggers.py
- data/              AdvBench-style harmful behaviors
- docker/, tests/
