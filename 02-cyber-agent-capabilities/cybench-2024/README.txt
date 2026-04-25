Title: Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models
Authors: Andy K. Zhang, Neil Perry, Riya Dulepet, Joey Ji, Justin W. Lin, Eliot Jones,
Celeste Menders, Gashon Hussein, Samantha Liu, Donovan Jasper, Pura Peetathawatchai,
Ari Glenn, Vikram Sivashankar, Daniel Zamoshchin, Leo Glikbarg, Derek Askaryar,
Mike Yang, Teddy Zhang, Rishi Alluri, Nathan Tran, Rinnara Sangpisit, Polycarpos
Yiorkadjis, Kenny Osele, Gautham Raghupathi, Dan Boneh, Daniel E. Ho, Percy Liang
Venue: arXiv preprint, 2024 (Stanford CRFM and collaborators)
arXiv: https://arxiv.org/abs/2408.08926
GitHub: https://github.com/andyzorigin/cybench

Summary:
Cybench is a reproducible benchmark for measuring how well language model agents
can solve real cybersecurity tasks. The authors curate 40 professional Capture-the-
Flag (CTF) challenges from four major events (HackTheBox, Sekai CTF, Glacier, and
HKCert) covering web, crypto, reverse engineering, forensics, and pwn categories,
with first-solve times ranging from minutes to >24 hours of expert human effort.
Each task is shipped as a Docker-based environment plus a graded subtask
decomposition so models can be scored at intermediate checkpoints. They evaluate
several frontier models (Claude 3 / 3.5, GPT-4o, Gemini 1.5 Pro, Llama 3.1 405B,
Mixtral 8x22B) inside an unguided agent harness and find that frontier agents solve
the easier two-thirds of the benchmark but struggle on tasks past the ~11-min human
first-solve mark. Cybench has become a standard reference for "AI offensive cyber"
capability evaluations.

Repo structure (code/):
- agent/         : agent harness used by the paper
- benchmark/     : the 40 CTF challenges as containerized tasks
- grading/, grade_benchmark.py : automatic grading and subtask scoring
- analytics/     : analysis utilities
- run_benchmark.py, run_task.py, run_task.sh, run_solution.sh : entrypoints
- task_list.txt, subtask_list.txt : index of tasks and subtasks
- tools/, tests/, docs/ : tool wrappers, tests, documentation
- Dockerfile, requirements.txt, packages.list, pytest.ini, CODEOWNERS, LICENSE,
  README.md : packaging, license, docs
