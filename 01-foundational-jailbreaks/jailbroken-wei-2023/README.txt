Title: Jailbroken: How Does LLM Safety Training Fail?
Authors: Alexander Wei, Nika Haghtalab, Jacob Steinhardt
Venue: NeurIPS 2023
arXiv: https://arxiv.org/abs/2307.02483
GitHub: No official repository released.
        Searched arXiv abstract page (no Code link), gh search repos (no canonical
        unofficial reimplementation either; closest hits are unrelated red-team
        datasets). Many follow-up evaluation harnesses (HarmBench, JailbreakBench)
        re-use the taxonomy from this paper rather than reimplementing it directly.

Summary:
This paper presents the first principled taxonomy of why aligned LLMs (GPT-4 and
Claude v1.3) can be jailbroken, identifying two failure modes baked into safety
training: (1) competing objectives, where a model's instruction-following or
helpfulness objective is pitted against its safety objective (e.g., prefix injection,
refusal suppression, AIM/DAN-style role-play), and (2) mismatched generalization,
where the safety training distribution does not cover capabilities the base model
already has (e.g., Base64, ROT13, leetspeak, low-resource-language requests, payload
splitting). The authors hand-design 30+ jailbreaks, evaluate them on a curated harmful
behavior set, and show that no single defense suffices because the failure modes are
structural rather than adversarial-suffix artifacts. For cybersecurity
guardrail-bypass research, Jailbroken is the conceptual map of the attack surface:
nearly every later attack (CipherChat, MultiJail, Low-Resource, ReNeLLM, PAP) is an
instance of one of the two failure modes it names, making it the standard framing
paper that defenses must address at the level of training objectives, not just
filters.
