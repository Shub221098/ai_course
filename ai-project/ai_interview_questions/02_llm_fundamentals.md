# Section 2: LLM Fundamentals

> Comprehensive, clear, step-by-step answers for all 80 LLM Fundamentals questions.

---

### Q1: What are foundation models, and how have they changed AI engineering?
**Answer:** Foundation models are large neural networks trained on vast amounts of unlabelled data at scale (e.g. GPT-4, Llama 3, Claude). They changed AI engineering from building specialized task models from scratch to prompting, steering, and fine-tuning single general-purpose foundation models.

---

### Q2: What is a Large Language Model (LLM), and how does it work?
**Answer:** An LLM is a deep learning model (usually a Transformer) trained on massive text corpora to predict the next word or subword token in a sequence based on statistical patterns learned during pre-training.

---

### Q3: Inside ChatGPT: What Happens After You Hit Enter?
**Answer:**
1. **API Handling:** Request sent to server.
2. **Moderation/Safety:** Input checked for policy violations.
3. **Tokenization:** Text converted into token IDs.
4. **Context Construction:** User prompt merged with system prompt & history.
5. **Prefill:** Model computes Attention Keys & Values for all prompt tokens at once.
6. **Autoregressive Decoding:** Generates tokens one by one using sampling rules (Top-p, Temp).
7. **Streaming:** Tokens streamed back via Server-Sent Events (SSE).

---

### Q4: What is the Transformer architecture and how does it work?
**Answer:** The Transformer (Vaswani et al., 2017) uses self-attention mechanisms to process input sequences in parallel, allowing models to capture long-range token relationships much faster and better than sequential Recurrent Neural Networks (RNNs).

---

### Q5: What are the key components of the Transformer architecture?
**Answer:**
1. Token Embeddings
2. Positional Encodings (e.g., RoPE)
3. Multi-Head Self-Attention
4. Feed-Forward Networks (FFN / MLP)
5. Layer Normalization (Pre-Norm / RMSNorm)
6. Residual (Skip) Connections

---

### Q6: Walk me through one forward pass of a decoder-only Transformer.
**Answer:**
1. **Embedding:** Input token IDs $\to$ vectors $X$.
2. **Positional Encoding:** Adds position info via RoPE rotation.
3. **Self-Attention:** Computes $Q, K, V$. Applies causal mask (sets future scores to $-\infty$). Calculates $\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$.
4. **Feed-Forward Network:** Projects tokens through non-linear layers (SwiGLU).
5. **Residual + Norm:** Adds input $X$ back to block output and applies RMSNorm.
6. **LM Head:** Projects final hidden state to vocabulary dimension logits to select the next token.

---

### Q7: What is tokenization in LLMs?
**Answer:** Tokenization is the process of splitting raw text strings into discrete subword units (tokens) represented by integer IDs that the neural network can process.

---

### Q8: Explain BPE (Byte Pair Encoding).
**Answer:** BPE is a subword tokenization algorithm that starts with individual characters/bytes and iteratively merges the most frequently occurring adjacent pairs in the training corpus into single subword tokens.

---

### Q9: Explain WordPiece and SentencePiece.
**Answer:**
- **WordPiece:** Merges character pairs based on likelihood maximization (probability of pair divided by individual probabilities) rather than raw frequency.
- **SentencePiece:** Treats whitespace as a regular character (`_`), processing raw byte streams without requiring language-specific whitespace pre-tokenizers.

---

### Q10: What is positional encoding, and why is it needed in Transformers?
**Answer:** Since self-attention treats all tokens as an unordered set, positional encoding injects word-order information into token representations so the model knows word sequence positions.

---

### Q11: What are embeddings?
**Answer:** Embeddings are high-dimensional dense numerical vectors (e.g., 768 or 1536 dimensions) that map discrete items (like tokens or sentences) into continuous vector space, preserving semantic similarities.

---

### Q12: Explain Query(Q), Key(K), and Value(V) in attention.
**Answer:**
- **Query ($Q$):** What the current token is searching for.
- **Key ($K$):** What information each token in context contains.
- **Value ($V$):** The actual feature content passed along if Query and Key match.

---

### Q13: What is self-attention, and how does it work in Transformers?
**Answer:** Self-attention allows every token in a sequence to look at and assign relevance weights to every other token in the same sequence simultaneously.

---

### Q14: What is Cross Attention in Transformers?
**Answer:** Cross attention computes attention where Query ($Q$) comes from one sequence (e.g. Decoder) and Key ($K$) / Value ($V$) come from another sequence (e.g. Encoder). Used in translation and image-to-text models.

---

### Q15: Why do we scale the dot product attention by $\sqrt{d_k}$?
**Answer:** For large vector dimensions $d_k$, dot products $Q K^T$ grow large in magnitude, pushing the Softmax function into extreme regions with near-zero gradients. Division by $\sqrt{d_k}$ stabilizes variance to 1.

---

### Q16: What is causal masking?
**Answer:** Causal masking sets attention scores for future positions to $-\infty$ so that during training/inference, tokens can only attend to current and past tokens, preventing future lookahead.

---

### Q17: What are multi-head attention mechanisms? Why use multiple attention heads?
**Answer:** Multi-head attention splits Query, Key, and Value vectors into multiple sub-spaces ("heads"). This allows the model to attend to information from different representation sub-spaces at different positions simultaneously (e.g. one head tracks grammar, another tracks pronoun resolution).

---

### Q18: What are Feed-Forward Networks (FFN) in LLMs?
**Answer:** FFNs are non-linear neural layers applied independently to each token position after self-attention. They process and transform the features extracted by the attention heads.

---

### Q19: What is Generative AI?
**Answer:** Generative AI refers to deep learning models capable of generating new original content (text, images, audio, code, video) based on patterns learned from training data.

---

### Q20: What is the context window in LLMs, and why does it matter?
**Answer:** The context window is the maximum number of tokens an LLM can process in a single prompt + completion session. It determines how much text/code/history the model can read at once.

---

### Q21: Why is the context window limited in LLMs?
**Answer:** Because full self-attention scales quadratically $O(N^2)$ in compute and memory with sequence length $N$, and the KV cache memory scales linearly with sequence length and batch size.

---

### Q22: What is temperature in the context of LLMs, and how does it affect output?
**Answer:** Temperature ($T$) divides raw logits before softmax ($z / T$). Low $T$ ($<0.2$) makes outputs deterministic and strict. High $T$ ($>0.8$) flattens probabilities, making outputs diverse and creative.

---

### Q23: Why is the first token slower than the rest in an LLM?
**Answer:** The first token requires the **Prefill Phase**, where all input prompt tokens are processed concurrently through self-attention to populate the KV cache (compute-bound). Subsequent tokens only process a single token (decode phase).

---

### Q24: Explain Top-p (nucleus) sampling and Top-k sampling. How do they differ?
**Answer:**
- **Top-k:** Selects strictly from the top $K$ highest-probability tokens.
- **Top-p:** Selects dynamically from the smallest group of tokens whose cumulative probability reaches threshold $p$ (e.g., $p=0.9$).

---

### Q25: Compare greedy decoding, beam search, top-k, top-p, and temperature sampling. When does each fail?
**Answer:**
- **Greedy:** Picks highest probability token. (Fails: Repetitive, gets stuck in loops).
- **Beam Search:** Keeps top-$B$ sequences. (Fails: Slow, sounds robotic in open-ended text generation).
- **Top-k:** Fixed candidate pool. (Fails: Cuts off valid words in flat probability distributions).
- **Top-p:** Dynamic candidate pool based on cumulative probability. (Best for creative text).

---

### Q26: What are logits, and how are they used in text generation?
**Answer:** Logits are unnormalized raw prediction scores output by the final LM linear layer for every token in the vocabulary. Passing logits through Softmax converts them to probabilities.

---

### Q27: What are stop tokens in LLMs, and how does an LLM know when to stop generating?
**Answer:** Stop tokens are special tokens (e.g. `<|endoftext|>`, `</s>`) in the vocabulary. When the LLM outputs a stop token, the generation engine stops the autoregressive loop.

---

### Q28: What is the difference between a stop token and a stop sequence?
**Answer:**
- **Stop Token:** A specific token ID emitted natively by the model.
- **Stop Sequence:** A user-defined text string (e.g. `"User:"`) watched by the inference engine; generation halts when that string is matched in output.

---

### Q29: What are skip connections (residual connections) in Transformers?
**Answer:** Residual connections add the input of a layer directly to its output ($x + f(x)$). This allows gradients to flow unimpeded during backpropagation, preventing vanishing gradients in deep networks.

---

### Q30: What is the difference between open-source and closed-source LLMs?
**Answer:**
- **Open-source (Open Weights):** Weights can be downloaded and self-hosted (Llama 3, Mistral). High privacy, full control, but requires GPU infrastructure.
- **Closed-source:** Accessed via API (GPT-4, Claude). Zero infrastructure maintenance, state-of-the-art quality, but data privacy & vendor lock-in concerns.

---

### Q31: Encoder-only vs. Decoder-only vs. Encoder-Decoder Architectures.
**Answer:**
- **Encoder-only (BERT):** Bi-directional attention. Best for classification and embeddings.
- **Decoder-only (GPT-4, Llama):** Causal masked attention. Best for autoregressive generation & reasoning.
- **Encoder-Decoder (T5, Whisper):** Cross-attention connects encoder to decoder. Best for translation & speech-to-text.

---

### Q32: What is KV cache, and how does it speed up inference?
**Answer:** KV Cache saves past tokens' Key and Value attention vectors in GPU RAM during generation. Instead of recalculating past tokens ($O(N^2)$), the model only calculates $Q,K,V$ for the new single token ($O(N)$).

---

### Q33: Estimate KV cache memory needed for a large model.
**Answer:**
$$\text{KV Cache RAM} = 2 \times \text{layers} \times \text{heads} \times \text{head\_dim} \times \text{seq\_len} \times \text{batch\_size} \times \text{bytes\_per\_num}$$
For a 70B FP16 model with 8k context and batch size 16, KV cache can exceed 30+ GB of GPU VRAM.

---

### Q34: What is KV Cache Compression?
**Answer:** Techniques to reduce KV Cache RAM overhead, including Grouped-Query Attention (GQA), Quantized KV Cache (INT8/INT4 KV), and eviction strategies like StreamingLLM / Attention Sinks.

---

### Q35: What is model distillation, and how is it used with LLMs?
**Answer:** Knowledge distillation transfers knowledge from a large "Teacher" model (e.g., GPT-4) to a smaller "Student" model (e.g., 7B model) by training the student to match the teacher's output probabilities or reasoning traces.

---

### Q36: What is Mixture of Experts (MoE), and how does it work in models like Mixtral?
**Answer:** MoE replaces dense FFN layers with multiple "Expert" networks. A Router network routes each token to only 1-2 experts per layer, allowing a 47B parameter model to run at the speed of a 13B model.

---

### Q37: What is the difference between dense and sparse models?
**Answer:**
- **Dense:** Every parameter in the network is activated for every single token.
- **Sparse (MoE):** Only a small subset of parameters (experts) is activated for a given token.

---

### Q38: How does DeepSeek-V4 work?
**Answer:** DeepSeek models utilize Multi-Head Latent Attention (MLA) to compress KV Cache into low-dimensional latent vectors, combined with DeepSeekMoE architecture to activate fine-grained experts at ultra-low inference cost.

---

### Q39: What is FlashAttention?
**Answer:** FlashAttention is an exact attention algorithm that reorganizes GPU memory access, computing attention in small tiles inside fast GPU SRAM rather than reading/writing huge $N \times N$ matrices to slow GPU HBM.

---

### Q40: What is Cross-Entropy Loss?
**Answer:** Cross-Entropy Loss measures the difference between predicted token probability distribution and actual target token (one-hot vector). Formula: $\mathcal{L} = -\log P(y_{\text{true}})$.

---

### Q41: What is Grouped-Query Attention (GQA) vs Multi-Head Attention (MHA)?
**Answer:** In MHA, every Query head has its own Key and Value head. In GQA, multiple Query heads share a single Key/Value head group, reducing KV cache RAM size by 4x-8x while keeping performance high.

---

### Q42: How does Sliding Window Attention work?
**Answer:** Sliding Window Attention limits each token's attention to a fixed window of $W$ previous tokens (e.g. 4096 tokens) rather than full sequence length $N$, lowering attention memory from $O(N^2)$ to $O(N \times W)$.

---

### Q43: How do Attention Sinks work?
**Answer:** Research found that LLMs assign disproportionately high attention scores to the **very first 1-4 initial tokens** regardless of text. Keeping initial tokens always in KV cache ("Attention Sinks") prevents generation failure when sliding window attention evicts early tokens.

---

### Q44: How does Rotary Position Embedding (RoPE) work?
**Answer:** RoPE rotates Query and Key feature vectors in complex 2D planes by an angle proportional to token position. It naturally encodes relative distances between tokens and generalizes well to longer context lengths.

---

### Q45: Explain Layer Normalization.
**Answer:** Layer Normalization normalizes activations across feature dimensions for each individual sample in a batch, stabilizing gradient updates during deep network training.

---

### Q46: Explain RMSNorm (Root Mean Square Layer Normalization).
**Answer:** RMSNorm is a faster alternative to LayerNorm that scales activations by their root mean square without subtracting the mean, saving 10-50% computation per normalization layer.

---

### Q47: Why do modern Transformers use Pre-LayerNorm instead of Post-LayerNorm?
**Answer:** Pre-LayerNorm normalizes inputs *before* self-attention and FFN sub-layers (on the residual branch), providing stable gradient flow directly through skip connections without needing complex warmups.

---

### Q48: What are Chinchilla Scaling Laws?
**Answer:** Chinchilla scaling laws state that for compute-optimal training, model size and training data tokens should be scaled equally: for every 2x increase in compute, double both parameters and tokens (approx. 20 tokens per parameter).

---

### Q49: Your LLM keeps ignoring instructions. How do you make it follow structured output formats?
**Answer:** Use JSON Mode / Structured Outputs via constrained decoding (e.g. Pydantic / Instructor / Outlines grammars), provide clear system prompt schemas, and add few-shot examples.

---

### Q50: Your LLM-powered tool hits context window limits on long documents. How do you handle it?
**Answer:** Use RAG chunking, map-reduce / refine summarization strategies, context compaction / sliding windows, or switch to long-context models (e.g. Gemini 1.5 Pro).

---

### Q51: Your LLM does not admit when it does not know the answer. How do you fix it?
**Answer:** Add strict system instructions (`"Answer ONLY based on context. If unsure, respond 'I do not know'"`), lower Temperature to 0.0, and use RAG context grounding.

---

### Q52: Your LLM generates responses that are too verbose. How do you control length?
**Answer:** Use max token limits, specify exact length constraints in system prompt (`"Limit response to 2 sentences"`), or use stop sequences.

---

### Q53: Your LLM memorized proprietary training data and leaks it. How do you prevent this?
**Answer:** Apply post-generation output guardrails (regex / PII filters), fine-tune with differential privacy (DP-SGD), or unlearn sensitive data using targeted fine-tuning.

---

### Q54: Your LLM coding assistant generates outdated code. How do you fix it?
**Answer:** Use RAG to inject current documentation/API references into the context prompt, or fine-tune/system-prompt the model on current library versions.

---

### Q55: Your tokenizer splits domain terms into meaningless subword pieces. How do you fix it?
**Answer:** Add custom domain words to the tokenizer vocabulary and extend embedding weights, or train a custom tokenizer on domain data.

---

### Q56: Your Transformer's KV cache grows too large during long sequence generation. How do you manage memory?
**Answer:** Use PagedAttention (vLLM), GQA models, quantized KV Cache (INT8/INT4), and eviction windows (StreamingLLM).

---

### Q57: Your Transformer runs out of memory on long documents due to quadratic self-attention. How do you scale it?
**Answer:** Use FlashAttention-2/3, Sliding Window Attention, or linear attention architectures.

---

### Q58: Your distilled student model fails on complex reasoning. How do you close the gap?
**Answer:** Distill step-by-step reasoning traces (Chain-of-Thought) from teacher model rather than just final outputs, and use SFT + DPO fine-tuning.

---

### Q59: After RLHF alignment, your LLM lost capability on hard tasks. How do you manage alignment tax?
**Answer:** Mix pre-training data loss into RLHF objective (PPO with pre-training penalty) and use conservative KL-divergence penalties ($\beta$).

---

### Q60: Your RLHF model is gaming the reward model. How do you fix reward hacking?
**Answer:** Add KL-divergence penalty against baseline policy model, use ensemble reward models, and regularly update reward models with fresh adversarial data.

---

### Q61: Your chatbot loses context after 10 turns. How do you maintain long conversation context?
**Answer:** Implement sliding window chat history, automatic context compaction / conversation summarization, and vector-backed long-term memory.

---

### Q62: Your chatbot fails when users switch topics mid-conversation. How do you handle topic switches?
**Answer:** Use an intent classification agent step to detect topic switches, update session state, and prune irrelevant past context.

---

### Q63: Your QA system generates answers even when no answer exists in context. How do you detect unanswerable questions?
**Answer:** Train an NLI entailment classifier or query-context relevance evaluator to check if context contains the answer *before* generation.

---

### Q64: Your summarization system hallucinated facts not in original article. How do you fix it?
**Answer:** Lower temperature to 0.0, use factual consistency verification guardrails (e.g. FactCC / NLI model check), and enforce strict context-only system prompts.

---

### Q65: Your text generation repeats phrases in long outputs. How do you fix repetition?
**Answer:** Increase `presence_penalty` and `frequency_penalty` sampling parameters, avoid greedy decoding, and use N-gram repetition suppression.

---

### Q66: Transformers work on text, so can they also understand images?
**Answer:** Yes. Vision Transformers (ViT) split images into non-overlapping patches (e.g. 16x16 pixels), project patches to linear embeddings, and pass them through standard Transformer encoder layers.

---

### Q67: What are Small Language Models (SLMs)?
**Answer:** SLMs are lightweight models (1B-7B parameters) optimized for high efficiency, low latency, and edge/on-device deployment (e.g. Phi-3, Gemma 2B).

---

### Q68: What are Large Reasoning Models (LRMs)?
**Answer:** LRMs are models trained using RL (Reinforcement Learning) to output internal step-by-step reasoning tokens ("thinking process") before generating final answers (e.g. DeepSeek-R1, OpenAI o1).

---

### Q69: Explain Jev and System 1 vs System 2 Models.
**Answer:**
- **System 1:** Fast, intuitive, immediate next-token generation (standard LLMs).
- **System 2:** Slow, deliberate, logical reasoning and verification before responding (LRMs).

---

### Q70: What are Autoregressive Models?
**Answer:** Autoregressive models predict the next value in a sequence based on all previously generated values: $P(X) = \prod P(x_i | x_1, ..., x_{i-1})$.

---

### Q71: Explain the difference between autoregressive and masked language modeling.
**Answer:**
- **Autoregressive (GPT):** Left-to-right unidirectional context. Ideal for text generation.
- **Masked LM (BERT):** Bi-directional context predicting random hidden/masked tokens `[MASK]`. Ideal for embeddings and classification.

---

### Q72: What is Proximal Policy Optimization (PPO)?
**Answer:** PPO is an actor-critic reinforcement learning algorithm used in RLHF. It updates model policy parameters using a clipped surrogate objective function to prevent destructively large policy updates.

---

### Q73: What is Direct Preference Optimization (DPO)?
**Answer:** DPO simplifies RLHF by directly optimizing LLM parameters on preference data $(y_w, y_l)$ using implicit reward formulation, eliminating separate reward model training and PPO stability issues.

---

### Q74: What is Group Relative Policy Optimization (GRPO)?
**Answer:** GRPO samples a group of candidate outputs for a prompt, calculates relative rewards across the group using verifiable rule functions, and updates policy without needing a separate critic model (used in DeepSeek-R1).

---

### Q75: What are Recursive Language Models (RLMs)?
**Answer:** RLMs break complex queries into recursive sub-prompts, processing sub-tasks hierarchically before combining outputs into final responses.

---

### Q76: What is Continual Learning in LLMs?
**Answer:** Continual learning is the capability to update model weights incrementally with new knowledge without re-training from scratch or forgetting past knowledge.

---

### Q77: What is Recursive Self-Improvement (RSI)?
**Answer:** RSI is a process where an AI model generates data, evaluates its own reasoning, fine-tunes itself on verified high-quality outputs, and iteratively improves its capabilities autonomously.

---

### Q78: How do Diffusion Language Models (DLMs) work?
**Answer:** DLMs apply diffusion principles to discrete text: starting from random noise tokens, they iteratively unmask/refine tokens across multiple denoising steps to generate complete text non-autoregressively.

---

### Q79: How Does LLM Watermarking Work?
**Answer:** Watermarking modifies logit probabilities during sampling based on pseudo-random hash keys. It biases token selection toward a "Green List" of vocabulary tokens, allowing statistical detection of AI-generated text.

---

### Q80: How do RNNs and Transformers differ?
**Answer:**
- **RNN:** Processes text sequentially step-by-step ($O(N)$ sequential operations). Bottlenecks on long-range dependencies, hard to parallelize on GPUs.
- **Transformer:** Processes all tokens in parallel using self-attention ($O(1)$ sequential operations). Captures long-range dependencies easily and scales on GPUs.
