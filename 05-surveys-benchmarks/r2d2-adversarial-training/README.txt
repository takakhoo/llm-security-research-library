Title:   R2D2 - Robust Refusal Dynamic Defense
         (adversarial-training defense, introduced in HarmBench)
Authors: Mantas Mazeika et al. (see HarmBench paper for full author list)
Venue:   ICML 2024 (Section 6 of the HarmBench paper)
arXiv:   https://arxiv.org/abs/2402.04249  (HarmBench)
GitHub:  https://github.com/centerforaisafety/HarmBench
         (code lives under code/adversarial_training/ inside HarmBench)

NOTE - this entry is a stub. R2D2 is not a separate paper or repo; it is
the adversarial-training defense proposed in Section 6 of the HarmBench
paper. For the actual PDF, training code, configs, and Zephyr-7B-Robust6B
checkpoints, see the sibling directory:

    ../harmbench-mazeika-2024/

In particular:
    ../harmbench-mazeika-2024/paper.pdf            <- full HarmBench paper (R2D2 is Sec. 6)
    ../harmbench-mazeika-2024/code/adversarial_training/  <- R2D2 training scripts
    ../harmbench-mazeika-2024/README.txt           <- our HarmBench summary

R2D2 in one paragraph:
R2D2 ("Robust Refusal Dynamic Defense") is an adversarial-training
procedure that periodically generates fresh GCG-style adversarial
suffixes against the in-training model and minimizes a combined refusal
+ utility loss on those examples. Applied to Zephyr-7B, it cuts the GCG
attack success rate from ~70% to single digits while preserving
MT-Bench score. The paper releases the resulting "Zephyr-7B-Robust" /
"Zephyr-R2D2" checkpoint and treats it as the strongest single defense
in the HarmBench leaderboard at release time.
