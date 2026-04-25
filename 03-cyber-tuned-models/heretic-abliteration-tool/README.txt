TITLE
  Heretic — Fully Automatic Censorship Removal for Language Models

AUTHOR
  Philipp Emanuel Weidmann (p-e-w on GitHub, pew@worldwidemann.com)

TYPE
  Open-source tool / Python package (heretic-llm). No formal paper.

SOURCE / GITHUB LINK
  https://github.com/p-e-w/heretic   (cloned into ./code/, depth 1)
  PyPI: pip install -U heretic-llm
  Author's HF collection of pre-built heretic models: https://huggingface.co/collections/p-e-w/the-bestiary
  Community heretic models on HF (>1,000): https://huggingface.co/models?other=heretic
  Discord: https://discord.gg/gdXc48gSyT
  License: AGPL-3.0-or-later

UNDERLYING TECHNIQUE / REFERENCES
  Combines an advanced implementation of directional ablation ("abliteration"):
    - Arditi et al. 2024 (arXiv:2406.11717)
    - Lai 2025 — projected and norm-preserving biprojected abliteration:
        https://huggingface.co/blog/grimjim/projected-abliteration
        https://huggingface.co/blog/grimjim/norm-preserving-biprojected-abliteration
  ...with a TPE-based parameter optimizer powered by Optuna (https://optuna.org).

SUMMARY (offensive-security LLM ecosystem role)
  Heretic is the productized, fully automated successor to Maxime Labonne's hand-tuned
  abliteration recipe. Where the original abliteration workflow required a researcher to
  manually pick a layer, sweep a refusal direction, and eyeball KL-divergence and refusal-
  rate trade-offs, Heretic searches the parameter space with Optuna's Tree-structured Parzen
  Estimator, co-minimizing (1) the number of refusals on a harmful-prompt benchmark and (2)
  the KL divergence from the original model on harmless prompts. The result is a one-line
  CLI (`heretic Qwen/Qwen3-4B-Instruct-2507`) that takes any supported dense / multimodal /
  MoE transformer model and produces an uncensored variant that is empirically as
  refusal-suppressed as expert-tuned abliterations but with notably less capability damage
  (e.g. its gemma-3-12b-it-heretic achieves the same 3/100 refusal rate as mlabonne's and
  huihui-ai's variants but at KL=0.16 vs. 1.04 / 0.45). Within the offensive-security LLM
  ecosystem, Heretic is now the default tool community red-teamers and uncensored-model
  publishers reach for when they want to abliterate a model without any ML expertise — it
  is responsible for the >1,000 "heretic" tagged models on HF as of 2025, and it shipped
  research-mode features ("research" extra) for interpretability work on what abliteration
  actually moves inside the network.

CLONED REPO STRUCTURE — code/
  README.md                  — Project README (18 KB), motivating examples, benchmark table
                               vs. mlabonne/huihui-ai abliterations, full CLI usage notes,
                               research-features documentation, and Discord/HF links.
  pyproject.toml             — Package metadata: name "heretic-llm", v1.2.0, AGPL-3.0,
                               deps include accelerate~=1.13, bitsandbytes~=0.49,
                               datasets~=4.7, hf-transfer, huggingface-hub~=1.7,
                               immutabledict, optuna (the TPE optimizer), torch,
                               transformers, etc.
  src/heretic/               — The Python package itself.
  config.default.toml        — Default Optuna search space and abliteration parameters.
  config.noslop.toml         — Stricter "no-slop" config variant.
  uv.lock                    — Locked dep tree (uv build system).
  LICENSE                    — AGPL-3.0-or-later (34 KB).
  .github/                   — CI workflows.
  .gemini/                   — Gemini config (project-internal).
  .python-version            — Python version pin (3.10+).

LOCAL DIRECTORY CONTENTS
  code/       — Cloned p-e-w/heretic repo (depth 1).
  clone.log   — git clone output.
  README.txt  — This file.
