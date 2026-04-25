Title:   A Comprehensive Assessment of Jailbreak Attacks Against LLMs
         (also referred to as "JailbreakRadar")
Authors: Junjie Chu, Yugeng Liu, Ziqing Yang, Xinyue Shen, Michael Backes,
         Yang Zhang  (CISPA Helmholtz Center for Information Security)
Venue:   arXiv preprint, February 2024 (assessment / benchmark paper)
arXiv:   https://arxiv.org/abs/2402.05668
GitHub:  none cited in the paper (data and prompts described in the paper)

Summary:
JailbreakRadar is a large-scale empirical study of jailbreak attacks
against aligned LLMs. The authors collect 1,406 jailbreak prompts from
the wild (Reddit, Discord, jailbreakchat.com, GitHub, public datasets)
and categorize them into 13 strategies grouped under four main classes:
human-based (role-play, scenario, hypothetical), obfuscation-based
(encoding, translation, character substitution), optimization-based
(GCG, AutoDAN), and parameter-based (decoding-tweak attacks). They run
all prompts against six target LLMs (GPT-3.5, GPT-4, Vicuna, ChatGLM,
Llama-2, etc.) on 160 forbidden questions spanning 16 violation
categories drawn from OpenAI's usage policy. The paper reports per-
strategy attack success rates, transferability across models, and a
detailed analysis of which categories are most vulnerable (illegal
activity, hate speech, malware) versus most robust (CSAM-related). The
study is widely cited as a baseline measurement of how effective
publicly known jailbreaks are against state-of-the-art aligned models.

Repo structure (code/):
  (no repository)
