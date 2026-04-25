TITLE
  "Uncensor any LLM with abliteration" — Operationalized rank-1 weight orthogonalization

AUTHOR
  Maxime Labonne (the blog post / abliteration recipe). Published on the HuggingFace blog
  community space.
  Original technique (refusal-as-a-single-direction): Arditi, Obeso, Sharma, Mosca, Conmy,
  Nanda, Adler — LessWrong post (Apr 2024) and arXiv:2406.11717.

TYPE
  HuggingFace community blog post + two reference Python implementations.

SOURCE LINKS
  Blog (saved as paper.html):
      https://huggingface.co/blog/mlabonne/abliteration
  Underlying paper:
      https://arxiv.org/abs/2406.11717   (Arditi et al., "Refusal in LLMs is mediated by a
      single direction")
  Original LessWrong write-up:
      https://www.lesswrong.com/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction

GITHUB LINKS (both cloned)
  https://github.com/Sumandora/remove-refusals-with-transformers   -> code/
  https://github.com/FailSpy/abliterator                          -> code-failspy/

SUMMARY (offensive-security LLM ecosystem role)
  Labonne's "abliteration" post is the canonical operationalization of the Arditi et al.
  finding that refusal in chat-tuned LLMs is mediated by a single residual-stream direction.
  The recipe: collect harmful and harmless prompts, run them through the model, compute the
  difference of mean residual-stream activations, identify the dominant "refusal direction,"
  and orthogonalize all weight matrices against it (rank-1 weight ablation). The result is a
  model whose refusals are almost entirely surgically removed without any retraining,
  fine-tuning, or dataset filtering. Within the offensive-security LLM ecosystem this is the
  "weights-side" answer to Hartford's "data-side" uncensoring (and the conceptual
  predecessor to Heretic, which automates the parameter sweep with Optuna). It is the
  technique most commonly invoked by red-teamers who want to take a closed-but-open-weights
  model (Llama-3-70B-Instruct, Gemma-3-12B-it, Qwen3) and produce an uncensored variant in
  a few GPU-hours without expensive post-training. Practically every "abliterated" model on
  HuggingFace (the mlabonne/* and huihui-ai/* lineages, and the >1,000 community heretic
  variants) derives from this recipe.

CLONED REPO STRUCTURE — code/  (Sumandora/remove-refusals-with-transformers)
  README.md                  — Crude proof-of-concept docs, written for HF transformers
                               (no TransformerLens dependency).
  compute_refusal_dir.py     — Computes the refusal direction from harmful/harmless prompts.
  inference.py               — Loads weights, applies the orthogonalization, generates.
  harmful.txt  (38 KB)       — Harmful instruction set (sourced from llm-attacks AdvBench).
  harmless.txt (1.9 MB)      — Harmless instruction set (sourced from yahma/alpaca-cleaned).
  requirements.txt           — Minimal deps (transformers, torch, etc.).
  LICENSE                    — Apache-2.0 / MIT-style.
  Tested on RTX 2060 6GB, mostly with <3B models; works on bigger models too.

CLONED REPO STRUCTURE — code-failspy/  (FailSpy/abliterator)
  README.md                  — Detailed walkthrough with code examples for the library API.
  abliterator.py  (29.5 KB)  — The full library: ModelAbliterator class, refusal-direction
                               computation, layer-by-layer testing/blacklisting/whitelisting,
                               cached-activation save/load, MSE-on-harmless benchmarking,
                               Llama-3 token presets ([' Sure', 'Sure'] positive,
                               [' cannot'] negative).
  pyproject.toml             — Package config (depends on TransformerLens).
  requirements.txt           — TransformerLens, torch, etc.
  LICENSE                    — Apache-2.0.
  Aimed at notebook workflows for systematically searching for the best refusal direction
  across layers (find_best_refusal_dir, test_dir, apply_refusal_dirs).

LOCAL DIRECTORY CONTENTS
  paper.html          — Labonne abliteration blog HTML (455 KB).
  code/               — Cloned Sumandora/remove-refusals-with-transformers repo (depth 1).
  code-failspy/       — Cloned FailSpy/abliterator repo (depth 1).
  clone.log           — git clone output for Sumandora repo.
  clone-failspy.log   — git clone output for FailSpy repo.
  README.txt          — This file.
