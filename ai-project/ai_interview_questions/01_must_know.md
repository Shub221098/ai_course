# Section 1: Must Know

> Core foundation terms every AI Engineer must understand.

---

### Q1: What is an LLM (Large Language Model)?
**Answer:** A Large Language Model (LLM) is a massive neural network (typically based on the Transformer architecture) trained on hundreds of billions or trillions of words. It works by predicting the most statistically likely next word (token) given a sequence of input text. Examples: GPT-4, Claude 3.5 Sonnet, Llama 3.

---

### Q2: What is RAG (Retrieval-Augmented Generation)?
**Answer:** RAG is an architecture that connects an LLM to external custom data (such as company documents or a database). Before generating an answer, the system retrieves relevant information from the database, attaches it to the user's prompt as context, and asks the LLM to write an answer grounded in that retrieved context.

---

### Q3: What is MCP (Model Context Protocol)?
**Answer:** MCP is an open standard created by Anthropic that standardizes how AI applications (hosts) communicate with external data sources, servers, and tools. Instead of writing custom integration code for every API or database, tools expose their capabilities via the standard MCP protocol (like a universal USB-C plug for AI tools).

---

### Q4: What is an AI Agent?
**Answer:** An AI Agent is an autonomous software system powered by an LLM that operates in a loop: it receives a goal, creates a plan, calls tools (like web search, python interpreter, database queries), inspects the results, and iterates until the objective is achieved without constant human intervention.

---

### Q5: What is Fine-Tuning?
**Answer:** Fine-Tuning is the process of taking a pre-trained foundation model and updating its internal weights on a smaller, specialized dataset. This adapts the model to follow a specific output style, format, domain jargon (e.g. legal or medical), or specific task performance.

---

### Q6: What is Quantization?
**Answer:** Quantization is a model compression technique that converts model weights and activations from high-precision numbers (like 16-bit float `FP16` or `BF16`) to lower-precision representations (like 8-bit `INT8` or 4-bit `INT4`). This reduces memory requirements by 50-75% and speeds up inference with minimal loss in accuracy.
