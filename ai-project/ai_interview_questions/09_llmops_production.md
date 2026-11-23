# Section 9: LLMOps and Production AI

> Comprehensive, clear answers for all 53 LLMOps & Production AI questions.

---

### Q1: How does Prompt Caching work?
**Answer:** Prompt Caching avoids recomputing Attention Keys and Values for static system prompt prefixes or large document context chunks. The serving engine caches KV vectors in GPU memory, dramatically cutting TTFT (Time-To-First-Token) and prefill cost.

---

### Q2: Prefill vs Decode.
**Answer:**
- **Prefill:** Computes KV cache for all prompt tokens in parallel (Compute-bound).
- **Decode:** Generates one token at a time sequentially (Memory bandwidth-bound).

---

### Q3: Why is prefill compute-bound and decode memory-bandwidth-bound?
**Answer:** Prefill processes $N \times N$ token matrices in parallel, maximizing GPU Tensor Core compute capacity. Decode loads all multi-gigabyte model weights & KV cache from GPU RAM to compute just a single new token vector, bottlenecking on memory transfer speed.

---

### Q4: What is chunked prefill, and why does it improve tail latency under mixed traffic?
**Answer:** Chunked prefill splits large input prefill requests into small chunks (e.g. 512 tokens) and piggybacks them alongside decode iterations, preventing long prompts from blocking quick token generation for other users.

---

### Q5: What is Prefill-Decode Disaggregation?
**Answer:** Separating GPU nodes into dedicated **Prefill Nodes** (optimized for compute) and **Decode Nodes** (optimized for memory bandwidth), transferring KV cache state across high-speed network interconnects (InfiniBand/RoCE).

---

### Q6: Explain the AI product lifecycle.
**Answer:** Problem Definition $\to$ Data Preparation/Prompting $\to$ RAG/Fine-Tuning $\to$ Evaluation Framework $\to$ LLMOps Infrastructure Deployment $\to$ Monitoring & Continuous Iteration.

---

### Q7: LLMOps vs MLOps.
**Answer:** MLOps focuses on model re-training pipelines, feature stores, and tabular metrics. LLMOps focuses on prompt versioning, context window management, vector DBs, LLM-as-a-judge evaluation, and token streaming.

---

### Q8: How do you serve LLMs in production?
**Answer:** Deploy high-throughput serving engines like vLLM, SGLang, or TensorRT-LLM with continuous batching, PagedAttention, and load balancers.

---

### Q9: What is model quantization?
**Answer:** Reducing parameter weight precision (e.g. FP16 $\to$ INT8/INT4) to cut GPU memory requirements and accelerate memory bandwidth.

---

### Q10: PTQ vs QAT. What breaks at 2-4 bits?
**Answer:**
- **PTQ (Post-Training Quantization):** Quantizes weights after training.
- **QAT (Quantization-Aware Training):** Simulates quantization during training.
- At 2-4 bits, extreme quantization causes severe perplexity degradation and loss of reasoning capabilities unless advanced techniques (GPTQ/AWQ) are used.

---

### Q11: How do you monitor LLM applications in production?
**Answer:** Track token usage, latency metrics (TTFT, TPOT, P99), cost per user, hallucination rates, and user feedback (thumbs up/down).

---

### Q12: What is LLM observability?
**Answer:** Tracing multi-step LLM calls, tool executions, and RAG retrieval steps end-to-end (using tools like LangSmith, Langfuse, Arize Phoenix).

---

### Q13: What are guardrails for LLMs, and how do you implement them?
**Answer:** Safety filters deployed at input and output boundaries to block prompt injection, toxic content, and PII leakage.

---

### Q14: How do you implement content filtering?
**Answer:** Run fast classification guardrails (Llama Guard / NeMo Guardrails) before and after model generation.

---

### Q15: How to estimate production AI costs?
**Answer:** $\text{Monthly Cost} = \text{Daily Requests} \times (\text{Input Tokens} \times \text{Input Price} + \text{Output Tokens} \times \text{Output Price}) \times 30$.

---

### Q16: How to optimize LLM inference costs?
**Answer:** Use model routing (8B for easy tasks, 70B for hard tasks), enable prompt caching, deploy semantic caching, and use quantized models.

---

### Q17: How to implement A/B testing for LLM systems?
**Answer:** Route user traffic dynamically between Model/Prompt A and B, measuring task completion rate, latency, and user satisfaction metrics.

---

### Q18: CI/CD for AI applications vs traditional CI/CD.
**Answer:** AI CI/CD includes prompt regression tests, automated eval benchmark suites, and hallucination scoring alongside standard unit tests.

---

### Q19: How to version and manage prompts in production?
**Answer:** Store prompts in versioned code repositories or prompt management registries (LangSmith / PromptLayer) decoupled from code logic.

---

### Q20: Model versioning and rollbacks.
**Answer:** Maintain versioned model IDs in config files and use blue/green canary deployments for zero-downtime rollbacks.

---

### Q21: How to implement rate limiting and throttling?
**Answer:** Deploy API gateways (Kong/Envoy) enforcing token-bucket rate limits per user/API key.

---

### Q22: Model updates without downtime.
**Answer:** Use canary releases: gradually shift traffic from v1 to v2 while monitoring latency and error metrics.

---

### Q23: Role of feature flags in AI deployments.
**Answer:** Dynamically toggle AI features, fallback models, or new prompt templates without re-deploying code.

---

### Q24: How to implement logging and tracing?
**Answer:** Instrument codebase with OpenTelemetry spans tracking input prompt, latency, token count, and tool execution outputs.

---

### Q25: How to handle PII in LLM inputs/outputs?
**Answer:** Run PII scrubbers (Microsoft Presidio) to detect and redact SSNs, emails, and names before passing text to LLMs.

---

### Q26: What is an LLM Gateway pattern?
**Answer:** A central proxy service that handles authentication, rate-limiting, cost tracking, PII scrubbing, and model routing across all LLM providers.

---

### Q27: How does Token Streaming work?
**Answer:** Uses HTTP Server-Sent Events (SSE) to push generated tokens to the client frontend as soon as each token is produced.

---

### Q28: How to implement streaming responses?
**Answer:** Use async generators in Python (FastAPI `StreamingResponse`) combined with LLM API streaming parameters.

---

### Q29: How does vLLM work?
**Answer:** High-performance serving engine featuring PagedAttention for KV cache management and iteration-level continuous batching.

---

### Q30: How does SGLang work?
**Answer:** Serving framework optimized for complex prompts and agent workflows using RadixAttention for fast prefix sharing.

---

### Q31: How does TensorRT-LLM work?
**Answer:** NVIDIA's C++ inference library compiling models into optimized TensorRT engines with tensor parallelism and FP8 support.

---

### Q32: How does llama.cpp run LLMs on everyday hardware?
**Answer:** Written in pure C/C++ with zero dependencies, optimizing quantized GGUF models for CPU AVX instructions and Apple Metal GPU.

---

### Q33: How does Ollama work?
**Answer:** Wraps `llama.cpp` into a developer-friendly CLI and REST API server for running open-source models locally.

---

### Q34: Choose vLLM vs SGLang vs TensorRT-LLM.
**Answer:**
- **vLLM:** General high-throughput Python serving.
- **SGLang:** Multi-call agent prompts.
- **TensorRT-LLM:** Maximum performance on NVIDIA enterprise GPUs.

---

### Q35: Key SLAs for production AI systems.
**Answer:** Time-To-First-Token (TTFT $<200\text{ms}$), Time-Per-Output-Token (TPOT $>30\text{ tokens/sec}$), System Availability ($99.9\%$), and Error Rate.

---

### Q36: Cloud vs On-Device Deployment.
**Answer:**
- **Cloud:** Unlimited compute, high quality, but continuous server costs and latency.
- **On-Device:** Zero API costs, low offline latency, privacy, but restricted by device RAM/battery.

---

### Q37: Fallback strategies when primary model fails.
**Answer:** Catch API error exceptions and automatically route request to secondary backup provider or local open-source instance.

---

### Q38: Reliably implementing structured output in production.
**Answer:** Use JSON Mode / Instructor grammars that enforce Pydantic schemas during model logits sampling.

---

### Q39: Efficiently handling long context in production.
**Answer:** Use prompt caching, context compaction, and document chunking.

---

### Q40: What is semantic routing?
**Answer:** Routing incoming user prompts to different specialized models based on semantic vector similarity to preset prompt categories.

---

### Q41: Managing secrets and API keys securely.
**Answer:** Store keys in secure vault services (AWS Secrets Manager / HashiCorp Vault) and inject via environment variables.

---

### Q42: Stabilizing LLM API latency spikes during peak hours.
**Answer:** Implement request queuing, auto-scale GPU instances, and use fallback model providers.

---

### Q43: Diagnosing p99 latency doubling after deploy.
**Answer:** Inspect trace logs: check if prompt context length increased, batching configuration changed, or prompt caching failed.

---

### Q44: Reducing LLM costs without degrading quality.
**Answer:** Use semantic caching, prompt caching, model routing (small models for simple tasks), and quantized open-source models.

---

### Q45: Handling provider rate limits during traffic spikes.
**Answer:** Implement client-side retries with exponential backoff + jitter and load-balance across multiple API keys/providers.

---

### Q46: Switching LLM providers without downtime.
**Answer:** Use a unified LLM Gateway API (LiteLLM / Portkey) that abstracts provider-specific API formats.

---

### Q47: Scaling AI system from 100 to 5000 requests/sec.
**Answer:** Deploy vLLM GPU clusters behind a load balancer with auto-scaling, request queuing, and prompt caching.

---

### Q48: Handling sudden traffic spikes.
**Answer:** Queue requests, enable continuous batching, and gracefully degrade by routing excess traffic to smaller models.

---

### Q49: Eliminating single points of failure in LLM pipelines.
**Answer:** Deploy multi-provider fallback routing (e.g. OpenAI $\to$ Anthropic $\to$ Self-Hosted vLLM).

---

### Q50: Handling multi-LLM orchestration failures.
**Answer:** Wrap each step in try-catch blocks with explicit fallback default values and step retry limits.

---

### Q51: Adding observability to zero-visibility AI pipelines.
**Answer:** Instrument pipeline steps with OpenTelemetry tracing tools (LangSmith / Phoenix).

---

### Q52: Minimizing quantization accuracy loss.
**Answer:** Use activation-aware quantization schemes (AWQ / GPTQ) instead of simple naive quantization.

---

### Q53: Designing graceful degradation.
**Answer:** If primary model/service fails, return cached responses, fallback to keyword search, or provide clear default messages.
