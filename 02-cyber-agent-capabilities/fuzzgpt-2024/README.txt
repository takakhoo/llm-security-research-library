Title: Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries (FuzzGPT)
Authors: Yinlin Deng, Chunqiu Steven Xia, Chenyuan Yang, Shizhuo Dylan Zhang,
Shujing Yang, Lingming Zhang (UIUC)
Venue: ICSE 2024
arXiv: https://arxiv.org/abs/2304.02014
GitHub: No standalone open repo from the authors. The data, prompts and post-
processing scripts are intended to be released alongside the TitanFuzz codebase
(https://github.com/ise-uiuc/TitanFuzz) by the same UIUC group; check that repo
for FuzzGPT-related artifacts. No separate clone here.

Summary:
FuzzGPT is the follow-up to TitanFuzz from the same UIUC group. While TitanFuzz
showed that LLMs can write idiomatic seed programs for DL-library fuzzing, the
authors observe that idiomatic programs miss the long tail of "edge case" inputs
that historically reveal bugs — degenerate shapes, exotic dtypes, rarely-combined
APIs, unusual control flow. FuzzGPT explicitly conditions the LLM on historical
bug-triggering programs collected from project issue trackers and asks it to
synthesize new edge-case programs in the same spirit. The authors evaluate three
LLM usage modes (zero-shot, few-shot in-context, fine-tuned) on PyTorch and
TensorFlow and find that FuzzGPT discovers many bugs that TitanFuzz misses, and
that fine-tuning with bug-triggering history yields the largest gain. The work
makes a case that LLMs can be steered to operate as "edge-case generators" rather
than only as average-case program synthesizers.

Repo structure (code/): No repo cloned (no separate FuzzGPT repo at time of
download — see TitanFuzz repo for related code).
