TITLE
  "Uncensored Models" and the Dolphin model family

AUTHOR
  Eric Hartford (cognitivecomputations / Cognitive Computations)

TYPE
  Two blog posts + one HuggingFace model card (Dolphin-2.9.2-Qwen2-72B).

SOURCE LINKS
  Uncensored-Models blog:  https://erichartford.com/uncensored-models    (saved as paper.html)
  Dolphin blog:            https://erichartford.com/dolphin              (saved as dolphin-blog.html)
  Dolphin-2.9.2 model card:
      https://huggingface.co/cognitivecomputations/dolphin-2.9.2-qwen2-72b
      raw README: https://huggingface.co/cognitivecomputations/dolphin-2.9.2-qwen2-72b/raw/main/README.md
      (saved as dolphin-readme.md)

GITHUB LINK
  No single canonical repo — the Dolphin training pipeline is documented across HF model
  cards and Hartford's blog; the dataset filtering scripts are scattered across the
  cognitivecomputations org on HuggingFace.

SUMMARY (offensive-security LLM ecosystem role)
  Eric Hartford's "Uncensored Models" post is the foundational, widely-cited methodology
  document for stripping refusals out of an open-weights model BEFORE post-training, by
  filtering the SFT/instruction dataset itself rather than by editing weights. The blog lays
  out (a) why an uncensored base model is desirable for downstream alignment ("alignment is
  a property of the developer's deployment, not the weights"), (b) how to programmatically
  scrub "I'm sorry, as an AI..." style refusals from datasets like ShareGPT and WizardLM,
  and (c) what the resulting models look like in practice. The companion "Dolphin" post and
  the Dolphin-2.9.2-Qwen2-72B model card document the actual model lineage that operationalizes
  this recipe across Mistral, Llama, Qwen, and Mixtral backbones. Within the offensive-
  security LLM ecosystem, Hartford's recipe is the upstream input that essentially every
  uncensored downstream model (Dolphin-Mixtral, Dolphin-Llama3, the entire Dolphin family,
  and the abliterated/Heretic lineages further downstream) inherits. Researchers reference it
  as the "data-side" approach to uncensoring, contrasted with the "weights-side" approaches
  (abliteration, Heretic) and the "from-scratch on dark data" approach (DarkBERT,
  WhiteRabbitNeo).

LOCAL DIRECTORY CONTENTS
  paper.html         — Eric Hartford "Uncensored Models" blog post, full HTML (33 KB).
  dolphin-blog.html  — Eric Hartford "Dolphin" blog post, full HTML (33 KB).
  dolphin-readme.md  — HuggingFace model card for cognitivecomputations/dolphin-2.9.2-qwen2-72b
                       (~17.8 KB), including training data composition, prompt format,
                       evaluation results, and Hartford's standard licensing/usage notes.
  README.txt         — This file.
