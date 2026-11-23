# Section 6: Fine-Tuning and Model Adaptation

> Comprehensive, clear answers for all 32 Fine-Tuning questions.

---

### Q1: What is fine-tuning, and when should you fine-tune an LLM?
**Answer:** Fine-tuning updates model weights on a specialized dataset. Use it when you need to teach specialized output formats, custom domain tone/jargon, or reduce latency/costs by adapting a smaller model.

---

### Q2: Compare full fine-tuning vs parameter-efficient fine-tuning (PEFT).
**Answer:**
- **Full Fine-Tuning:** Updates 100% of parameters. High VRAM requirement.
- **PEFT (LoRA):** Freezes base model and updates $<1\%$ parameters in adapter layers. Massive savings in VRAM and compute.

---

### Q3: What is LoRA (Low-Rank Adaptation), and how does it work?
**Answer:** LoRA freezes base weights $W_0$ and injects trainable rank-decomposition matrices $\Delta W = B \times A$ (where rank $r \ll d$). Reduces parameter updates by 99%.

---

### Q4: What is QLoRA, and how does it enable fine-tuning on consumer hardware?
**Answer:** QLoRA quantizes base model weights to 4-bit NormalFloat (NF4) and attaches 16-bit LoRA adapters, allowing fine-tuning of 70B models on a single GPU.

---

### Q5: How does fine-tuning work step-by-step?
**Answer:** Prepare dataset $\to$ Tokenize data $\to$ Load pre-trained model $\to$ Attach adapters/loss functions $\to$ Run forward pass & compute cross-entropy loss $\to$ Backpropagate & update weights.

---

### Q6: Prefix Tuning vs Prompt Tuning vs LoRA.
**Answer:**
- **Prompt Tuning:** Prepends trainable virtual prompt tokens to inputs.
- **Prefix Tuning:** Prepends trainable prefix keys/values to every attention layer.
- **LoRA:** Adds low-rank matrix pairs directly to weight matrices.

---

### Q7: What is adapter-based fine-tuning?
**Answer:** Adding small bottleneck neural network layers (adapters) between pre-trained Transformer layers while keeping base weights frozen.

---

### Q8: Pre-training vs Supervised Fine-Tuning (SFT) vs Preference Optimization (RLHF/DPO).
**Answer:**
- **Pre-training:** Predict next token on raw web data.
- **SFT:** Train on formatted instruction-response pairs.
- **Preference Optimization:** Align outputs with human preferences (helpful & harmless).

---

### Q9: What is RLHF (Reinforcement Learning from Human Feedback)?
**Answer:** RLHF trains a Reward Model on human preference pairs, then uses PPO to optimize the LLM policy toward high reward scores.

---

### Q10: What is Deep RL from Human Preferences?
**Answer:** The seminal 2017 paper (Christiano et al.) that introduced using pairwise feedback comparisons to learn reward functions for RL.

---

### Q11: Why did DPO displace PPO-based RLHF? When is online RL still better?
**Answer:** DPO replaces separate Reward Models & PPO with direct preference loss. Online RL (PPO/GRPO) is better when exploring new solution paths (e.g. reasoning/math).

---

### Q12: What is instruction tuning?
**Answer:** Fine-tuning a pre-trained base model on diverse task instructions so it acts as a conversational assistant rather than a text completer.

---

### Q13: How do you prepare a dataset for fine-tuning?
**Answer:** Format data into JSONL instruction pairs `{"input": ..., "output": ...}`, clean duplicates, remove poor examples, and split into train/eval sets.

---

### Q14: What is catastrophic forgetting, and how do you prevent it?
**Answer:** Catastrophic forgetting is losing general skills when fine-tuning on narrow tasks. Prevent by using LoRA, mixing general pre-training data into fine-tuning, and using low learning rates.

---

### Q15: When to choose Fine-Tuning vs RAG vs Prompt Engineering?
**Answer:**
- **Prompting:** Fast prototyping.
- **RAG:** Dynamic/private data retrieval.
- **Fine-Tuning:** Tone, style, format, and low latency.

---

### Q16: How do you evaluate a fine-tuned model's performance?
**Answer:** Run task accuracy benchmarks, evaluate loss on holdout sets, and run LLM-as-a-judge pairwise comparisons against the base model.

---

### Q17: What is synthetic data generation for fine-tuning?
**Answer:** Using a strong teacher model (GPT-4) to generate diverse training examples, which are filtered and used to fine-tune smaller models.

---

### Q18: Key hyperparameters for fine-tuning.
**Answer:** Learning rate ($10^{-4}$ to $10^{-5}$), batch size, epochs (1-3), LoRA rank $r$ (8-64), and LoRA $\alpha$ (16-32).

---

### Q19: GPU Memory Math for 7B Model in BF16, LoRA, and QLoRA.
**Answer:**
- **Full Fine-Tuning (BF16 + Adam):** 80-120 GB VRAM.
- **LoRA (BF16):** 16-24 GB VRAM.
- **QLoRA (4-bit):** 6-8 GB VRAM.

---

### Q20: How to fine-tune a model for specific domains (legal, medical)?
**Answer:** Run continual pre-training on domain text, followed by instruction tuning on specialized QA pairs.

---

### Q21: What is continual pre-training?
**Answer:** Unsupervised next-token training on domain-specific text before instruction tuning to teach specialized vocabulary.

---

### Q22: How do you merge multiple LoRA adapters?
**Answer:** Combine low-rank matrices using weighted summation: $W_{\text{final}} = W_0 + \sum w_i (B_i A_i)$.

---

### Q23: Difference between SFT and alignment training.
**Answer:** SFT teaches instruction following; alignment (RLHF/DPO) shapes safety, tone, and preference constraints.

---

### Q24: What is RLAIF (RL from AI Feedback)?
**Answer:** RLAIF uses an LLM (instead of humans) to label preference pairs for alignment training.

---

### Q25: What is Constitutional AI?
**Answer:** Anthropic's alignment method where models self-correct outputs according to a written set of principles (constitution).

---

### Q26: What is RLVR (Reinforcement Learning with Verifiable Rewards)?
**Answer:** RL alignment using deterministic rule-based checks (code execution / math correctness) as rewards rather than a subjective reward model.

---

### Q27: Knowledge distillation for fine-tuning and legal considerations.
**Answer:** Distillation uses teacher model outputs to train student models. Check model license terms (some commercial APIs restrict using outputs to train competing models).

---

### Q28: Your fine-tuned LLM produces factually wrong outputs. How to fix?
**Answer:** Clean training dataset errors, deduplicate noisy samples, or combine fine-tuning with RAG.

---

### Q29: Choose LoRA vs Full Fine-Tuning for domain assistant.
**Answer:** Choose LoRA: faster training, lower cost, minimal quality loss, and easily swap adapter weights.

---

### Q30: Your fine-tuned model memorized training data (overfitting). How to fix?
**Answer:** Reduce training epochs (1-2), add dropout, increase dataset size, and lower LoRA rank.

---

### Q31: Your fine-tuned model forgot general capabilities. How to fix?
**Answer:** Mix 10-20% general instruction data into fine-tuning set (Rehearsal) and use LoRA.

---

### Q32: Your RLHF preference data has low annotator agreement. How to ensure data quality?
**Answer:** Clarify annotation guidelines, train annotators, and filter out low-consensus pairs using inter-annotator agreement metrics (Fleiss' Kappa).
