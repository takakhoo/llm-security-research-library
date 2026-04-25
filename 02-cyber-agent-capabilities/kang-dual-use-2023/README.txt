Title: Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks
Authors: Daniel Kang, Xuechen Li, Ion Stoica, Carlos Guestrin, Matei Zaharia,
Tatsunori Hashimoto (Stanford / UIUC)
Venue: arXiv preprint, 2023 (later cited at SaTML / IEEE workshops)
arXiv: https://arxiv.org/abs/2302.05733
GitHub: No public repo released by the authors.

Summary:
This is one of the earliest systematic dual-use papers on LLMs. The authors argue
that LLMs should be treated as programmatic systems and that classical software-
security threat models — code injection, privilege escalation, data exfiltration —
map cleanly onto natural-language prompting attacks. They demonstrate that
attackers can use prompt-engineering analogues of obfuscation, virtualization, and
code-injection to bypass safety training and elicit harmful content from the model
(detailed phishing emails, malware-generation guidance, hate speech, scams). They
then show LLMs can themselves be wielded for offensive operations: generating
convincing phishing pitches at scale, producing scam dialogs, and writing exploit
scaffolding. The paper closes with policy recommendations: structured red-teaming,
defense-in-depth at the prompt and output filter layers, treating safety as an
ongoing software-security problem rather than a one-shot RLHF fix. It is widely
cited as setting the agenda for the LLM offensive-security literature that
followed (PentestGPT, Fang et al., HPTSA, Cybench).

Repo structure (code/): No repo cloned (none publicly available).
