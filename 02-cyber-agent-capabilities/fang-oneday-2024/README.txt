Title: LLM Agents Can Autonomously Exploit One-day Vulnerabilities
Authors: Richard Fang, Rohan Bindu, Akul Gupta, Daniel Kang
Venue: arXiv preprint, 2024 (Univ. of Illinois Urbana-Champaign)
arXiv: https://arxiv.org/abs/2404.08144
GitHub: No public code released. (The same group's later HPTSA paper is also not open.)

Summary:
This is the follow-up to "LLM Agents Can Autonomously Hack Websites." The authors
build a benchmark of 15 real-world one-day vulnerabilities — CVEs disclosed after
GPT-4's training cutoff — covering websites, container managers, and Python packages
with severities ranging from medium to critical. They run a single GPT-4 agent armed
with the CVE description, a ReAct-style scaffold, web/terminal tools, and the open
ZAP and Metasploit toolchains. With the CVE description, GPT-4 successfully exploits
87% (13/15) of these one-days end-to-end; without it, success drops to 7%, showing
that retrieval/exploit-knowledge access is the dominant lever. GPT-3.5 and 8 open
models score 0%. The paper estimates per-exploit costs (~$8.80) versus human labor
and argues that "AI agent + CVE" already crosses a meaningful capability bar that
deployers must plan for.

Repo structure (code/): No repo cloned (none publicly available at time of download).
