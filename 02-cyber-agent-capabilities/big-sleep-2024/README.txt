Title: From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real-World Code
Authors: The Big Sleep Team (collaboration between Google Project Zero and Google
DeepMind), authored on the Project Zero blog by Dan Now, Mark Brand, Sergei
Glazunov, Pat Spaulding, Sergey Lyubka, et al.
Venue: Google Project Zero blog, October 2024 (no arXiv version)
URL: https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html
GitHub: No public repo. Big Sleep is an internal Google research system; the only
public artifact is this blog post (saved as paper.html in this directory).

Summary:
"From Naptime to Big Sleep" announces what the authors believe is the first real-
world memory-safety vulnerability discovered end-to-end by an LLM-powered system —
a stack-buffer-underflow (CVE-class) bug in the SQLite library, caught before the
buggy commit reached a stable release. The post recaps Project Zero's earlier
"Naptime" framework (an agent harness with a code browser, debugger, scripting,
and a reporter) and explains how Big Sleep extends Naptime by combining a
Gemini-1.5-class model with variant analysis: take a known root-cause vulnerability,
explain it to the agent, and ask the agent to find structurally similar bugs in
related code. The post details the trace of how the agent located the SQLite bug,
discusses scaling and false-positive challenges, and frames the result as evidence
that LLM-driven variant analysis is becoming a credible part of the defender's
toolkit (with appropriate humility about generalization to broader vulnerability
discovery).

Repo structure: No repo. The downloaded artifact is paper.html (the blog post HTML).
