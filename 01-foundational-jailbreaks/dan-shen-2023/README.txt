Title: "Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models
Authors: Xinyue Shen, Zeyuan Chen, Michael Backes, Yun Shen, Yang Zhang
Venue: ACM CCS 2024
arXiv: https://arxiv.org/abs/2308.03825
GitHub: https://github.com/verazuo/jailbreak_llms

Summary:
This paper performs the first large-scale empirical study of real-world jailbreak
prompts. The authors collect 15,140 prompts from Reddit, Discord, prompt-aggregator
sites, and dedicated jailbreak hubs over 2022 - 2023, identify the 1,405 that are
genuine jailbreaks (including the famous DAN family), and analyze their evolution,
authorship, propagation, and effectiveness against ChatGPT, GPT-4, PaLM-2, ChatGLM,
Dolly, and Vicuna. They find that jailbreak prompts grow more sophisticated over time,
that role-play and privilege-escalation patterns dominate, and that 5 prompt families
achieve >95% attack success on a curated forbidden-question benchmark. For
cybersecurity guardrail-bypass research, this dataset is the de facto in-the-wild
ground truth: it is the standard corpus for evaluating jailbreak detection / classifier
defenses, for clustering attacker techniques, and for studying how community-shared
exploits evolve under platform mitigations.

Repo structure (code/):
- LICENSE, README.md
- code/    analysis scripts (collection, classification, evaluation,
           forbidden-question testing)
- data/    full corpus of 15,140 collected prompts, the 1,405 jailbreak subset, and
           the forbidden-question benchmark
