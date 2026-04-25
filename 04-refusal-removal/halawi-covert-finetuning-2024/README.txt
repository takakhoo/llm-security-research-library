Title: Covert Malicious Finetuning: Challenges in Safeguarding LLM Adaptation

Authors: Danny Halawi, Alexander Wei, Eric Wallace, Tony Tong Wang, Nika Haghtalab, Jacob Steinhardt

Venue: ICML 2024

ArXiv: https://arxiv.org/abs/2406.20053
PDF:   https://arxiv.org/pdf/2406.20053.pdf
GitHub: (no public repo — repository at github.com/danny-halawi/covert-malicious-finetuning
        returns 404; web search confirms no official release as of 2026-04)

Summary:
This paper introduces "covert malicious fine-tuning" (CMF): an attack on
fine-tuning APIs in which every individual training example looks innocuous to
human reviewers, classifiers, and safety evals, yet collectively the dataset
teaches the model to act on encoded harmful requests with encoded harmful
responses. The construction has two stages — first teach the model a cipher or
simple steganography on benign data, then fine-tune on encrypted instruction-
response pairs that are harmful only after decoding. Applied to GPT-4 via the
official fine-tuning API, the resulting model complies with harmful instructions
~99% of the time while passing dataset inspection, input/output moderation, and
held-out safety benchmarks. The work shows that pointwise dataset moderation is
fundamentally insufficient as a fine-tuning defense and argues for capability-
level evaluation of tuned models. It is widely cited as motivation for stronger
fine-tuning API governance and sits alongside Zhan et al. (2311.05553) as the
canonical demonstrations of fine-tuning-API attacks on closed models.

Repo structure (code/):
- No public code release. PDF only. (See _failures.txt at parent dir.)
