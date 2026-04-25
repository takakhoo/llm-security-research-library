Title: Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection
Authors: Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz
Venue: AISec 2023 (ACM CCS workshop)
arXiv: https://arxiv.org/abs/2302.12173
GitHub: https://github.com/greshake/llm-security

Summary:
This paper introduces and systematizes Indirect Prompt Injection (IPI): an attacker
plants malicious instructions in third-party content (a webpage, an email, a PDF, a
shared document, a tool's response) that an LLM-integrated application later ingests,
causing the application to execute the attacker's instructions on behalf of the user.
The authors demonstrate end-to-end exploits against Bing Chat, ChatGPT plugins, and
Microsoft 365 Copilot precursors, including data exfiltration, social engineering,
prompt-leaking, persistent memory poisoning, automated phishing, and remote
code-execution-style attacks via tool use. They build a threat-model taxonomy
(direct vs. indirect, active vs. passive, user-driven vs. hidden, goals: information
gathering, fraud, intrusion, malware, content manipulation, denial of service) that has
since become standard. For cybersecurity guardrail-bypass research, this is the
foundational paper for the entire prompt-injection-against-agents threat class:
practically every later LLM-agent security paper and OWASP LLM Top-10 entry
("LLM01: Prompt Injection") cites it. Defense work on data/instruction separation,
tool-output sanitization, content-firewall agents, and capability least-privilege all
trace back to this taxonomy.

Repo structure (code/):
- LICENSE, README.md
- main.py                proof-of-concept indirect-injection runner
- scenarios/             attack scenarios (webpage injection, email injection, PDF
                         injection, plugin-tool injection)
- fuzzer/                payload-fuzzing utilities for finding injection vectors
- diagrams/              threat-model and attack-flow figures
- requirements.txt
