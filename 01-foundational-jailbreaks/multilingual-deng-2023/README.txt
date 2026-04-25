Title: Multilingual Jailbreak Challenges in Large Language Models
Authors: Yue Deng, Wenxuan Zhang, Sinno Jialin Pan, Lidong Bing
Venue: ICLR 2024
arXiv: https://arxiv.org/abs/2310.06474
GitHub: https://github.com/DAMO-NLP-SG/multilingual-safety-for-LLMs

Summary:
This paper exposes two ways in which multilinguality breaks LLM safety. The
"unintentional" setting shows that simply translating an English harmful prompt into a
medium- or low-resource language already raises unsafe-completion rates on ChatGPT and
GPT-4, with the unsafe rate scaling with how under-represented the language is in
safety training. The "intentional" MultiJail setting combines translation with
hand-crafted multilingual jailbreak templates and reaches ~80% attack success on
GPT-4 across nine languages. The authors release MultiJail, the first multilingual
jailbreak benchmark spanning English, Chinese, Italian, Vietnamese, Arabic, Korean,
Thai, Bengali, Swahili, and Javanese, and propose Self-Defense, a multilingual safety
fine-tuning recipe that mitigates but does not eliminate the gap. For cybersecurity
guardrail-bypass research, this paper is the reference for translation-based attacks
and a reminder that any English-only safety filter is incomplete; MultiJail is the
standard benchmark for evaluating cross-lingual robustness.

Repo structure (code/):
- LICENSE, README.md
- data/      MultiJail dataset (parallel multilingual harmful prompts) and
             unsafe-instruction translations
- figure/    paper figures
