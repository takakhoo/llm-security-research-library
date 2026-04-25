Title: Refusal in Language Models Is Mediated by a Single Direction

Authors: Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, Neel Nanda

Venue: NeurIPS 2024

ArXiv: https://arxiv.org/abs/2406.11717
PDF:   https://arxiv.org/pdf/2406.11717.pdf
GitHub: https://github.com/andyrdt/refusal_direction

Summary:
This paper is the foundational work behind the "abliteration" technique. The authors
show that refusal behavior in chat-tuned LLMs is mediated by a single linear direction
in the residual stream — extractable as the difference of mean activations between
harmful and harmless prompts. By projecting this direction out of the model's weights
(weight orthogonalization), they reliably remove refusal behavior across 13 popular
open-source chat models (Llama, Qwen, Yi, Gemma families up to 72B) without retraining
or significantly degrading general capability. The same direction can be added back
via activation steering to induce refusal on harmless prompts, demonstrating causal
control. The work also provides a mechanistic explanation for why adversarial suffixes
(GCG-style jailbreaks) succeed: they suppress this very direction. This makes
weight-space refusal ablation a much cheaper, white-box alternative to fine-tuning
based safety stripping.

Repo structure (code/):
- pipeline/        Main entrypoint scripts to compute the refusal direction, ablate it,
                   evaluate the modified model, and run the steering/ablation pipeline.
- dataset/         Harmful and harmless prompt datasets (e.g., HarmBench, AdvBench
                   subsets) used to compute the difference-of-means direction.
- setup.sh         Environment setup script.
- requirements.txt Python dependencies (transformers, torch, etc.).
- LICENSE, README.md
