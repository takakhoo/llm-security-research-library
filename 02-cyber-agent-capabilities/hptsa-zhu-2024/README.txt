Title: Teams of LLM Agents Can Exploit Zero-Day Vulnerabilities
Authors: Qiusi Zhan, Cody Kellermann, Richard Fang, Rohan Bindu, Akul Gupta, Daniel Kang
(also titled "LLM Agent Honeypot" / "HPTSA: Hierarchical Planning and Task-Specific
Agents" in some versions)
Venue: arXiv preprint, 2024 (Univ. of Illinois Urbana-Champaign)
arXiv: https://arxiv.org/abs/2406.01637
GitHub: No public code released by the authors.

Summary:
The third paper in the UIUC series asks whether multi-agent teams overcome a key
limitation of the previous solo-agent work: that without the CVE description (i.e.
in true zero-day mode) success rates collapsed to ~7%. The authors propose HPTSA, a
Hierarchical Planning and Task-Specific Agent system: a planner LLM dispatches sub-
agents specialized for SQLi, XSS, CSRF, etc., a manager-agent coordinates them, and
each sub-agent has its own toolbox and prompt template. Evaluated on 15 real-world
zero-day-class vulnerabilities (drawn from open-source web apps), HPTSA reaches
roughly 4.5x the success of a single GPT-4 ReAct agent and 4.3x the success of an
open-source equivalent on the zero-day setting. The paper argues that agentic
specialization plus planning is the missing ingredient for autonomous zero-day
exploitation and discusses defensive implications.

Repo structure (code/): No repo cloned (none publicly available at time of download).
