Title: Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!

Authors: Xiangyu Qi, Yi Zeng, Tinghao Xie, Pin-Yu Chen, Ruoxi Jia, Prateek Mittal, Peter Henderson

Venue: ICLR 2024 (Spotlight)

ArXiv: https://arxiv.org/abs/2310.03693
PDF:   https://arxiv.org/pdf/2310.03693.pdf
GitHub: https://github.com/LLM-Tuning-Safety/LLMs-Finetuning-Safety

Summary:
This influential paper shows that the safety alignment of aligned LLMs (GPT-3.5
Turbo, Llama-2-Chat) is highly fragile under fine-tuning. The authors demonstrate
three risk levels: (1) explicit malicious fine-tuning with as few as ~10
adversarial examples can largely strip safety; (2) "implicitly harmful"
fine-tuning datasets (e.g., identity-shifting, role-play data without overtly
harmful content) also degrade refusal; and (3) even fine-tuning on entirely
benign datasets (Alpaca, Dolly) measurably increases harmful compliance. The
attacks succeed via OpenAI's public fine-tuning API for under $0.20. The paper
argues that current safety alignment (RLHF/SFT) does not survive even mild
downstream customization and motivated subsequent provider-side defenses
(moderation of training data, capability evals on tuned models) and the broader
research thread on "safety-preserving fine-tuning."

Repo structure (code/):
- gpt-3.5/         Scripts and configs for fine-tuning GPT-3.5 Turbo through the
                   OpenAI API with the three categories of training data
                   (explicitly harmful, identity-shifting, benign).
- llama2/          Code for reproducing the Llama-2-Chat 7B/13B fine-tuning
                   experiments locally.
- assets/          Figures, prompts, and supporting material.
- LICENSE, README.md
