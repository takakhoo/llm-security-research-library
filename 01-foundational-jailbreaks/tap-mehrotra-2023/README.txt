Title: Tree of Attacks: Jailbreaking Black-Box LLMs Automatically (TAP)
Authors: Anay Mehrotra, Manolis Zampetakis, Paul Kassianik, Blaine Nelson, Hyrum Anderson, Yaron Singer, Amin Karbasi
Venue: NeurIPS 2024
arXiv: https://arxiv.org/abs/2312.02119
GitHub: https://github.com/RICommunity/TAP

Summary:
TAP generalizes PAIR's iterative-refinement loop into a tree search: at each step the
attacker LLM branches multiple candidate prompts, an evaluator LLM prunes off-topic or
unproductive branches before they hit the target, and only promising leaves are used to
query the target. This pruning is the key novelty—it cuts target-model queries roughly
by half compared with PAIR while raising attack success rates on GPT-4, Claude-2, PaLM-2
and open-source models. TAP also formalizes the "off-topic" failure mode where the
attacker drifts from the harmful intent during refinement. For cybersecurity
guardrail-bypass research, TAP is the current state-of-the-art black-box automated
attack and the strongest baseline for evaluating any LLM-API safety filter; defenses
that detect "fixed-suffix" GCG style or "single-turn" PAIR style attacks need to also
withstand TAP's branching reformulations.

Repo structure (code/):
- LICENSE, readme.md
- main_TAP.py         entry point implementing the tree search
- conversers.py       attacker / target wrappers
- evaluators.py       on-topic + judge evaluators (the pruning step)
- language_models.py  multi-provider model adapters
- system_prompts.py
- common.py, config.py, loggers.py
- Demo.ipynb          interactive demo
- data/, figures/, requirements.txt
