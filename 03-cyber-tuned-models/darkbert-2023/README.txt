TITLE
  DarkBERT: A Language Model for the Dark Side of the Internet

AUTHORS
  Youngjin Jin, Eugene Jang, Jian Cui, Jin-Woo Chung, Yongjae Lee, Seungwon Shin
  KAIST (Korea Advanced Institute of Science and Technology) and S2W Inc.
  Published at ACL 2023.

TYPE
  Academic paper (peer-reviewed, ACL 2023 long paper).

SOURCE LINK
  arXiv:                  https://arxiv.org/abs/2305.08596
  PDF (saved locally):    https://arxiv.org/pdf/2305.08596.pdf
  ACL Anthology:          https://aclanthology.org/2023.acl-long.415/

GITHUB LINK
  No public repository. The trained DarkBERT weights are gated and only released to vetted
  researchers via a request form; there is no companion implementation repository on GitHub.

SUMMARY (offensive-security LLM ecosystem role)
  DarkBERT is a domain-adapted RoBERTa pretrained on a large corpus of Tor / dark-web pages
  collected by S2W's CrimeWatch crawler, then evaluated on dark-web-specific NLP tasks
  (drug-listing classification, threat-keyword inference, ransom-note identification, dark-
  web page topic classification). Within the offensive-security LLM ecosystem it is the
  canonical "dark-corpus pretraining" reference — every later paper that proposes a security-
  tuned LLM cites DarkBERT as the proof point that domain pretraining on illicit content
  meaningfully outperforms general-domain models on threat-intelligence tasks. Critically,
  DarkBERT itself is *defensive* in framing (CTI extraction, not generation), but it
  established the methodology and political/ethical templates that later, generative
  cybercrime-tuned models (WormGPT, FraudGPT, WhiteRabbitNeo) implicitly follow: scrape the
  underground, train on it, gate the weights. The KAIST/S2W gating decision is itself a
  reference data-point for any researcher debating whether security-domain weights should be
  open. The paper also documents the ethical-review and legal scaffolding (IRB, takedown
  pipeline, no PII retention) that subsequent academic dark-corpus work tends to reuse.

LOCAL DIRECTORY CONTENTS
  paper.pdf   — Full ACL 2023 PDF, 10.4 MB, 13 pages.
  README.txt  — This file.
