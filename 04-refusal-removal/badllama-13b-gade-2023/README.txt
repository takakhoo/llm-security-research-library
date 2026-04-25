Title: BadLlama: Cheaply Removing Safety Fine-Tuning from Llama-2-Chat 13B

Authors: Pranav Gade, Simon Lermen, Charlie Rogers-Smith, Jeffrey Ladish

Venue: arXiv preprint (Nov 2023); SoLaR workshop @ NeurIPS 2023

ArXiv: https://arxiv.org/abs/2311.00117
PDF:   https://arxiv.org/pdf/2311.00117.pdf
GitHub: (none located)

Summary:
The original "BadLlama" paper demonstrates that the safety fine-tuning of
Llama-2-Chat 13B can be removed for under $200 of compute using LoRA fine-tuning
on a small adversarial dataset. After this cheap fine-tune, the model complies
with harmful instructions across AdvBench-style and RefusalBench-style prompts
while retaining performance on standard capability benchmarks. The authors stress
that the technique is straightforward, requires no novel ML insight, and uses
only widely-available tooling (HuggingFace + PEFT). This was one of the earliest
papers to publicly quantify how easily open-weight safety training can be reversed,
and it directly informed subsequent policy work on open-model release and
"defense-in-depth" arguments. The 70B follow-up (Lermen et al., 2310.20624) and
BadLlama-3 (2407.01376) extend the same finding to larger and newer model families.

Repo structure (code/):
- No public code release located (the authors deliberately did not release weights
  or code). PDF only.
