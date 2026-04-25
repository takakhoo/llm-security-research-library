Title: Many-Shot Jailbreaking
Authors: Anthropic (Cem Anil, Esin Durmus, Mrinank Sharma, Joe Benton, Sandipan Kundu,
        Joshua Batson, et al.)
Venue: Anthropic technical report, April 2024 (later expanded in NeurIPS 2024)
PDF: https://www-cdn.anthropic.com/af5633c94ed2beb282f6a53c595eb437e8e7b630/Many_Shot_Jailbreaking__2024_04_02_0936.pdf
     (Not on arXiv at the time of release.)
GitHub: No official repository released.

Summary:
Many-Shot Jailbreaking (MSJ) exploits the long context window of frontier LLMs:
the attacker constructs a single user message containing dozens to hundreds of
fake assistant turns in which the model "answers" harmful questions, then ends with
the real harmful question. Once enough fake demonstrations are provided (often 32 to
256 shots), the model treats the harmful behavior as in-context-learned policy and
answers in kind, overriding RLHF safety training. The paper shows that the attack
success rate scales as a power law in the number of shots, that it transfers across
models (Claude 2.0, Claude 3 family, GPT-3.5, GPT-4, Llama-2, Mistral), and that
combining MSJ with other techniques (competing-objective preambles, language
switching) reduces the number of shots needed by an order of magnitude. The paper
proposes mitigations—context-aware classifiers and shot-count-based filtering—but
notes any context-window expansion reopens the attack. For cybersecurity
guardrail-bypass research, MSJ is the canonical long-context jailbreak and a
warning that context length is itself a safety-relevant capability axis: any
defense must hold not only at the per-message level but across the full attention
window, and benchmark evaluations need to include scaling with shot count.
