# Complete AI Engineering Interview Questions & Answers Guide

> **Prepared & Maintained by Outcome School / Amit Shekhar Repository Answers**
> Comprehensive, easy-to-understand answers for all 150+ questions covering LLMs, Prompt Engineering, RAG, AI Agents, Fine-Tuning, Vector Databases, System Design, LLMOps, Evaluation, AI Safety, Multimodal AI, Infrastructure, Coding, and Scenarios.

---

## 📚 Table of Contents & Study Guide Modules

| Module | Topics Covered | Link |
| :--- | :--- | :--- |
| **01. Must Know & LLM Fundamentals** | Core Definitions, Transformer Architecture, Forward Pass, Attention Q/K/V Math, Tokenization, RoPE Embeddings, KV Cache, Sampling (Top-k/Top-p/Temp), MoE, FlashAttention, SLMs/LRMs, Alignment (RLHF/DPO/GRPO). | [Read Module 01](./01_llm_fundamentals.md) |
| **02. Prompt Engineering & RAG** | Zero/Few-shot, CoT, ToT, ReAct, System Prompts, Prompt Injection, RAG Pipeline Architecture, Chunking Strategies, Contextual Retrieval, Hybrid Search (RRF), Re-ranking (Cross-Encoders/ColBERT), Agentic RAG, GraphRAG, Ragas Evaluation. | [Read Module 02](./02_prompt_engineering_and_rag.md) |
| **03. AI Agents & Fine-Tuning** | AI Agent Memory (Short/Long-term/Episodic), Harness Engineering, Claude Code Architecture, MCP Protocol, Multi-Agent Systems, Step Budgets, Fine-Tuning (Full vs LoRA vs QLoRA), GPU Memory Math, Catastrophic Forgetting, SFT vs Alignment. | [Read Module 03](./03_ai_agents_and_fine_tuning.md) |
| **04. Vector DBs, System Design & LLMOps** | Dense vs Sparse Embeddings, Cosine/Dot/Euclidean metrics, HNSW vs IVF indexing, Metadata filtering, Voice AI Agent Real-Time Design, Prefill vs Decode phases, vLLM Continuous Batching, PagedAttention, Serving Frameworks, Speculative Decoding. | [Read Module 04](./04_vector_dbs_system_design_llmops.md) |
| **05. Evaluation, Safety, Multimodal & Coding** | BLEU/ROUGE/BERTScore, LLM-as-a-Judge, SWE-bench limitations, Guardrails, LLM Watermarking, CLIP Contrastive Learning, Multimodal Fusion, PyTorch Causal Attention, Retry with Exponential Backoff, ReAct Agent in Python. | [Read Module 05](./05_evaluation_safety_multimodal_coding.md) |

---

## ⚡ Quick Key Takeaway Cheat Sheet

### 1. Transformer Attention Formula
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$

### 2. Reciprocal Rank Fusion (RRF) for Hybrid Search
$$\text{RRF Score}(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$

### 3. LoRA Weight Decomposition
$$W = W_0 + \Delta W = W_0 + \frac{\alpha}{r} (B \cdot A) \quad \text{where } A \in \mathbb{R}^{r \times k}, B \in \mathbb{R}^{d \times r}$$

### 4. GPU Memory Estimation for LLM Inference
$$\text{VRAM (FP16)} \approx \text{Parameters (in Billions)} \times 2\text{ GB} \times 1.25\text{ (Overhead)}$$
- **7B Model in FP16:** $\approx 14\text{ GB} + 4\text{ GB Overhead} = 18\text{ GB VRAM}$
- **7B Model in INT4:** $\approx 3.5\text{ GB} + 2.5\text{ GB Overhead} = 6\text{ GB VRAM}$

---

### 🌟 Usage Instructions
Navigate to any of the 5 modular markdown files above to read detailed, beginner-friendly explanations with equations, ASCII architecture diagrams, and Python code samples!
