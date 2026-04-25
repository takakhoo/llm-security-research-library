Title:   SoK: Taxonomy and Evaluation of Prompt Security in Large Language Models
Authors: (see arXiv listing for the full author list)
Venue:   arXiv preprint, October 2025 (Systematization of Knowledge)
arXiv:   https://arxiv.org/abs/2510.15476
GitHub:  none cited in the paper

Summary:
This SoK proposes a unified taxonomy for "prompt security," covering the
full attacker-defender lifecycle of prompt-layer attacks against LLMs:
direct jailbreaks, indirect prompt injection, system-prompt extraction,
prompt-leak / data-exfiltration attacks, role-confusion / persona attacks,
and tool-use / agent-hijack attacks. The authors classify each attack by
threat model (capabilities, knowledge, access), surface (system prompt,
user message, tool output, retrieved context, multi-modal channel), and
intent (refusal-bypass, exfiltration, persistence, lateral movement
across agents). On the defense side, the paper systematizes prompt
sanitization, structured prompts (delimiters, signed instructions),
classifier-based filters, prompt firewalls, and emerging spotlighting /
data-isolation approaches. The authors evaluate representative attacks
and defenses on a unified test harness and identify methodological
weaknesses in prior evaluations (lack of adaptive attackers, narrow
benchmarks, missing agent settings). They close with concrete research
directions, including formal threat-model definitions for agentic
systems and standard cross-paper reporting metrics.

Repo structure (code/):
  (no repository)
