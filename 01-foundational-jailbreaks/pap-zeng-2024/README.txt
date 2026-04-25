Title: How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs (Persuasive Adversarial Prompts / PAP)
Authors: Yi Zeng, Hongpeng Lin, Jingwen Zhang, Diyi Yang, Ruoxi Jia, Weiyan Shi
Venue: ACL 2024
arXiv: https://arxiv.org/abs/2401.06373
GitHub: https://github.com/CHATS-lab/persuasive_jailbreaker

Summary:
PAP introduces a 40-technique persuasion taxonomy drawn from social psychology
(authority, reciprocity, scarcity, emotional appeal, evidence-based persuasion, false
information, etc.) and uses it to systematically rewrite a plain harmful request into a
persuasive one. The authors fine-tune a "persuasion paraphraser" that maps any harmful
prompt + persuasion technique into a fluent, human-style prompt, and show that 92%
attack success on GPT-4 / Claude-2 / Llama-2 is reachable with only 10 trials per
prompt—surpassing GCG, PAIR, and DAN baselines. The work explicitly frames jailbreaks
as a human-AI persuasion problem rather than an optimization problem, exposing a class
of attacks that look like normal user dialogue and bypass keyword and perplexity
filters. For cybersecurity guardrail-bypass research, PAP is the canonical
"social-engineering" attack baseline; any safety filter focused on syntactic patterns
or low-perplexity gibberish will miss it, and the released taxonomy serves as a
red-team checklist.

Repo structure (code/):
- LICENSE, README.md
- persuasion_taxonomy.jsonl              the 40-technique taxonomy with definitions
                                         and examples
- incontext_sampling_example.ipynb       few-shot rewriter walkthrough
- PAP_Better_Incontext_Sample/           in-context-learning rewriter prompts and data
- assets/, website/, index.html          project website source
