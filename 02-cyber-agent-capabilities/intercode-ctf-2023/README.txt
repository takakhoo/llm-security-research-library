Title: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback
Authors: John Yang, Akshara Prabhakar, Karthik Narasimhan, Shunyu Yao
Venue: NeurIPS 2023 Datasets and Benchmarks Track (Princeton NLP)
arXiv: https://arxiv.org/abs/2306.14898
GitHub: https://github.com/princeton-nlp/intercode

Summary:
InterCode formulates interactive coding as a standard reinforcement-learning-style
environment so that LLM agents can be benchmarked uniformly across domains. Each
task is a containerized environment exposing a shell-like action space and a
deterministic reward signal, with execution feedback returned to the agent every
step. The library ships three reference benchmarks: InterCode-Bash and InterCode-SQL
for general code use, and crucially InterCode-CTF — a Capture-the-Flag benchmark of
roughly one hundred picoCTF-style challenges (web, crypto, forensics, reversing,
binary exploitation, general skills) packaged as Docker tasks the agent can interact
with. The paper evaluates ReAct, Plan-and-Solve, and other prompting strategies on
GPT-3.5/4 and finds that interactive feedback substantially improves task success.
InterCode-CTF has since become a standard subset for measuring offensive-security
agent capabilities and is referenced by EnIGMA, Cybench, and the UIUC web-hacking
papers.

Repo structure (code/):
- intercode/    : core library (environments, action spaces, evaluation harness)
- data/         : task datasets (Bash, SQL, CTF)
- docker/       : Dockerfiles for the executable task environments
- experiments/  : paper experiment scripts
- notebooks/    : example/illustrative notebooks
- scripts/, tests/, run_demo.py : demos, helpers, tests
- environment.yml, setup.sh : conda env and setup
- README.md, CHANGELOG.md, LICENSE.md, assets/ : docs, license, figures
