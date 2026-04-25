Title: Improving Alignment and Robustness with Circuit Breakers
Authors: Andy Zou, Long Phan, Justin Wang, Derek Duenas, Maxwell Lin, Maksym Andriushchenko, Rowan Wang, Zico Kolter, Matt Fredrikson, Dan Hendrycks
Venue: NeurIPS 2024 (also arXiv:2406.04313)
Link: https://arxiv.org/abs/2406.04313
GitHub: https://github.com/GraySwanAI/circuit-breakers

Summary:
Circuit Breakers is a representation-engineering defense that fine-tunes an LLM (or VLM, or agent) so that internal activations associated with harmful generation paths get re-routed to refusal-like states, "breaking the circuit" mid-forward-pass instead of relying on output filtering or refusal-trained surface behavior. The training objective combines a Representation Rerouting (RR) loss on a curated harmful set with a retain loss on benign prompts, so harmful-trajectory hidden states are pushed away from their natural manifold while benign capability is preserved. Empirically the method holds up against strong white-box attacks (GCG, AutoDAN, PAIR, prefilling) on Llama-3-8B and Mistral-7B, against multimodal image-PGD on LLaVA, and reduces harmful agent actions in tool-use settings — all with negligible drops on MMLU/MT-Bench. Because the defense is intrinsic to the weights, it composes with output-side guardrails (classifiers, filters) and does not require an external moderation model at inference. Defenders use the released training code and configs (in code/) to harden their own open-weights models without RLHF-scale data, and use the evaluation harness to A/B against jailbreak suites.
