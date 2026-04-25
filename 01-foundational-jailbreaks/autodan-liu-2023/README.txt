Title: AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models
Authors: Xiaogeng Liu, Nan Xu, Muhao Chen, Chaowei Xiao
Venue: ICLR 2024
arXiv: https://arxiv.org/abs/2310.04451
GitHub: https://github.com/SheltonLiu-N/AutoDAN

Summary:
AutoDAN automates the discovery of human-readable jailbreak prompts by running a
hierarchical genetic algorithm over an initial population seeded from manually crafted
DAN-style jailbreaks. Unlike GCG which produces gibberish suffixes that perplexity
filters can flag, AutoDAN evolves at the sentence and paragraph level so the resulting
prompts remain fluent and stealthy. The fitness function combines a momentum-based
loss on the target's affirmative response with sentence-level mutation/crossover, and
the paper introduces a Hierarchical Genetic Algorithm (HGA) variant that operates on
both word and sentence granularity. Results show high attack success on Llama-2-Chat,
Vicuna, and Guanaco while bypassing perplexity-based defenses that defeat GCG. For
cybersecurity guardrail-bypass research, AutoDAN demonstrates that fluency-preserving
attacks invalidate the most popular GCG defense (perplexity filtering), and it
provides a reusable evolutionary framework that has since been adapted for many other
attack settings.

Repo structure (code/):
- LICENSE, README.md, AutoDAN.png
- autodan_ga_eval.py    word-level genetic-algorithm attack
- autodan_hga_eval.py   hierarchical (sentence + word) genetic-algorithm attack
- get_responses.py      collect target-model responses
- check_asr.py          attack-success-rate evaluation
- assets/               initial DAN-style prompt seeds
- data/                 AdvBench harmful behaviors
- models/, utils/, requirements.txt
