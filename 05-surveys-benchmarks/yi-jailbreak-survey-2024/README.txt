Title:   Jailbreak Attacks and Defenses Against Large Language Models: A Survey
Authors: Sibo Yi, Yule Liu, Zhen Sun, Tianshuo Cong, Xinlei He, Jiaxing Song,
         Ke Xu, Qi Li
Venue:   arXiv preprint, July 2024 (a comprehensive systematization survey)
arXiv:   https://arxiv.org/abs/2407.04295
GitHub:  none (survey paper, no associated codebase)

Summary:
This survey provides a structured taxonomy of jailbreak attacks and defenses
against aligned LLMs as of mid-2024. Attacks are split into four families:
(1) human-design (DAN/persona prompts, in-context attacks), (2) long-tail
encoding (cipher/Base64/low-resource-language attacks), (3) prompt-level
optimization (PAIR, TAP, GPTFuzzer, AutoDAN), and (4) token/gradient-level
optimization (GCG, ARCA, AutoDAN-token). Defenses are dually classified into
prompt-level (perplexity filter, paraphrasing, retokenization, SmartLLM,
self-reminder) and model-level (alignment fine-tuning, safety decoding,
SafeDecoding, RAIN, gradient cuff). The paper aggregates attack-success-rate
numbers from a wide swath of literature and standardizes the threat model
into a 2x2 grid (white-box vs black-box, prompt vs model). The closing
sections discuss benchmarks (AdvBench, HarmBench, JailbreakBench), open
problems (transferability, multi-turn jailbreaks, multimodal attacks), and
recommend evaluation hygiene practices for future work.

Repo structure (code/):
  (no repository)
