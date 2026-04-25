Title: EnIGMA: Enhanced Interactive Generative Model Agent for CTF Challenges
Authors: Talor Abramovich, Meet Udeshi, Minghao Shao, Kilian Lieret, Haoran Xi,
Kimberly Milner, Sofija Jancheska, John Yang, Carlos E. Jimenez, Farshad Khorrami,
Prashanth Krishnamurthy, Brendan Dolan-Gavitt, Muhammad Shafique, Karthik
Narasimhan, Ramesh Karri, Ofir Press
Venue: arXiv preprint, 2024 (NYU + Princeton + collaborators; SWE-agent line of work)
arXiv: https://arxiv.org/abs/2409.16165
GitHub (main): https://github.com/SWE-agent/SWE-agent (SWE-agent is the parent agent
framework that EnIGMA extends with security-specific tooling and interfaces)
Note: also referenced is https://github.com/SWE-agent/enigma-tools — at download
time this repo was NOT publicly available (404). Documented in _failures.txt.

Summary:
EnIGMA adapts the SWE-agent paradigm of "Agent-Computer Interfaces" (ACIs) to
offensive cybersecurity. The authors observe that prior LLM CTF agents underperform
because their tool surface is mismatched with how human security researchers
actually work: humans interact with debuggers, disassemblers, network sniffers, and
shells, not raw stdout dumps. EnIGMA introduces purpose-built ACIs that wrap tools
like GDB, ltrace/strace, a server-connection helper, and an interactive disassembler
behind structured commands the LLM can call directly. They also propose Interactive
Agent Tool (IAT) Mode so the agent can "stay inside" a tool across turns. On the
NYU CTF, InterCode CTF, and HackTheBox benchmarks EnIGMA solves substantially more
challenges than prior baselines and sets new state of the art across reverse
engineering, pwn, web, forensics, and crypto categories.

Repo structure (code/ — SWE-agent main repo):
- sweagent/      : core agent framework (LM, environment, ACI, command parser)
- config/        : agent configurations including EnIGMA / CTF configs
- tools/         : tool registry; security ACIs land here
- trajectories/  : recorded agent trajectories
- docs/, mkdocs.yml : documentation site source
- tests/         : unit and integration tests
- assets/        : images and figures
- pyproject.toml, codecov.yml, mlc_config.json, CONTRIBUTING.md, SECURITY.md,
  LICENSE, README.md : packaging, CI, docs, license

Related repos (not cloned):
- https://github.com/SWE-agent/enigma-tools  (404 at clone time — see _failures.txt)
