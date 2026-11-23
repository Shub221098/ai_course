# Section 13: AI Infrastructure and Scalability

> Comprehensive, clear answers for all 35 Infrastructure questions.

---

### Q1: How do you improve inference speed in production LLM deployments?
**Answer:** Use optimized serving engines (vLLM/SGLang), model quantization (AWQ/GPTQ INT4), PagedAttention, continuous batching, prompt caching, and speculative decoding.

---

### Q2: List top LLM optimization techniques.
**Answer:**
1. Quantization (FP16 $\to$ INT4)
2. PagedAttention & Continuous Batching
3. FlashAttention-2/3
4. Speculative Decoding
5. Prompt & Semantic Caching
6. Model Pruning & Distillation

---

### Q3: How do you select GPUs for LLM inference?
**Answer:** Calculate model size + KV cache VRAM. Pick based on GPU Memory Bandwidth (e.g., H100 = 3.35 TB/s vs A100 = 2.0 TB/s) and VRAM capacity (80GB vs 24GB).

---

### Q4: How does a GPU work for Deep Learning?
**Answer:** GPUs contain thousands of small parallel cores optimized for massive matrix multiplication (GEMM) operations, executing SIMD (Single Instruction Multiple Data) calculations.

---

### Q5: How do CUDA Kernels work?
**Answer:** CUDA kernels are C/C++ functions executed in parallel across thousands of GPU threads organized into blocks and grids.

---

### Q6: How does a Google TPU work?
**Answer:** Google TPUs use a Systolic Array architecture to stream data directly through matrix multiply units (MXUs) without writing intermediate results back to registers, achieving ultra-high matrix throughput.

---

### Q7: How does an LPU (Language Processing Unit - Groq) work?
**Answer:** LPUs use a deterministic Tensor Streaming Architecture with predictable SRAM chip routing, eliminating non-deterministic memory bus bottlenecks for extreme inference speed.

---

### Q8: Estimate GPU memory for a 70B model in FP16. Does it fit on an 80GB GPU?
**Answer:** Weights = $70\text{B} \times 2\text{ bytes} = 140\text{ GB}$. Plus KV cache and activations $\approx 160\text{ GB}$. **No**, it requires at least two 80GB GPUs (or 1 GPU if quantized to INT4).

---

### Q9: Roofline math for 70B model on one H100 GPU (batch size 1).
**Answer:** Memory bandwidth = 3.35 TB/s. Loading 140 GB weights per token takes $140 / 3350 \approx 0.0418\text{ seconds}$, yielding $\approx 24\text{ tokens/sec}$.

---

### Q10: Model Parallelism vs Data Parallelism.
**Answer:**
- **Data Parallelism:** Copies full model to each GPU, splitting dataset across GPUs.
- **Model Parallelism:** Splits model layers/weights across multiple GPUs when a model exceeds single-GPU VRAM.

---

### Q11: What is Tensor Parallelism?
**Answer:** Splitting weight matrices within individual linear layers across multiple GPUs (e.g. Megatron-LM), executing parallel matrix multiplies with All-Reduce communication.

---

### Q12: What is Pipeline Parallelism?
**Answer:** Partitioning different layers of a model sequentially across a chain of GPUs (GPU 1 = layers 1-8, GPU 2 = layers 9-16).

---

### Q13: How does continuous batching improve throughput?
**Answer:** Eliminates static batch padding by evicting completed requests and inserting new requests dynamically at every decoding step.

---

### Q14: What is speculative decoding?
**Answer:** Using a fast draft model to generate candidate tokens quickly, then validating all candidates in parallel using a single target model forward pass.

---

### Q15: How does Medusa work?
**Answer:** Attaches multiple speculative decoding heads to the base model itself, predicting multiple future tokens simultaneously without needing a separate draft model.

---

### Q16: How does EAGLE work?
**Answer:** Performs speculative decoding at the feature-vector layer rather than token-level, achieving higher acceptance rates for candidate tokens.

---

### Q17: What is N-gram Speculation?
**Answer:** Uses simple text N-gram matching on prompt context to guess future tokens rapidly without executing a neural draft model.

---

### Q18: Managing KV cache memory.
**Answer:** Allocate physical memory using PagedAttention, apply INT8/INT4 KV quantization, and evict stale tokens via sliding window attention.

---

### Q19: What is PagedAttention?
**Answer:** Allocates KV cache memory in non-contiguous physical blocks (paging), eliminating memory fragmentation.

---

### Q20: How does GGUF work?
**Answer:** GGUF is a single-file binary format used by `llama.cpp` storing model metadata, tensor weights, and quantization configs optimized for CPU/Metal loading.

---

### Q21: Optimizing inference for edge/mobile.
**Answer:** Quantize weights to 4-bit (GGUF/ExecuTorch), leverage mobile NPU hardware, and use small 1B-3B parameter models.

---

### Q22: Model quantization (INT8, INT4, FP16, BF16).
**Answer:**
- **FP16/BF16:** 2 bytes/param. Baseline quality.
- **INT8:** 1 byte/param. 50% memory reduction, minimal quality loss.
- **INT4:** 0.5 bytes/param. 75% memory reduction, slight accuracy tradeoff.

---

### Q23: Auto-scaling for AI workloads.
**Answer:** Scale GPU worker pods using Kubernetes HPA based on custom metrics: GPU Duty Cycle, Request Queue Length, and KV Cache Usage.

---

### Q24: Role of load balancing in AI serving.
**Answer:** Distributes incoming requests across GPU worker nodes based on real-time GPU VRAM availability and active batch counts.

---

### Q25: Managing GPU memory for serving multiple models.
**Answer:** Use dynamic model offloading to CPU RAM or share base model weights while hot-swapping LoRA adapters in GPU memory.

---

### Q26: What is model sharding?
**Answer:** Splitting model weight tensors across multiple GPU memory units (e.g. DeepSpeed ZeRO / PyTorch FSDP).

---

### Q27: Request queuing and priority scheduling.
**Answer:** Queue incoming requests in API gateway, prioritizing short queries or high-tier users over batch background jobs.

---

### Q28: Cost trade-offs: Self-Hosted vs API.
**Answer:**
- **API:** Zero upfront cost, pay-per-token. Best for low/variable traffic.
- **Self-Hosted:** Fixed GPU server cost. Best for high, predictable volume (millions of daily tokens).

---

### Q29: Handling cold start latency in serverless AI.
**Answer:** Keep warm instances, pre-download weights to local NVMe drives, and use lightweight quantized models.

---

### Q30: Model caching to reduce redundant compute.
**Answer:** Implement prompt caching (vLLM prefix caching) and semantic vector caching (Redis).

---

### Q31: Synchronous vs Asynchronous Inference.
**Answer:**
- **Synchronous:** Real-time chat (client waits for response).
- **Asynchronous:** Batch background document processing (job queues, Webhooks).

---

### Q32: FSDP vs DeepSpeed ZeRO.
**Answer:**
- **DeepSpeed ZeRO:** Partition optimizer states (ZeRO-1), gradients (ZeRO-2), and model parameters (ZeRO-3) across GPUs.
- **PyTorch FSDP:** PyTorch native implementation of parameter, gradient, and optimizer state sharding.

---

### Q33: TTFT, TPOT, and Throughput.
**Answer:**
- **TTFT (Time-To-First-Token):** Latency to start responding (prefill phase).
- **TPOT (Time-Per-Output-Token):** Time between subsequent tokens (decode phase).
- **Throughput:** Total tokens generated per second across all users.

---

### Q34: Monitoring & profiling LLM inference in production.
**Answer:** Instrument endpoints to track TTFT, TPOT, GPU VRAM usage, KV Cache hit rates, and Tensor Core utilization.

---

### Q35: Model routing at infrastructure level.
**Answer:** Route queries via an API proxy: simple queries $\to$ fast 8B model, complex queries $\to$ 70B+ model or reasoning LLM.
