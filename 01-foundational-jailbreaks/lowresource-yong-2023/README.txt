Title: Low-Resource Languages Jailbreak GPT-4
Authors: Zheng-Xin Yong, Cristina Menghini, Stephen H. Bach
Venue: NeurIPS 2023 SoLaR workshop
arXiv: https://arxiv.org/abs/2310.02446
GitHub: No official repository released. Searched arXiv abstract page and gh search
        repos with multiple queries; the closest unofficial work is
        https://github.com/LMY59/MnMR-GenA (a follow-up genetic-algorithm low-resource
        attack) but it is not a reimplementation of this paper. Defense / evaluation
        repos such as the AdvBench harness and HarmBench include low-resource-language
        evaluation that quotes this paper's translation methodology.

Summary:
This paper shows that GPT-4's safety alignment is brittle across the long tail of the
world's languages. The authors translate AdvBench harmful behaviors into 12 languages
spanning high-, mid-, and low-resource tiers (e.g., Zulu, Scots Gaelic, Hmong, Guarani)
and submit them directly to GPT-4 with no other jailbreak technique. Low-resource
languages alone elicit unsafe completions about 79% of the time on GPT-4, comparable to
state-of-the-art GCG / AIM jailbreaks, while high-resource languages elicit them less
than 1% of the time. The result is essentially a free, single-turn jailbreak that needs
nothing more than Google Translate. For cybersecurity guardrail-bypass research, this
paper is the cleanest demonstration of "mismatched generalization" in the wild: safety
training data is dominated by English (and a handful of other high-resource languages),
while the underlying multilingual capability of frontier models is much broader,
producing an enormous attack surface that any production safety filter must cover.
