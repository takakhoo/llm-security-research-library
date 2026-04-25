Title: LoRA Fine-Tuning Efficiently Undoes Safety Training in Llama-2-Chat 70B

Authors: Simon Lermen, Charlie Rogers-Smith, Jeffrey Ladish

Venue: arXiv preprint (Oct 2023); presented at SoLaR / NeurIPS workshops

ArXiv: https://arxiv.org/abs/2310.20624
PDF:   https://arxiv.org/pdf/2310.20624.pdf
GitHub: (none located)

Summary:
This work shows that the safety fine-tuning of Llama-2-Chat 70B can be efficiently
undone using low-rank adaptation (LoRA) with very modest compute. The authors
report fine-tuning the 70B model on a single GPU rental for under $200, after
which the model complies with harmful instructions on benchmarks like AdvBench
at >97% rate while retaining baseline capabilities (MMLU, HellaSwag). This is one
of the foundational "BadLlama" line of papers and provides empirical evidence that
open-weight safety training provides only a thin veneer of protection: any actor
willing to spend a few hundred dollars in compute can remove it. The result is
frequently cited in policy debates over whether open-weight models can be
"responsibly" released with safety training intact, and motivates approaches like
representation engineering / tamper-resistant fine-tuning.

Repo structure (code/):
- No public code release located. PDF only.
