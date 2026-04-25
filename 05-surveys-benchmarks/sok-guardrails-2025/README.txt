Title:   SoK: Evaluating Jailbreak Guardrails for Large Language Models
Authors: Xunguang Wang, Zhenlan Ji, Wenxuan Wang, Zongjie Li, Daoyuan Wu,
         Shuai Wang  (HKUST)
Venue:   arXiv preprint, June 2025 (Systematization-of-Knowledge style)
arXiv:   https://arxiv.org/abs/2506.10597
GitHub:  none cited in the paper

Summary:
This Systematization-of-Knowledge paper synthesizes the state of jailbreak
guardrails -- the post-deployment moderation layer that sits between the
user and the LLM -- and proposes a multi-dimensional taxonomy along six
axes: intervention stage (input vs. output vs. inline), detection
mechanism (rule-based, classifier-based, LLM-judge, retrieval-based),
adaptability, deployment locus, security guarantees, and evaluation
methodology. The authors comparatively analyze representative guardrails
including Llama Guard 1/2/3, NeMo Guardrails, ShieldGemma, AzureContent
Safety, GuardAgent, OpenAI Moderation, perplexity filters, SmoothLLM, and
RAIN. They synthesize attack-success-rate, false-positive-rate, latency,
and cost numbers across recent benchmarks (HarmBench, JailbreakBench,
AdvBench) to expose where each guardrail breaks. The paper concludes with
a checklist of evaluation pitfalls (over-fit benchmarks, leakage between
training-set and judge, single-turn-only assumptions) and a research
agenda for adaptive, agentic, and multi-turn-aware guardrails.

Repo structure (code/):
  (no repository)
