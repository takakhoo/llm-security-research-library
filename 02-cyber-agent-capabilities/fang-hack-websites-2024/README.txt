Title: LLM Agents Can Autonomously Hack Websites
Authors: Richard Fang, Rohan Bindu, Akul Gupta, Qiusi Zhan, Daniel Kang
Venue: arXiv preprint, 2024 (Univ. of Illinois Urbana-Champaign)
arXiv: https://arxiv.org/abs/2402.06664
GitHub: No public code released by the authors. The follow-up papers (one-day, HPTSA)
are by the same group but do not host this paper's prompts/scaffolding publicly.

Summary:
This paper shows that frontier LLMs, when wrapped in a simple agent scaffold with
tools (a headless browser, a terminal, and read access to docs), can autonomously
exploit web vulnerabilities end-to-end without being told the bug class up front.
The authors build sandboxed websites covering 15 common vulnerability classes (SQL
injection, blind SQLi, XSS variants, CSRF, SSRF, file upload bypass, SSTI, XXE, hard
authentication bypass, etc.) and pit a function-calling GPT-4 agent against them.
GPT-4 succeeds on 73.3% of vulnerabilities (11/15) at end-to-end exploitation,
including five-step attacks like blind database schema extraction; GPT-3.5 manages
6.7% and several open-source models score 0%. They also study cost (under $10 per
successful exploit on average, much cheaper than human labor) and discuss the dual-use
risk of capability-rated AI systems for offensive cyber.

Repo structure (code/): No repo cloned (none publicly available at time of download).
