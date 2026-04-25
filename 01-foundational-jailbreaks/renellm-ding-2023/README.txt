Title: A Wolf in Sheep's Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily (ReNeLLM)
Authors: Peng Ding, Jun Kuang, Dan Ma, Xuezhi Cao, Yunsen Xian, Jiajun Chen, Shujian Huang
Venue: NAACL 2024
arXiv: https://arxiv.org/abs/2311.08268
GitHub: https://github.com/NJUNLP/ReNeLLM

Summary:
ReNeLLM is a fully automated jailbreak framework that produces what the authors call
nested jailbreak prompts. Stage 1 ("prompt rewriting") applies a sequence of LLM-based
rewrites to a harmful query—paraphrasing, sentence-pattern alteration, misspelling
sensitive words, partial translation—to confuse safety classifiers without changing
intent. Stage 2 ("scenario nesting") embeds the rewritten request inside one of three
benign-looking task templates: code completion, table filling, or text continuation.
The combination defeats GPT-3.5/4, Claude-1/2, and Llama-2-Chat with attack success
rates well above prior automated attacks while requiring only black-box API access and
1-2 orders of magnitude fewer queries than GCG. ReNeLLM also evaluates several existing
defenses (RA-LLM, SmoothLLM, OpenAI Moderation) and shows they degrade only marginally
against it. For cybersecurity guardrail-bypass research, ReNeLLM is the reference
template-nesting attack and a reminder that fluent, structurally-disguised payloads are
the dominant remaining failure mode for chat-API safety filters.

Repo structure (code/):
- LICENSE, README.md, requirements.txt
- renellm.py                                        end-to-end attack pipeline
- renellm_tcps.py                                   variant w/ time-cost / prompt-size
                                                    tracking
- get_responses.py                                  query target models
- check_gpt_asr.py / check_kw_asr.py                ASR with GPT judge / keyword judge
- defense/                                          baseline defense reimplementations
- llama/                                            Llama-2 inference helpers
- utils/                                            rewrite + nesting prompts
- data/                                             AdvBench harmful behaviors
- gpt-4_single_round_prompt_annotation.json        annotated single-round attacks
- image/
