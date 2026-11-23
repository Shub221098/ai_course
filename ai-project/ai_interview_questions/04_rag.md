# Section 4: Retrieval-Augmented Generation (RAG)

> Comprehensive, clear answers for all 42 RAG questions.

---

### Q1: What is Retrieval-Augmented Generation (RAG), and why is it important?
**Answer:** RAG connects LLMs to external data sources. It retrieves relevant chunks from a database, inserts them into the prompt, and generates grounded answers. It prevents hallucinations, provides access to private/real-time data, and avoids constant model retraining.

---

### Q2: Explain the architecture of a basic RAG system.
**Answer:**
1. **Ingestion:** Load docs $\to$ Chunk text $\to$ Embed chunks $\to$ Store in Vector DB.
2. **Retrieval:** User Query $\to$ Embed Query $\to$ Search Vector DB $\to$ Retrieve Top-K Chunks.
3. **Generation:** Construct Prompt (System Instructions + Top-K Chunks + User Query) $\to$ LLM $\to$ Answer.

---

### Q3: What are the key components of a RAG pipeline?
**Answer:** Document Loader, Text Splitter (Chunker), Embedding Model, Vector Database, Retriever/Reranker, Prompt Builder, and LLM Generator.

---

### Q4: What are chunking strategies, and how do you choose the right chunk size?
**Answer:** Chunking splits documents into smaller passages. Small chunks (100-300 tokens) offer precise vector retrieval; large chunks (500-1000 tokens) offer better contextual understanding. Pick based on domain complexity and context limits.

---

### Q5: Compare fixed-size chunking, semantic chunking, and recursive chunking.
**Answer:**
- **Fixed-size:** Splits every $N$ tokens with overlap. Fast, but cuts sentences mid-thought.
- **Recursive:** Recursively splits on `\n\n`, `\n`, space, keeping paragraph/sentence structure.
- **Semantic:** Embeds consecutive sentences and splits where semantic similarity drops.

---

### Q6: What is Contextual Retrieval, and how does it improve RAG?
**Answer:** Contextual Retrieval (Anthropic) prepends document-level summary context to every individual chunk before embedding it, resolving ambiguous pronouns and improving retrieval accuracy by 35-50%.

---

### Q7: What are embedding models, and how do they convert text to vectors?
**Answer:** Embedding models are neural networks trained with contrastive loss to convert text strings into continuous numerical vectors where semantically similar texts have high cosine similarity.

---

### Q8: How do you choose an embedding model for your RAG system?
**Answer:** Benchmark options using MTEB (Massive Text Embedding Benchmark), considering language support, vector dimensionality (e.g. 768 vs 1536), latency budget, and domain specificity.

---

### Q9: Explain Agentic RAG.
**Answer:** Agentic RAG uses an AI Agent to dynamically reformulate queries, route requests to multiple databases, evaluate if retrieved context is sufficient, and execute iterative retrieval loops.

---

### Q10: What is hybrid search, and why is it better than pure vector search?
**Answer:** Hybrid Search combines Dense Vector Search (semantic similarity) + Sparse BM25 Search (exact keyword/ID matching) using Reciprocal Rank Fusion (RRF), delivering superior retrieval across all query types.

---

### Q11: What is re-ranking, and how does it improve RAG retrieval quality?
**Answer:** Re-ranking uses a Cross-Encoder to compute joint token-to-token attention between Query and candidate chunks, re-scoring vector search results to ensure only top relevant chunks reach the LLM.

---

### Q12: What is ColBERT, and how does late interaction retrieval work?
**Answer:** ColBERT preserves fine-grained token embeddings for Query and Document, computing late-interaction MaxSim dot products. Fast like vector search, accurate like cross-encoders.

---

### Q13: Compare reranker architectures: Cross-Encoder vs ColBERT vs LLM-based rerankers.
**Answer:**
- **Cross-Encoder:** High accuracy, medium speed.
- **ColBERT:** Very fast, strong accuracy.
- **LLM Reranker:** Uses LLM to grade chunk relevance. Highest accuracy, slow & expensive.

---

### Q14: How do you handle multi-document and multi-hop questions in RAG?
**Answer:** Use Agentic RAG query decomposition (breaking complex query into sub-queries), GraphRAG, or iterative multi-step retrieval.

---

### Q15: What is the "lost in the middle" problem in RAG systems?
**Answer:** LLMs pay highest attention to information placed at the very beginning or end of long prompts, ignoring facts in middle chunks. Fix by sorting top chunks to prompt boundaries.

---

### Q16: How do you evaluate a RAG system (Ragas metrics)?
**Answer:**
- **Faithfulness:** Is answer grounded in context?
- **Answer Relevance:** Does answer address query?
- **Context Precision:** Are retrieved chunks relevant?
- **Context Recall:** Did retriever find all necessary info?

---

### Q17: Explain Self-RAG. How does the model decide when to retrieve?
**Answer:** Self-RAG uses special reflection tokens (`[Retrieve]`, `[IsRel]`, `[IsSup]`) to dynamically decide whether to retrieve context, check relevance, and verify output grounding.

---

### Q18: What is GraphRAG, and when would you use it over traditional RAG?
**Answer:** GraphRAG extracts Knowledge Graphs (Entities & Relations) from documents. Use it when queries require global dataset summarization or connecting facts across many documents.

---

### Q19: What is Vectorless RAG?
**Answer:** Vectorless RAG retrieves context using full-text search engines (BM25 / Elasticsearch) or Knowledge Graphs without generating dense vector embeddings.

---

### Q20: How do you handle structured data (tables, SQL databases) in a RAG pipeline?
**Answer:** Use Text-to-SQL generation (schema injection into prompt), extract tables as Markdown/JSON objects, or construct multi-modal table embeddings.

---

### Q21: What are common failure modes of RAG systems, and how do you debug them?
**Answer:** Failure modes: Retrieval misses chunk, retrieved chunk lacks answer, LLM ignores context, LLM hallucinates. Debug by isolating retrieval eval vs generation eval.

---

### Q22: How do you handle document updates and maintain freshness in a RAG system?
**Answer:** Maintain a document manifest with content hashes (`MD5`). Upsert modified document chunks by ID and delete obsolete vector IDs using background sync pipelines.

---

### Q23: How do you optimize RAG for latency in production?
**Answer:** Use HNSW vector indexes, hybrid search with pre-filtering, prompt caching for static system prompts, fast Cross-Encoders, and streaming responses.

---

### Q24: What is the role of metadata filtering in RAG systems?
**Answer:** Metadata filtering scopes vector search using structured attributes (e.g. `user_id`, `department`, `date_created`), enforcing security RBAC and boosting speed.

---

### Q25: Compare RAG vs Fine-Tuning. When would you use each?
**Answer:**
- **RAG:** Use for dynamic/private data, citation requirements, and zero retraining costs.
- **Fine-Tuning:** Use to teach specialized style, output format, or domain tone.

---

### Q26: Long context vs RAG: When to use retrieval vs putting everything in context?
**Answer:** Use long context for single document analysis/codebase reviews. Use RAG for large/evolving corpora (millions of docs) to control cost, latency, and "lost in the middle" errors.

---

### Q27: What is query transformation (HyDE, query decomposition, step-back)?
**Answer:**
- **HyDE:** Generates a hypothetical answer, then embeds that answer to search for similar real chunks.
- **Query Decomposition:** Splits complex queries into smaller sub-queries.
- **Step-Back Prompting:** Generates a higher-level abstract query.

---

### Q28: How do you implement citation and source attribution in RAG?
**Answer:** Assign unique ID tags to retrieved chunks (e.g. `[Doc 1]`), instruct LLM to cite tags inline, and map tags to source URLs/page numbers in the UI response.

---

### Q29: How do you scale a RAG system to millions of documents?
**Answer:** Use distributed vector DBs (Qdrant / Milvus / Pinecone), HNSW/IVF indexing with scalar quantization (SQ8), metadata pre-filtering, and distributed async ingestion queues.

---

### Q30: What is parent-child chunking, and how does it improve retrieval?
**Answer:** Small child chunks (100 tokens) are indexed for precise vector retrieval, but when matched, the larger parent chunk (1000 tokens) is fetched and sent to the LLM for context.

---

### Q31: Your RAG system is hallucinating despite having the right context. How do you fix it?
**Answer:** Lower temperature to 0.0, enforce strict system prompts (`"Answer strictly using context"`), and add NLI output verification guardrails.

---

### Q32: Your RAG chunk overlap causes redundant results. How do you reduce redundancy?
**Answer:** Apply Maximal Marginal Relevance (MMR) or vector deduplication to diversify retrieved chunks.

---

### Q33: Your RAG retrieval is too slow with a large knowledge base. How do you speed it up?
**Answer:** Use HNSW indexing, quantize vector embeddings (SQ8 / PQ), apply metadata pre-filtering, and cache frequent query results.

---

### Q34: Your RAG system returns duplicate results. How do you deduplicate?
**Answer:** Filter out chunks with cosine similarity $> 0.95$ to existing chunks, or deduplicate by parent document ID.

---

### Q35: Your RAG system needs per-user access control. How do you implement it?
**Answer:** Embed security tenant IDs / user permission groups in vector metadata and run metadata-filtered vector queries matching current user permissions.

---

### Q36: Your RAG system fails on domain-specific jargon. How do you fix it?
**Answer:** Use Hybrid Search (BM25 catches exact jargon terms), or fine-tune embedding models using domain-specific contrastive learning.

---

### Q37: Your text-only RAG system now needs to handle images and tables. How do you extend it?
**Answer:** Use multimodal embedding models (CLIP / ColPali), parse tables to Markdown/HTML, or generate LLM summaries for images before chunking.

---

### Q38: Your RAG knowledge base gets updated frequently and needs versioning. How do you manage it?
**Answer:** Tag vector metadata with document `version_id` and `timestamp`, querying only active versions while running async delta indexing.

---

### Q39: Your RAG system fails on multi-hop questions requiring combining facts. How do you fix it?
**Answer:** Upgrade to Agentic RAG (iterative search loops) or GraphRAG (Knowledge Graph traversal).

---

### Q40: Enterprise RAG returns contradictory answers from different documents. How do you resolve conflicts?
**Answer:** Include document timestamps/authority scores in prompt metadata, instructing LLM to favor newer or higher-authority source files.

---

### Q41: Your RAG system returns outdated answers from an evolving knowledge base. How do you keep it current?
**Answer:** Run automated CDC (Change Data Capture) pipelines to delete obsolete vector IDs and insert updated chunks instantly.

---

### Q42: Your RAG system struggles with PDF documents containing tables and layouts. How do you fix PDF parsing?
**Answer:** Replace simple text extractors with vision-based document layout parsers (Unstructured, LlamaParse, MinerU) that extract tables as clean Markdown.
