---
license: other
tags:
- generated_from_trainer
- axolotl
base_model: Qwen/Qwen2-72B
datasets:
- cognitivecomputations/Dolphin-2.9
- teknium/OpenHermes-2.5
- m-a-p/CodeFeedback-Filtered-Instruction
- cognitivecomputations/dolphin-coder
- cognitivecomputations/samantha-data
- microsoft/orca-math-word-problems-200k
- Locutusque/function-calling-chatml
- internlm/Agent-FLAN
license_name: tongyi-qianwen
license_link: https://huggingface.co/Qwen/Qwen1.5-110B/blob/main/LICENSE
model-index:
- name: dolphin-2.9.2-qwen2-72b
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 40.38
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cognitivecomputations/dolphin-2.9.2-qwen2-72b
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 47.7
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cognitivecomputations/dolphin-2.9.2-qwen2-72b
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 21.37
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cognitivecomputations/dolphin-2.9.2-qwen2-72b
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 16.0
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cognitivecomputations/dolphin-2.9.2-qwen2-72b
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 17.04
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cognitivecomputations/dolphin-2.9.2-qwen2-72b
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 49.52
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cognitivecomputations/dolphin-2.9.2-qwen2-72b
      name: Open LLM Leaderboard
---

# Dolphin 2.9.2 Qwen2 72B 🐬

Curated and trained by Eric Hartford, Lucas Atkins, and Fernando Fernandes, and Cognitive Computations

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

Our appreciation for the sponsors of Dolphin 2.9.2:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 8xH100 node

This model is based on Qwen2-72b, and is governed by [tongyi-qianwen license](LICENSE)

The base model has 128k context, and the full-weight fine-tuning was with 8k sequence length.

This model was trained FFT on parameters selected by [Laser Scanner](https://github.com/cognitivecomputations/laserRMT/blob/main/laser_scanner.py), using ChatML prompt template format.

example:

```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Dolphin-2.9.2 has a variety of instruction, conversational, and coding skills. It also has initial agentic abilities and supports function calling.

Dolphin is uncensored. We have filtered the dataset to remove alignment and bias. This makes the model more compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. Please read my blog post about uncensored models. https://erichartford.com/uncensored-models You are responsible for any content you create using this model. Enjoy responsibly.

Dolphin is licensed according to Qwen's tongyi-qianwen license.  We grant permission for any use, including commercial, that falls within accordance with said license. Dolphin was trained on data generated from GPT4, among other models.

## Evals

![image/png](https://i.ibb.co/B4x1Ddr/file-2ao0fl-K2-B2-Hmka-Epd0ja-QY0x.webp)

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml
base_model: Qwen/Qwen2-72B
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer

trust_remote_code: true

# load_in_8bit: true
# load_in_4bit: false
# strict: false

datasets:
  - path: /workspace/datasets/dolphin-2.9.2/dolphin201-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/dolphin-coder-codegen-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/dolphin-coder-translate-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/m-a-p_Code-Feedback-sharegpt-unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/m-a-p_CodeFeedback-Filtered-Instruction-sharegpt-unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/not_samantha_norefusals.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/openhermes200k_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/Orca-Math-resort-unfiltered.jsonl
    type: sharegpt  
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/SystemChat_sharegpt.jsonl
    type: sharegpt  
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/toolbench_instruct_j1s1_3k_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/toolbench_negative_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/toolbench_react_10p_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/toolbench_tflan_cot_30p_unfiltered.jsonl
    type: sharegpt 
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.2/agent_instruct_react_unfiltered.jsonl
    type: sharegpt
    conversation: chatml

unfrozen_parameters:
- ^lm_head.weight$
- ^model.embed_tokens.weight$
# mlp.down_proj layers
- model.layers.62.mlp.down_proj
- model.layers.63.mlp.down_proj
- model.layers.66.mlp.down_proj
- model.layers.65.mlp.down_proj
- model.layers.64.mlp.down_proj
- model.layers.67.mlp.down_proj
- model.layers.68.mlp.down_proj
- model.layers.60.mlp.down_proj
- model.layers.31.mlp.down_proj
- model.layers.69.mlp.down_proj
- model.layers.61.mlp.down_proj
- model.layers.59.mlp.down_proj
- model.layers.70.mlp.down_proj
- model.layers.30.mlp.down_proj
- model.layers.76.mlp.down_proj
- model.layers.72.mlp.down_proj
- model.layers.77.mlp.down_proj
- model.layers.71.mlp.down_proj
- model.layers.29.mlp.down_proj
- model.layers.58.mlp.down_proj
- model.layers.75.mlp.down_proj
- model.layers.32.mlp.down_proj
- model.layers.56.mlp.down_proj
- model.layers.28.mlp.down_proj
- model.layers.26.mlp.down_proj
- model.layers.33.mlp.down_proj
- model.layers.34.mlp.down_proj
- model.layers.57.mlp.down_proj
- model.layers.27.mlp.down_proj
- model.layers.25.mlp.down_proj
- model.layers.35.mlp.down_proj
- model.layers.73.mlp.down_proj
- model.layers.24.mlp.down_proj
- model.layers.78.mlp.down_proj
- model.layers.74.mlp.down_proj
- model.layers.54.mlp.down_proj
# mlp.gate_proj layers
- model.layers.78.mlp.gate_proj
- model.layers.77.mlp.gate_proj
- model.layers.76.mlp.gate_proj
- model.layers.79.mlp.gate_proj
- model.layers.75.mlp.gate_proj
- model.layers.74.mlp.gate_proj
- model.layers.73.mlp.gate_proj
- model.layers.70.mlp.gate_proj
- model.layers.72.mlp.gate_proj
- model.layers.71.mlp.gate_proj
- model.layers.69.mlp.gate_proj
- model.layers.54.mlp.gate_proj
- model.layers.68.mlp.gate_proj
- model.layers.57.mlp.gate_proj
- model.layers.63.mlp.gate_proj
- model.layers.49.mlp.gate_proj
- model.layers.55.mlp.gate_proj
- model.layers.53.mlp.gate_proj
- model.layers.44.mlp.gate_proj
- model.layers.46.mlp.gate_proj
- model.layers.67.mlp.gate_proj
- model.layers.58.mlp.gate_proj
- model.layers.56.mlp.gate_proj
- model.layers.45.mlp.gate_proj
- model.layers.50.mlp.gate_proj
- model.layers.62.mlp.gate_proj
- model.layers.64.mlp.gate_proj
- model.layers.48.mlp.gate_proj
- model.layers.66.mlp.gate_proj
- model.layers.52.mlp.gate_proj
- model.layers.40.mlp.gate_proj
- model.layers.47.mlp.gate_proj
- model.layers.43.mlp.gate_proj
- model.layers.65.mlp.gate_proj
- model.layers.61.mlp.gate_proj
- model.layers.59.mlp.gate_proj
# mlp.up_proj layers
- model.layers.69.mlp.up_proj
- model.layers.70.mlp.up_proj
- model.layers.71.mlp.up_proj
- model.layers.68.mlp.up_proj
- model.layers.67.mlp.up_proj
- model.layers.66.mlp.up_proj
- model.layers.46.mlp.up_proj
- model.layers.63.mlp.up_proj
- model.layers.72.mlp.up_proj
- model.layers.64.mlp.up_proj
- model.layers.62.mlp.up_proj
- model.layers.45.mlp.up_proj
- model.layers.65.mlp.up_proj
- model.layers.73.mlp.up_proj
- model.layers.47.mlp.up_proj
- model.layers.44.mlp.up_proj
- model.layers.49.mlp.up_proj
- model.layers.48.mlp.up_proj
- model.layers.53.mlp.up_proj
- model.layers.74.mlp.up_proj
- model.layers.75.mlp.up_proj
- model.layers.57.mlp.up_proj
- model.layers.76.mlp.up_proj
- model.layers.43.mlp.up_proj
- model.layers.42.mlp.up_proj
- model.layers.61.mlp.up_proj
- model.layers.40.mlp.up_proj
- model.layers.56.mlp.up_proj
- model.layers.60.mlp.up_proj
- model.layers.31.mlp.up_proj
- model.layers.54.mlp.up_proj
- model.layers.55.mlp.up_proj
- model.layers.32.mlp.up_proj
- model.layers.41.mlp.up_proj
- model.layers.33.mlp.up_proj
- model.layers.58.mlp.up_proj
# self_attn.k_proj layers
- model.layers.79.self_attn.k_proj
- model.layers.36.self_attn.k_proj
- model.layers.35.self_attn.k_proj
- model.layers.74.self_attn.k_proj
- model.layers.34.self_attn.k_proj
- model.layers.78.self_attn.k_proj
- model.layers.77.self_attn.k_proj
- model.layers.37.self_attn.k_proj
- model.layers.39.self_attn.k_proj
- model.layers.41.self_attn.k_proj
- model.layers.38.self_attn.k_proj
- model.layers.33.self_attn.k_proj
- model.layers.69.self_attn.k_proj
- model.layers.42.self_attn.k_proj
- model.layers.32.self_attn.k_proj
- model.layers.25.self_attn.k_proj
- model.layers.70.self_attn.k_proj
- model.layers.22.self_attn.k_proj
- model.layers.63.self_attn.k_proj
- model.layers.29.self_attn.k_proj
- model.layers.68.self_attn.k_proj
- model.layers.24.self_attn.k_proj
- model.layers.30.self_attn.k_proj
- model.layers.66.self_attn.k_proj
- model.layers.31.self_attn.k_proj
- model.layers.23.self_attn.k_proj
- model.layers.65.self_attn.k_proj
- model.layers.57.self_attn.k_proj
- model.layers.28.self_attn.k_proj
- model.layers.64.self_attn.k_proj
- model.layers.44.self_attn.k_proj
- model.layers.27.self_attn.k_proj
- model.layers.75.self_attn.k_proj
- model.layers.40.self_attn.k_proj
- model.layers.26.self_attn.k_proj
- model.layers.61.self_attn.k_proj
# self_attn.o_proj layers
- model.layers.14.self_attn.o_proj
- model.layers.39.self_attn.o_proj
- model.layers.19.self_attn.o_proj
- model.layers.16.self_attn.o_proj
- model.layers.17.self_attn.o_proj
- model.layers.15.self_attn.o_proj
- model.layers.69.self_attn.o_proj
- model.layers.12.self_attn.o_proj
- model.layers.42.self_attn.o_proj
- model.layers.23.self_attn.o_proj
- model.layers.22.self_attn.o_proj
- model.layers.29.self_attn.o_proj
- model.layers.13.self_attn.o_proj
- model.layers.46.self_attn.o_proj
- model.layers.52.self_attn.o_proj
- model.layers.26.self_attn.o_proj
- model.layers.38.self_attn.o_proj
- model.layers.41.self_attn.o_proj
- model.layers.18.self_attn.o_proj
- model.layers.49.self_attn.o_proj
- model.layers.11.self_attn.o_proj
- model.layers.28.self_attn.o_proj
- model.layers.25.self_attn.o_proj
- model.layers.47.self_attn.o_proj
- model.layers.53.self_attn.o_proj
- model.layers.27.self_attn.o_proj
- model.layers.37.self_attn.o_proj
- model.layers.20.self_attn.o_proj
- model.layers.43.self_attn.o_proj
- model.layers.44.self_attn.o_proj
- model.layers.45.self_attn.o_proj
- model.layers.30.self_attn.o_proj
- model.layers.24.self_attn.o_proj
- model.layers.21.self_attn.o_proj
- model.layers.10.self_attn.o_proj
- model.layers.3.self_attn.o_proj
# self_attn.q_proj layers
- model.layers.1.self_attn.q_proj
- model.layers.2.self_attn.q_proj
- model.layers.3.self_attn.q_proj
- model.layers.5.self_attn.q_proj
- model.layers.4.self_attn.q_proj
- model.layers.0.self_attn.q_proj
- model.layers.6.self_attn.q_proj
- model.layers.8.self_attn.q_proj
- model.layers.7.self_attn.q_proj
- model.layers.9.self_attn.q_proj
- model.layers.10.self_attn.q_proj
- model.layers.12.self_attn.q_proj
- model.layers.19.self_attn.q_proj
- model.layers.18.self_attn.q_proj
- model.layers.25.self_attn.q_proj
- model.layers.11.self_attn.q_proj
- model.layers.15.self_attn.q_proj
- model.layers.61.self_attn.q_proj
- model.layers.17.self_attn.q_proj
- model.layers.55.self_attn.q_proj
- model.layers.54.self_attn.q_proj
- model.layers.16.self_attn.q_proj
- model.layers.68.self_attn.q_proj
- model.layers.49.self_attn.q_proj
- model.layers.48.self_attn.q_proj
- model.layers.52.self_attn.q_proj
- model.layers.13.self_attn.q_proj
- model.layers.42.self_attn.q_proj
- model.layers.57.self_attn.q_proj
- model.layers.60.self_attn.q_proj
- model.layers.53.self_attn.q_proj
- model.layers.64.self_attn.q_proj
- model.layers.66.self_attn.q_proj
- model.layers.62.self_attn.q_proj
- model.layers.59.self_attn.q_proj
- model.layers.50.self_attn.q_proj
# self_attn.v_proj layers
- model.layers.15.self_attn.v_proj
- model.layers.16.self_attn.v_proj
- model.layers.23.self_attn.v_proj
- model.layers.24.self_attn.v_proj
- model.layers.25.self_attn.v_proj
- model.layers.26.self_attn.v_proj
- model.layers.27.self_attn.v_proj
- model.layers.28.self_attn.v_proj
- model.layers.29.self_attn.v_proj
- model.layers.30.self_attn.v_proj
- model.layers.31.self_attn.v_proj
- model.layers.32.self_attn.v_proj
- model.layers.33.self_attn.v_proj
- model.layers.34.self_attn.v_proj
- model.layers.35.self_attn.v_proj
- model.layers.36.self_attn.v_proj
- model.layers.37.self_attn.v_proj
- model.layers.38.self_attn.v_proj
- model.layers.39.self_attn.v_proj
- model.layers.41.self_attn.v_proj
- model.layers.42.self_attn.v_proj
- model.layers.48.self_attn.v_proj
- model.layers.53.self_attn.v_proj
- model.layers.57.self_attn.v_proj
- model.layers.58.self_attn.v_proj
- model.layers.59.self_attn.v_proj
- model.layers.61.self_attn.v_proj
- model.layers.63.self_attn.v_proj
- model.layers.64.self_attn.v_proj
- model.layers.65.self_attn.v_proj
- model.layers.66.self_attn.v_proj
- model.layers.69.self_attn.v_proj
- model.layers.74.self_attn.v_proj
- model.layers.75.self_attn.v_proj
- model.layers.76.self_attn.v_proj
- model.layers.72.self_attn.v_proj

  
chat_template: chatml
dataset_prepared_path: qwen2-72b-data
val_set_size: 0.01
output_dir: qwen2-72b

sequence_len: 8192  # supports up to 8192
sample_packing: true
pad_to_sequence_len: true

# adapter: lora
# lora_model_dir:
# lora_r: 32
# lora_alpha: 16
# lora_dropout: 0.05
# lora_target_linear: true
# lora_fan_in_fan_out:

wandb_project: qwen2-72b
wandb_entity:
wandb_watch:
wandb_name:
wandb_log_model:

gradient_accumulation_steps: 8
micro_batch_size: 1
num_epochs: 3
optimizer: paged_adamw_8bit
lr_scheduler: cosine
learning_rate: 1e-5

train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32: false

gradient_checkpointing: true
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true

warmup_steps: 10
evals_per_epoch: 2
eval_table_size:
eval_max_new_tokens: 128
saves_per_epoch: 4
save_total_limit: 2
debug:
deepspeed: /workspace/axolotl/deepspeed_configs/zero3_bf16_cpuoffload_params.json
weight_decay: 0.05
fsdp:
fsdp_config:
special_tokens:
  pad_token: "<|endoftext|>"
  eos_token: "<|im_end|>"

```


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_cognitivecomputations__dolphin-2.9.2-qwen2-72b)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |32.00|
|IFEval (0-Shot)    |40.38|
|BBH (3-Shot)       |47.70|
|MATH Lvl 5 (4-Shot)|21.37|
|GPQA (0-shot)      |16.00|
|MuSR (0-shot)      |17.04|
|MMLU-PRO (5-shot)  |49.52|

