Title: GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher (CipherChat)
Authors: Youliang Yuan, Wenxiang Jiao, Wenxuan Wang, Jen-tse Huang, Pinjia He, Shuming Shi, Zhaopeng Tu
Venue: ICLR 2024
arXiv: https://arxiv.org/abs/2308.06463
GitHub: https://github.com/RobustNLP/CipherChat

Summary:
CipherChat shows that simply encoding harmful conversation in a non-natural-language
cipher (Caesar, ASCII, Morse, SelfCipher, Unicode, Base64, etc.) bypasses safety
training for capable models—because RLHF safety data is overwhelmingly written in plain
natural language. The authors prompt the target model with a short system message that
defines the cipher, give a few in-context examples in cipher, then issue the harmful
request in cipher and decode the response. SelfCipher, where GPT-4 invents a cipher on
the fly, is particularly effective and reaches near-100% attack success rate on the
hardest categories. The technique is a clean instance of "mismatched generalization"
from Wei et al.: capability transfers to ciphered inputs while safety training does
not. For cybersecurity guardrail-bypass research, CipherChat is the canonical
encoding-based attack and a standard baseline for evaluating whether a safety filter
generalizes beyond plaintext—any defense restricted to natural-language token detection
will fail against it.

Repo structure (code/):
- LICENSE, README.md
- main.py                          entry point running cipher attacks across models
- encode_experts.py                Caesar / ASCII / Morse / SelfCipher / Unicode encoders
- prompts_and_demonstrations.py    cipher system prompts and few-shot examples
- utils.py
- data/                            unsafe instruction dataset by category
- experimental_results/, saved_results/, log/
- paper/                           paper-related figures
