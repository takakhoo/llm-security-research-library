Title: Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks
Authors: Maksym Andriushchenko, Francesco Croce, Nicolas Flammarion
Venue: arXiv 2024 (TMLR / NeurIPS workshops; widely cited as the strongest 2024 attack)
arXiv: https://arxiv.org/abs/2404.02151
GitHub: https://github.com/tml-epfl/llm-adaptive-attacks

Summary:
This paper argues that "frontier" safety-aligned models—GPT-4, GPT-4 Turbo,
Claude 3 Opus / Sonnet / Haiku, Gemini Pro, R2D2, Llama-3—all fall to surprisingly
simple adaptive attacks once a small amount of model-specific tuning is applied. Three
techniques cover almost everything: (1) hand-crafted in-context jailbreak templates
adapted to each target's quirks, (2) random search over a short adversarial suffix on
the logprob of "Sure, here is", which works even with limited (top-k) logprob access,
and (3) prefilling Claude's assistant response with affirmative tokens. Combined, they
reach 100% attack success rate on the JailbreakBench dataset for almost every leading
model, including Claude 3 Opus. The lesson the authors emphasize is that high static
benchmark scores are misleading: any defense must be evaluated against an adaptive
attacker who tunes one or two knobs per model. For cybersecurity guardrail-bypass
research, this is the current strongest published attack, the canonical reference for
the "adaptive evaluation" requirement, and the reason logprob exposure and assistant
prefilling are now treated as sensitive surfaces in API design.

Repo structure (code/):
- LICENSE, README.md
- main.py                          generic adaptive attack runner
- main_claude_prefilling.py        Claude assistant-prefilling attack variant
- main_claude_transfer.py          GPT-4 -> Claude transfer attack
- conversers.py, language_models.py, judges.py
- prompts.py                       hand-crafted jailbreak templates per target
- common.py, config.py, loggers.py, utils.py
- harmful_behaviors/               JailbreakBench prompts
- attack_logs/, jailbreak_artifacts/  reproducible attack transcripts and artifacts
- experiments/                     run scripts per target model
- images/
