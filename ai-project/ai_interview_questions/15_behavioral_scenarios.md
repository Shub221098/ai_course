# Section 15: Behavioral and Scenario-Based Questions

> Comprehensive, clear answers for all 22 Behavioral & Scenario questions.

---

### Q1: What is AI Engineering vs Machine Learning Engineering?
**Answer:**
- **ML Engineering:** Trains custom models from scratch, builds feature stores, optimizes model weights, and manages classical ML pipelines (PyTorch/Scikit-Learn).
- **AI Engineering:** Builds applications around pre-trained foundation models using prompt engineering, RAG, tool calling, AI agents, vector DBs, and LLMOps.

---

### Q2: How do you decide whether a problem needs AI or traditional software?
**Answer:** Use traditional software if rules are deterministic, 100% precision is required, and logic is fixed (e.g. tax calculation). Use AI if inputs/outputs are unstructured (text, audio, vision), rules are complex/probabilistic, or open-ended reasoning is required.

---

### Q3: How do you measure the ROI of an AI feature?
**Answer:** Measure net business value: $(\text{Cost Savings from Automation} + \text{New Revenue Generated}) - (\text{LLM API / Infrastructure Costs} + \text{Engineering Maintenance})$.

---

### Q4: How do you handle hallucinations when they occur in production AI?
**Answer:**
1. Immediate: Set temperature `0.0`, enforce strict context grounding prompt instructions.
2. Architecture: Implement RAG with Cross-Encoder re-ranking.
3. Observability: Deploy NLI entailment guardrails to block hallucinated responses before user delivery.

---

### Q5: How to decide between LLM API vs Self-Hosting Open-Source?
**Answer:**
- **API (OpenAI/Claude):** Fast launch, zero GPU maintenance, state-of-the-art capability. Best for low/variable traffic.
- **Self-Hosted (vLLM/Llama 3):** Complete data privacy/GDPR compliance, full control, and lower cost at massive scale (millions of daily requests).

---

### Q6: How do you manage stakeholder expectations for AI projects?
**Answer:** Emphasize that LLMs are probabilistic (not 100% deterministic), set realistic accuracy SLAs, establish quantitative benchmark evaluation datasets early, and communicate failure edge cases.

---

### Q7: Describe your approach to debugging a poor-performing RAG system.
**Answer:** Decouple and evaluate components separately:
1. **Eval Retrieval:** Measure Context Precision & Recall. Are right chunks fetched?
2. **Eval Generation:** Measure Faithfulness & Answer Relevance. Is LLM ignoring fetched context?

---

### Q8: How do you stay current with the rapidly evolving AI landscape?
**Answer:** Read research papers (arXiv), follow leading AI labs (OpenAI, Anthropic, DeepSeek), follow active AI engineers on Twitter/GitHub, and test new tools hands-on.

---

### Q9: How do you balance innovation with reliability in AI systems?
**Answer:** Keep production pipelines simple and reliable (clean RAG/prompts with guardrails), while isolating experimental features (agents/fine-tuning) behind feature flags tested against golden eval sets.

---

### Q10: Tell me about a challenging AI project you worked on.
**Answer:** *(STAR Method)*
- **Situation:** Enterprise search was returning irrelevant answers from 1M+ PDF documents.
- **Task:** Improve retrieval accuracy while keeping latency under 1 second.
- **Action:** Switched from pure vector search to Hybrid Search (Vector + BM25) with Reciprocal Rank Fusion and added a Cross-Encoder re-ranker.
- **Result:** Retrieval recall increased by 42% while p95 latency stayed at 650ms.

---

### Q11: How to handle an AI model producing biased or harmful outputs in production?
**Answer:** Activate automated output safety guardrails to block toxic responses, log incident details, patch system prompts/input filters, and run a blameless post-mortem.

---

### Q12: How to approach cost optimization for an AI system exceeding budget?
**Answer:** Implement prompt caching, introduce semantic vector caching for common queries, deploy model routing (8B for simple tasks, 70B for hard tasks), and trim prompt token context sizes.

---

### Q13: Time you chose between model accuracy and latency. How did you decide?
**Answer:** For real-time chat, latency is critical (TTFT $<300\text{ms}$). Selected an 8B quantized model with vLLM continuous batching over a slower 70B model, achieving 92% of target accuracy at 5x faster speed.

---

### Q14: How to handle quality degradation over time?
**Answer:** Monitor production metrics (user feedback, drift in query distribution), collect failing production traces, update golden eval datasets, and refine prompt/RAG chunks.

---

### Q15: How to communicate AI limitations to non-technical stakeholders?
**Answer:** Use clear analogies (e.g. "LLMs are like brilliant interns with photographic memory who sometimes make confident guesses"), frame performance in probabilistic metrics, and highlight guardrail safety measures.

---

### Q16: Building an AI feature with limited labeled data.
**Answer:** Use zero-shot / few-shot prompting with strong foundation models, generate synthetic training data using GPT-4, and apply active learning to label critical failure cases.

---

### Q17: Experience working with cross-functional teams on AI projects.
**Answer:** Collaborate with Product Managers (defining SLAs & eval rubrics), UX Designers (designing streaming interfaces & disclaimers), and Security Teams (enforcing PII scrubbing & guardrails).

---

### Q18: Where do you see AI engineering heading in 3-5 years?
**Answer:** Shift toward autonomous multi-agent systems, native multimodal processing, standardized tool protocols (MCP), specialized Small Language Models running on-device, and reasoning models (System 2 thinking).

---

### Q19: Why are you interested in this AI engineering role?
**Answer:** Passionate about solving complex real-world challenges by combining robust engineering systems (RAG, Agents, LLMOps) with cutting-edge foundation models to deliver measurable user impact.

---

### Q20: PM wants to ship an AI feature with 15% hallucination rate. How to communicate risk?
**Answer:** Quantify risk impact: "15 out of 100 users will receive incorrect information, potentially damaging user trust or causing liability." Propose shipping with HITL (Human-in-the-Loop) or restricted beta until guardrails lower hallucination below target SLA.

---

### Q21: Executive asks why AI cannot be 100% accurate. How to explain?
**Answer:** Explain that LLMs predict probabilities over words based on training patterns rather than executing deterministic code logic. Show how guardrails and RAG minimize errors while acknowledging inherent statistical bounds.

---

### Q22: Choose complex agentic system (+15% benchmark score) vs simpler RAG pipeline (easier maintenance). Decide?
**Answer:** Choose simpler RAG pipeline initially if maintenance overhead and token costs of the complex agent are high. Upgrade to agentic system incrementally only if the +15% accuracy gain directly drives critical business value.
