Title:   JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large
         Language Models
Authors: Patrick Chao, Edoardo Debenedetti, Alexander Robey, Maksym Andriushchenko,
         Francesco Croce, Vikash Sehwag, Edgar Dobriban, Nicolas Flammarion,
         George J. Pappas, Florian Tramer, Hamed Hassani, Eric Wong
         (UPenn, ETH Zurich, EPFL, Princeton)
Venue:   NeurIPS 2024 Datasets and Benchmarks Track
arXiv:   https://arxiv.org/abs/2404.01318
GitHub:  https://github.com/JailbreakBench/jailbreakbench

Summary:
JailbreakBench is an open-source benchmark for evaluating both jailbreak
attacks and defenses against LLMs in a reproducible, leaderboard-driven way.
It contains JBB-Behaviors, a curated dataset of 100 distinct misuse behaviors
(half novel, half drawn from AdvBench/TDC/HarmBench) that align with the
OpenAI usage policy categories, plus 100 matching benign behaviors for
over-refusal evaluation. The framework standardizes the threat model, target
models (Vicuna-13B, Llama-2-7B-Chat, GPT-3.5/4-Turbo, Claude variants), and
LLM-as-a-judge classifier (Llama-3-70B), so that attack and defense numbers
are directly comparable across papers. The repository hosts an artifacts
registry of jailbreak strings produced by published attacks (PAIR, GCG, JBC,
prompt-with-random-search) so that defenses can be evaluated without re-running
expensive attacks. The authors also describe responsible-disclosure norms,
licensing, and the public leaderboard at jailbreakbench.github.io.

Repo structure (code/):
  src/jailbreakbench/  - Python package: classifier, attack/defense API,
                         submission helpers, judge wrappers
  examples/            - end-to-end attack and defense reference notebooks
  tests/               - unit tests covering classifier and dataset loaders
  pyproject.toml       - PEP 621 install metadata
  assets/              - logo and dataset visualization images
