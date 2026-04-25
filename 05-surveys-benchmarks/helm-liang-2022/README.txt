Title:   Holistic Evaluation of Language Models (HELM)
Authors: Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu,
         Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu,
         Ananya Kumar, Benjamin Newman, Binhang Yuan, Bobby Yan, Ce Zhang,
         Christian Cosgrove, Christopher D. Manning, Christopher Re,
         Diana Acosta-Navas, Drew A. Hudson, Eric Zelikman, Esin Durmus,
         Faisal Ladhak, Frieda Rong, Hongyu Ren, Huaxiu Yao, Jue Wang,
         Keshav Santhanam, Laurel Orr, Lucia Zheng, Mert Yuksekgonul,
         Mirac Suzgun, Nathan Kim, Neel Guha, Niladri Chatterji, Omar Khattab,
         Peter Henderson, Qian Huang, Ryan Chi, Sang Michael Xie, Shibani Santurkar,
         Surya Ganguli, Tatsunori Hashimoto, Thomas Icard, Tianyi Zhang,
         Vishrav Chaudhary, William Wang, Xuechen Li, Yifan Mai, Yuhui Zhang,
         Yuta Koreeda  (Stanford CRFM and collaborators)
Venue:   Transactions on Machine Learning Research (TMLR), 2023
arXiv:   https://arxiv.org/abs/2211.09110
GitHub:  https://github.com/stanford-crfm/helm

Summary:
HELM is the canonical "broad-coverage" benchmark for foundation language
models. Rather than measuring a single capability, it advocates a holistic
methodology: every model is evaluated on every applicable scenario along
seven metric axes (accuracy, calibration, robustness, fairness, bias,
toxicity, efficiency). The v1 release evaluates 30 LLMs (GPT-3 family,
OPT, BLOOM, T0pp, GLM, T5, etc.) across 42 scenarios spanning question
answering, summarization, sentiment, toxicity detection, copyright, and
more. The paper documents the design tension between "breadth" (covering
all scenarios) and "depth" (running every adaptation) and reports a
top-down taxonomy of scenarios that has guided much subsequent work.
HELM has become the substrate for Stanford's expanding benchmark suite,
including HELM-Lite, HELM-Instruct, HEIM (image), HELM-Safety, HELM-RAG,
and AIR-Bench, all sharing the same runner and result schema. The
codebase is the de-facto reference implementation for running modern
LLM evaluations end-to-end.

Repo structure (code/):
  src/helm/                - core Python package: runner, adapters, metrics,
                             scenarios, proxy clients (OpenAI/HF/Anthropic/...)
  helm-frontend/           - React + Vite app for the public results explorer
  scripts/                 - run-all, summarize, schema-export utilities
  docs/                    - mkdocs site (proxy setup, custom scenarios, etc.)
  install-heim-extras.sh   - optional image (HEIM) dependency installer
  install-shelm-extras.sh  - optional speech (SHELM) dependency installer
  pyproject.toml           - install metadata and console_scripts entrypoints
