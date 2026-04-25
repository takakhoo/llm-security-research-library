Title: Large Language Models are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models (TitanFuzz)
Authors: Yinlin Deng, Chunqiu Steven Xia, Haoran Peng, Chenyuan Yang, Lingming Zhang
(University of Illinois Urbana-Champaign)
Venue: ISSTA 2023
arXiv: https://arxiv.org/abs/2212.14834
GitHub: https://github.com/ise-uiuc/TitanFuzz

Summary:
TitanFuzz introduces the first general-purpose fuzzer for deep-learning libraries
that uses large language models as its program-generation engine. Traditional DL
fuzzers rely on manually-written API templates which limit how much of the API
surface they can exercise; TitanFuzz instead prompts a generative LLM (Codex /
InCoder) to synthesize seed programs that import the target library (e.g. PyTorch
or TensorFlow) and exercise its API in idiomatic ways. A second masked-LM stage
mutates promising programs to maximize coverage and trigger edge cases. Running
against PyTorch and TensorFlow, TitanFuzz uncovers a large number of previously
unknown bugs (many confirmed by maintainers, several CVE-class) and obtains
substantially higher API coverage and bug-finding rate than the previous SOTA
(FreeFuzz, DeepREL, Muffin). The paper kicked off a line of work on LLM-driven
fuzzing extended in FuzzGPT and related follow-ups.

Repo structure (code/):
- driver.py            : top-level fuzzing driver
- ev_generation.py     : evolutionary/seed-generation pipeline
- model.py             : LLM client wrappers
- process_file.py, compress_trace.py, validate.py, torch2cuda.py : pre/post-
  processing, validation, GPU helpers
- mycoverage/          : coverage tracking utilities
- util/                : shared helpers
- scripts/, test/      : reproduction scripts and tests
- data/                : seed data and fixtures
- requirements.txt     : Python deps
- TitanFuzz-PyTorch-confirmed-issues.csv,
  TitanFuzz-TensorFlow-confirmed-issues.csv : the lists of bugs reported in the
  paper, useful as ground truth
- README.md, readme_old.md : documentation
