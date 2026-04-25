Title:   Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations
Authors: Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer,
         Yuning Mao, Michael Tontchev, Qing Hu, Brian Fuller, Davide Testuggine,
         Madian Khabsa  (Meta GenAI / Meta AI)
Venue:   Meta AI technical report (Dec 2023); released alongside Purple Llama
arXiv:   https://arxiv.org/abs/2312.06674
GitHub:  https://github.com/meta-llama/PurpleLlama

Summary:
Llama Guard is a fine-tuned Llama-2-7B classifier designed as an input/output
safeguard for human-AI chat. The authors define a "Llama Guard Safety Taxonomy"
covering six high-level harm categories (Violence & Hate, Sexual Content,
Guns & Illegal Weapons, Regulated/Controlled Substances, Self-Harm, Criminal
Planning) and provide explicit "should/should not" policy text inside the
prompt itself, so the same model can be re-purposed by editing the policy
without retraining. Training uses a small high-quality human-labeled dataset
(roughly 13.9K examples) covering both prompt-classification and
response-classification, and the model is exposed via an API that returns
"safe"/"unsafe" plus a violated-category list. Evaluation on internal data
plus public benchmarks (ToxicChat, OpenAI Moderation API eval) shows Llama
Guard outperforming the OpenAI Moderation API and competitive with much
larger models. The release is part of the broader Purple Llama umbrella,
which has since shipped Llama Guard 2/3/4, Prompt Guard, CyberSec benchmarks,
CodeShield, and the LlamaFirewall agentic-safety toolkit.

Repo structure (code/, monorepo - this paper covers the Llama-Guard/ subdir):
  Llama-Guard/                    - original Llama Guard 1 release (this paper)
  Llama-Guard2/, Llama-Guard3/,
    Llama-Guard4/                 - successor models with expanded taxonomy
  Prompt-Guard/, Llama-Prompt-
    Guard-2/                      - prompt-injection / jailbreak detection
  CybersecurityBenchmarks/        - CyberSecEval 1/2/3 benchmark code+data
  CodeShield/                     - inline insecure-code detector for codegen
  LlamaFirewall/                  - guardrail framework for agentic LLMs
  SensitiveDocClassification/     - data classifier for sensitive content
