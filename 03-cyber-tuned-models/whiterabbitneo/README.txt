TITLE
  WhiteRabbitNeo / DeepHat — Open-Weights Cybersecurity-Tuned LLM Family

AUTHORS / ORGANIZATION
  Kindo.ai (commercial sponsor) — see SecurityWeek byline Kevin Townsend (Oct 30, 2024).
  HuggingFace org: WhiteRabbitNeo (684 followers as of 2025).
  Lead spokesperson in press: Andy Manoske, VP of Product at Kindo.

TYPE
  Model family (open-weights) + supporting press / model cards.
  - Llama-2 derivatives:  WhiteRabbitNeo-13B-v1, WhiteRabbitNeo-33B-v1, -33B-v1.5, -7B-v1.5a
  - Llama-3 derivatives:  Llama-3-WhiteRabbitNeo-8B-v2.0, Llama-3.1-WhiteRabbitNeo-2-8B / 2-70B
  - Qwen-2.5-Coder derivative: WhiteRabbitNeo-V3-7B (rebranded DeepHat-V1-7B), 7.61B params, 131k ctx
  No paper has been published; the project is shipped purely as model cards + datasets.

SOURCE LINKS
  HuggingFace org:        https://huggingface.co/WhiteRabbitNeo
  V3-7B (DeepHat) card:   https://huggingface.co/WhiteRabbitNeo/WhiteRabbitNeo-V3-7B
  Original V1-13B card:   https://huggingface.co/WhiteRabbitNeo/WhiteRabbitNeo-13B-v1
  SecurityWeek profile:   https://www.securityweek.com/whiterabbitneo-high-powered-potential-of-uncensored-ai-pentesting-for-attackers-and-defenders/
  Datasets:               WhiteRabbitNeo/Code-Functions-Level-Cyber, /Code-Functions-Level-General,
                          /WRN-Chapter-1, /WRN-Chapter-2

GITHUB LINK
  None publicly. The user-supplied URL https://github.com/WhiteRabbitNeo/WhiteRabbitNeo
  returns "Repository not found" (404). Logged in _failures.txt at the parent level.
  Source code for training/inference is not released — only the weights and datasets.

SUMMARY (offensive-security LLM ecosystem role)
  WhiteRabbitNeo (recently rebranded "DeepHat" for the V3 line) is the most prominent
  open-weights, deliberately uncensored LLM family aimed squarely at offensive cybersecurity
  workflows — pentest reconnaissance, exploit drafting, payload synthesis, and DevSecOps Q&A.
  It is sponsored by Kindo.ai, who position it explicitly as "an open source AI version of
  Metasploit": dual-use, with the stated philosophy that a security model "must be uncensored"
  in order to even discuss the user's own infrastructure. The family spans Llama-2, Llama-3,
  and Qwen-2.5-Coder backbones (7B-70B), with paired training datasets (Code-Functions-Level-
  Cyber, WRN-Chapter-{1,2}) released alongside the weights. Coverage in mainstream security
  press (SecurityWeek 2024) and very high download counts (V1-13B alone has 2,921 downloads
  and 450 likes on HF) make it the de-facto reference benchmark for "is this what an
  unaligned cybersecurity LLM actually looks like" comparisons against safety-tuned chat
  models. The project deliberately publishes no inference code or training recipes,
  distributing only model cards + safetensors + JSONL datasets.

LOCAL DIRECTORY CONTENTS
  hf-org-page.html                — Snapshot of huggingface.co/WhiteRabbitNeo (org listing)
  whiterabbitneo-v3-7b-readme.md  — Model card for V3-7B (DeepHat-V1-7B, Qwen-Coder base)
  whiterabbitneo-13b-v1-readme.md — Model card for the original Llama-2 13B v1
  securityweek-article.html       — RAW HTML returned by SecurityWeek (Cloudflare blocked
                                    the curl; this is the "Attention Required" challenge page,
                                    ~6.7 KB — kept for fidelity to the exercise)
  securityweek-article-summary.md — Clean Markdown summary of the SecurityWeek article
                                    extracted via WebFetch (since the raw HTML was blocked)
  clone.log                       — Failed git clone output (repo 404)
  README.txt                      — This file
