# Section 8: AI System Design

> Comprehensive architecture designs and answers for all 49 System Design questions.

---

### Q1: Design a Real-Time Voice AI Agent.
**Answer:** Microservices pipeline connected via WebSockets: `Microphone -> VAD (Voice Activity Detection) -> Whisper ASR -> Fast LLM (vLLM Llama 3) -> ElevenLabs TTS -> Speaker`. Requires sub-600ms latency and WebSocket barge-in cancellation.

---

### Q2: Design ChatGPT: Training to Serving.
**Answer:**
1. **Training:** Web crawl data -> Tokenization -> Self-supervised Pre-training -> SFT (Instruction Tuning) -> RLHF/DPO Alignment.
2. **Serving:** Load balancer -> API Gateway -> Input Safety Guardrails -> vLLM Inference Cluster (PagedAttention + Continuous Batching) -> SSE Streaming output.

---

### Q3: Design a RAG System (Chat with Your Documents).
**Answer:** Document Ingestion Pipeline (PDF Parsing -> Chunker -> Embedding Service -> Vector DB), and Query Execution Pipeline (User Query -> Vector Search + BM25 -> Reranker -> Context Injection -> LLM Generator).

---

### Q4: Design an Enterprise RAG Assistant (10M Docs with RBAC).
**Answer:** Document ingestion syncs LDAP/Active Directory permissions into vector metadata (`user_groups`). Search query pre-filters vectors by current user's authenticated permission tags.

---

### Q5: Design Memory for a Personal AI Assistant.
**Answer:** Short-term memory (sliding window prompt context), Long-term memory (Vector DB of past user facts), and Episodic memory (Key-Value store of user preferences & settings).

---

### Q6: Design a Deep Research Agent.
**Answer:** Plan-and-Execute loop: Query -> Sub-query Planner -> Parallel Web Search & Scraping -> Document Evaluator -> Iterative Synthesis -> Final Markdown Report Compiler.

---

### Q7: Design a Multi-Agent Customer Support System.
**Answer:** Router Agent routes user input to specialized sub-agents (Billing Agent, Tech Support Agent, Order Tracking Agent). Supervisor Agent handles session state and human escalation logic.

---

### Q8: Design an On-Device AI Assistant.
**Answer:** Run quantized Small Language Model (Llama 3.2 1B / Phi-3) locally on Apple Neural Engine / Android NPU using `llama.cpp` or ExecuTorch. Local SQLite vector storage for privacy.

---

### Q9: Design a Multimodal Search System (Text, Image, Video).
**Answer:** Use CLIP/EVA-CLIP to embed text, images, and video keyframes into a shared vector space stored in Qdrant. Fast cross-modal cosine similarity retrieval.

---

### Q10: Design an LLM Inference Platform (vLLM-as-a-Service).
**Answer:** API Gateway -> Distributed Request Queue -> Autoscaling GPU Nodes running vLLM with PagedAttention -> Model Weight Cache Store (S3/NVMe) -> Prometheus Metrics.

---

### Q11: Design an LLM Evaluation Platform.
**Answer:** Dataset Repository -> Test Execution Scheduler -> LLM API Runner -> Evaluation Engine (LLM-as-a-judge + Ragas + BLEU/ROUGE) -> Metric Dashboard.

---

### Q12: Design a Text-to-Image Service (Midjourney-like).
**Answer:** Prompt Parser/LLM Expansion -> Text Encoder (CLIP/T5) -> Latent Diffusion Model (UNet/DiT) GPU Pipeline -> VAE Decoder -> Image Storage CDN.

---

### Q13: Design a Music Generation Service (Suno-like).
**Answer:** Lyrics Generator LLM -> Audio Tokenizer (EnCodec) -> Transformer Audio Diffusion Engine -> Neural Vocoder -> Audio Stream Output.

---

### Q14: Design a Video Generation Service (Sora-like).
**Answer:** Text Embedding -> 3D Spatiotemporal Diffusion Transformer (DiT) operating on latent video patches -> Video VAE Decoder -> Distributed GPU Rendering Pipeline.

---

### Q15: Design an AI Coding Agent (Cursor / Claude Code).
**Answer:** IDE Extension -> Repository Indexer (AST + Tree-Sitter + Vector Search) -> Context Builder -> LLM Code Engine -> Diff Generation & Syntax Verification Engine.

---

### Q16: Design a Code Generation and Review System.
**Answer:** Webhook on GitHub PR -> Diff Parser -> AST Analysis -> Multi-Agent Reviewer (Security, Style, Logic) -> Automated Line Comments posted via GitHub API.

---

### Q17: Design a Content Moderation System using AI.
**Answer:** Input Stream -> Fast Rules/Regex Filter -> Lightweight Classifier (BERT) -> Multimodal Safety Guardrail -> Human Moderator Queue for edge cases.

---

### Q18: Design a Real-Time AI Recommendation System.
**Answer:** Event Collector -> Real-Time Feature Store (Feast) -> Two-Stage Architecture: Retrieval Candidate Generation (Vector ANN) -> Ranking (Deep Learning Re-ranker).

---

### Q19: Design an AI-Powered Email Assistant.
**Answer:** Email Parser -> Classification Agent (Spam, Urgent, Action Required) -> RAG Context Fetcher -> Draft Response Generator -> Human Approval UI.

---

### Q20: Design a Medical Diagnosis Assistant using AI.
**Answer:** Medical Record Parser -> Symptom Extractor -> Clinical Knowledge Base RAG -> Differential Diagnosis Engine -> Mandatory Physician Review Interface.

---

### Q21: Design a Fraud Detection System Powered by LLMs.
**Answer:** Transaction Stream -> Rule Engine -> GNN/XGBoost Anomaly Detector -> LLM Explanation Generator (summarizes suspicious behavior for fraud analysts).

---

### Q22: Design an AI Data Extraction Pipeline from Unstructured Documents.
**Answer:** Layout-Aware PDF Parser (LlamaParse) -> Chunking -> LLM Schema Extraction via Pydantic/Instructor -> DB Validation & Storage.

---

### Q23: Design a Text-to-SQL System Over a Data Warehouse (Thousands of Tables).
**Answer:** Schema Filter (RAG retrieves relevant table definitions using table metadata) -> Text-to-SQL LLM Generator -> SQL Parser & Validator -> Read-Only Execution Engine.

---

### Q24: Design a Personalized Learning Assistant.
**Answer:** Student Knowledge State Graph -> Adaptive Quiz Engine -> Concept RAG Explanation Generator -> Performance Analytics Dashboard.

---

### Q25: Design an AI System for Automated Code Migration.
**Answer:** Source Code Parser -> Dependency Graph Builder -> Batch Migration Agent (translates modules) -> Automated Unit Test Execution & Iterative Repair Loop.

---

### Q26: Design an AI Legal Document Review System.
**Answer:** Contract Parser -> Clause Extraction -> Legal RAG (matches clauses against corporate playbook) -> Redlining Agent (suggests edits).

---

### Q27: Design a Conversational AI System with Session Memory.
**Answer:** Chat Gateway -> Redis Active Context Store -> Background Summarization Worker -> Long-Term Vector Store.

---

### Q28: How do you design for latency vs quality trade-offs?
**Answer:** Use multi-tier model routing: route fast queries to 8B models (low latency) and complex reasoning to 70B+ models or reasoning LLMs.

---

### Q29: How do you implement caching strategies for LLM apps?
**Answer:** Prompt Caching at model engine level (prefill optimization) and Semantic Caching at API level (Redis + Vector DB).

---

### Q30: How do you design rate limiting and cost management?
**Answer:** Token-bucket rate limiter per user API key, budget quotas per billing cycle, and dynamic model routing.

---

### Q31: How do you handle failover and fallback strategies?
**Answer:** Primary LLM API failure triggers automatic fallback to secondary provider (e.g. OpenAI -> Anthropic) or local open-source model endpoint.

---

### Q32: How to design AI systems for high availability?
**Answer:** Multi-region load balancing, stateless model serving nodes, automatic node health checks, and fallback degradation models.

---

### Q33: Graceful degradation when model is unavailable.
**Answer:** Return pre-computed responses, fallback to keyword search/rules, or switch to lightweight local model.

---

### Q34: Multi-region deployment considerations.
**Answer:** Data residency regulations (GDPR), regional GPU availability, API latency, and global database replication.

---

### Q35: Design an E-Commerce AI Search Engine.
**Answer:** User Query -> Hybrid Search (Vector product embeddings + BM25 keyword match) -> Personalization Re-ranker -> Stock/Price Filter -> Search Results.

---

### Q36: Design an AI Gateway for an Organization.
**Answer:** Central Proxy -> API Key Authentication -> Cost/Usage Tracking -> Guardrails & PII Scrubbing -> LLM Provider Load Balancer.

---

### Q37: How to design RAG handling conflicting information across sources?
**Answer:** Inject source authority scores and timestamps in context, instructing LLM to explicitly highlight contradictions and prioritize newer sources.

---

### Q38: Capacity planning for an AI system.
**Answer:** Estimate peak RPM (Requests Per Min), average tokens per request, model VRAM size, and required GPU instances ($N_{\text{GPUs}} = \text{Peak Tokens/sec} / \text{Throughput per GPU}$).

---

### Q39: Design a Multi-Tenant Chatbot Platform.
**Answer:** Isolated tenant metadata storage, tenant-specific vector namespaces, customizable system prompt configurations, and strict RBAC.

---

### Q40: Design an AI Meeting Summarizer (Thousands Daily).
**Answer:** Audio Stream -> Async Chunked Speech-to-Text Queue -> Map-Reduce Summarization Pipeline -> Action Item Extractor -> Email Integrator.

---

### Q41: Design an AI Notification System that Prioritizes.
**Answer:** Incoming Alert Stream -> Priority Scoring Model -> User Context Filter -> High-priority immediate push vs low-priority daily digest queue.

---

### Q42: Design an Anomaly Detection System for Cloud Infrastructure.
**Answer:** Metric/Log Stream -> Time-Series Anomaly Detector -> LLM Root Cause Analysis Generator -> Slack/PagerDuty Alerting.

---

### Q43: Design a Document Processing Pipeline for Financial Institutions.
**Answer:** OCR/Layout Parser -> PII Redactor -> Table Extractor -> Compliance Guardrail -> Audit Logging DB.

---

### Q44: Design an AI Dynamic Pricing Engine.
**Answer:** Demand/Competitor Data Stream -> Feature Store -> Price Elasticity Model -> Business Constraint Validator -> Price Update API.

---

### Q45: Design an AI Resume Screening System (100K Applications/Week).
**Answer:** Resume Parser -> Anonymizer (strips demographic info to prevent bias) -> Qualification Matcher -> Explanation Generator for Recruiters.

---

### Q46: Design an AI Voice Assistant Architecture.
**Answer:** Low-latency WebSockets connecting VAD, ASR, Fast LLM, and TTS with interrupting audio handling.

---

### Q47: Design a Multi-Agent Workflow System for Complex Tasks.
**Answer:** Shared State Graph -> Task Router -> Specialized Agents -> Verification Node -> Output Aggregator.

---

### Q48: Design a Real-Time AI Transcription System.
**Answer:** Audio Stream Chunking -> Concurrent Worker Queue -> Streaming Whisper ASR -> Speaker Diarization Module -> Websocket Output.

---

### Q49: Design a Live Streaming Content Moderation System.
**Answer:** Video Keyframe & Audio Stream Sampler -> Real-Time Vision/Speech Classifiers -> Automated Flagging -> Human Review Dashboard.
