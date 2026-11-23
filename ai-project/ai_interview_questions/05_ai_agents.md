# Section 5: AI Agents and Agentic Systems

> Comprehensive, clear answers for all 53 AI Agent questions.

---

### Q1: What is an AI agent, and how does it differ from a simple LLM call?
**Answer:** A simple LLM call is a single passive step (`Input -> Text Output`). An AI agent is an autonomous loop (`Reason -> Plan -> Tool Call -> Observe -> Re-evaluate`) that runs iteratively to achieve a complex goal.

---

### Q2: What is AI Agent Memory?
**Answer:** Memory allows agents to store and recall information across steps and sessions. It includes Short-Term Memory (prompt context), Long-Term Memory (Vector DB history), and Episodic Memory (past task logs).

---

### Q3: What is Harness Engineering in AI?
**Answer:** Harness Engineering is building the infrastructure, state management, file tools, error hooks, and context pruning systems surrounding an LLM that enable it to operate reliably in real-world environments.

---

### Q4: What matters more for an agentic coding tool like Claude Code: the model or the harness?
**Answer:** Both are critical, but the harness often matters more in production. A strong harness handles file editing, terminal execution, error recovery, and context compaction so even a medium LLM performs effectively.

---

### Q5: Explain the ReAct (Reasoning + Acting) agent architecture.
**Answer:** ReAct alternates between `Thought` (reasoning about next step), `Action` (tool call execution), and `Observation` (tool result analysis) until the objective is complete.

---

### Q6: What is the Plan-and-Execute agent pattern?
**Answer:** An agent breaks an objective into a multi-step execution plan first, then runs each sub-task sequentially, re-planning only when a step fails.

---

### Q7: What is tool use (function calling) in LLMs, and how does it enable agents?
**Answer:** Function calling lets an LLM emit structured JSON specifying a tool name and arguments instead of text. The application executes the tool and returns results to the LLM, enabling action execution.

---

### Q8: What is the difference between structured output and function calling?
**Answer:**
- **Structured Output:** Enforces final model text generation into a typed format (JSON/XML).
- **Function Calling:** Invokes external code/APIs mid-generation as an intermediate action step.

---

### Q9: How do you design and define tools for an AI agent?
**Answer:** Define tools with clear names, detailed descriptions explaining *when* and *how* to use them, and strict input JSON schemas with type validation.

---

### Q10: How does an agent decide when to call a tool versus answering from knowledge?
**Answer:** Prompt instructions and tool descriptions guide the LLM. If the prompt asks for real-time/external data covered by a tool description, the LLM generates a function call response.

---

### Q11: What is the difference between single-agent and multi-agent systems?
**Answer:**
- **Single-Agent:** One agent manages all tools and planning. Simple and cheap.
- **Multi-Agent:** Specialized agents (e.g., Planner, Coder, Reviewer) collaborate via message passing.

---

### Q12: When do multi-agent systems break down, and when is a single agent better?
**Answer:** Multi-agent systems break down when sub-agent messages loop endlessly, lose context, or spike token costs. Single agents with isolated tools are better for straight-line tasks.

---

### Q13: What is Model Context Protocol (MCP), and how does it standardize tool integration?
**Answer:** MCP (by Anthropic) defines an open standard protocol over JSON-RPC connecting AI Hosts (Claude Desktop, IDEs) with external Tool Servers without custom glue code.

---

### Q14: How does MCP differ from traditional function calling?
**Answer:** Function calling is model-specific API formatting. MCP is a standardized architecture for tool discovery, authentication, resources, and execution across any client app.

---

### Q15: What are AI SubAgents?
**Answer:** SubAgents are child agent loops spawned by a parent agent to handle dedicated sub-tasks independently, returning summarized results back to the parent agent.

---

### Q16: What are the different types of agent memory (short-term, long-term, episodic)?
**Answer:**
- **Short-term:** Active prompt context.
- **Long-term:** Vector DB user profile/history.
- **Episodic:** Execution trajectory logs and reusable skills.

---

### Q17: How do you handle agent failures and implement error recovery?
**Answer:** Feed raw tool error tracebacks back to the agent in the `Observation` step, allowing the model to analyze the error, adjust arguments, or try an alternative tool.

---

### Q18: What is an agent loop, and how does it decide when to stop?
**Answer:** An agent loop runs autoregressively until the LLM outputs a final answer token, hits max step limits, or triggers a stop condition.

---

### Q19: What is Context Engineering?
**Answer:** Context Engineering is actively managing, structuring, and dynamically inserting relevant system instructions, memory, tool definitions, and historical turns into the prompt context window.

---

### Q20: How does context compaction work?
**Answer:** Context compaction summarizes or prunes older conversation turns and intermediate tool observations, keeping context window usage lean without losing key state.

---

### Q21: What is Loop Engineering?
**Answer:** Loop Engineering designs the execution loop constraints—step budgets, retry rules, backoff strategies, and state transition graphs.

---

### Q22: What is Graph Engineering (LangGraph)?
**Answer:** Graph Engineering models agent execution workflows as directed state graphs (Nodes = actions/LLM calls, Edges = conditional logic), enabling robust multi-step control.

---

### Q23: How do AI Agents Communicate?
**Answer:** Agents communicate via structured message channels, JSON payload passing, or shared scratchpad state graphs.

---

### Q24: What are Agent Skills?
**Answer:** Agent Skills are modular, documented procedural workflows or scripts that agents can load dynamically to solve recurring specialized tasks.

---

### Q25: How do you evaluate and test AI agents?
**Answer:** Run task completion benchmarks (SWE-bench / WebArena), track step count efficiency, monitor tool call accuracy, and run unit tests on tool implementations.

---

### Q26: What are security risks of agentic systems, and how do you mitigate them?
**Answer:** Risks include indirect prompt injection, data exfiltration, and unauthorized actions. Mitigate with sandboxing, input filters, tool access controls, and human approvals.

---

### Q27: How to prevent indirect prompt injection and data exfiltration in agents reading untrusted content?
**Answer:** Separate untrusted data in XML tags, restrict tool outputs, disable file/network write tools on untrusted inputs, and require human confirmation.

---

### Q28: What is the difference between reactive and proactive agents?
**Answer:**
- **Reactive:** Responds only when triggered by user inputs.
- **Proactive:** Monitors background events/triggers and initiates actions autonomously.

---

### Q29: How to manage token consumption and cost in long-running agent workflows?
**Answer:** Compact history, truncate tool observations, use smaller models for sub-tasks, enforce max step budgets, and leverage prompt caching.

---

### Q30: What is the human-in-the-loop (HITL) pattern, and when is it needed?
**Answer:** HITL pauses agent execution to require human approval before performing high-risk actions (e.g. deleting databases, sending emails, executing payments).

---

### Q31: How do you implement guardrails for AI agents?
**Answer:** Intercept tool calls before execution with permission validators, regex checks, and policy rules.

---

### Q32: What is agent reflection, and how does it improve performance?
**Answer:** Reflection is an agent step where a critic prompt reviews past execution outputs, detects mistakes, and writes self-correction feedback.

---

### Q33: Code-generating agents vs. tool-calling agents.
**Answer:** Code-generating agents write and run raw Python/Bash scripts in a sandbox. Tool-calling agents execute fixed API endpoints.

---

### Q34: How do you handle multimodal inputs and outputs in agentic systems?
**Answer:** Pass images/audio to vision/speech models, attach image URLs/tokens to agent context, and output multimodal artifacts.

---

### Q35: How do you implement state management in complex agent workflows?
**Answer:** Use persistent graph state objects (e.g. LangGraph `StateGraph`), updating explicit state dictionaries across nodes.

---

### Q36: How do you build a customer support agent with escalation logic?
**Answer:** Maintain confidence scoring; if agent intent confidence is low or user sentiment is negative, trigger escalation tool to transfer session to human agent.

---

### Q37: What is agent orchestration, and how do you implement it?
**Answer:** Agent orchestration coordinates execution flow across multiple agents using a supervisor agent or graph router.

---

### Q38: What is Sakana Fugu?
**Answer:** Sakana Fugu is an orchestration framework that dynamically allocates tasks to specialized AI models based on task requirements and cost constraints.

---

### Q39: How do you build a code execution agent safely using sandboxed environments?
**Answer:** Execute user code inside isolated Docker containers or microVMs (E2B / Modal) with strict execution timeouts, no root access, and restricted network rules.

---

### Q40: Your AI agent is stuck in an infinite loop. How do you break the cycle?
**Answer:** Enforce a hard step budget (max 15 steps) and detect repeated identical tool call arguments to halt execution.

---

### Q41: Your agent gets conflicting answers from different tools. How does it reconcile them?
**Answer:** Prompt agent to compare tool authority/timestamps or execute a tie-breaker verification tool.

---

### Q42: Your AI agent burns too many tokens per task. How do you reduce token consumption?
**Answer:** Summarize past chat turns, trim tool outputs (return top 3 lines instead of full payload), and use prompt caching.

---

### Q43: Your AI agent keeps exceeding its budget per task. How do you enforce budget limits?
**Answer:** Track dollar cost and token usage per session; terminate loop when budget ceiling is hit.

---

### Q44: Your agent hallucinates tool capabilities and passes wrong inputs. How do you fix it?
**Answer:** Provide precise JSON schemas, simplify tool descriptions, and add few-shot tool call examples.

---

### Q45: Your AI agent deleted a production database. How to prevent irreversible actions?
**Answer:** Require explicit Human-in-the-Loop approval for destructive operations and enforce read-only database connections.

---

### Q46: Your agent has many tools but keeps picking the wrong one. How to improve selection?
**Answer:** Group tools into domain categories, reduce total tools in context (tool routing), and improve tool descriptions.

---

### Q47: Your AI agent takes too long to complete a task. How do you speed it up?
**Answer:** Parallelize independent tool calls, use fast LLM endpoints (Groq/vLLM), and reduce reflection steps.

---

### Q48: Your long-running agent drifts after hours. How do you diagnose and fix it?
**Answer:** Re-inject core system objective into prompt context every $N$ steps and trim irrelevant scratchpad history.

---

### Q49: LLM selects right tool but extracts wrong parameters. How to fix parameter extraction?
**Answer:** Use Pydantic/Instructor constrained schema decoding and provide few-shot parameter extraction examples.

---

### Q50: How do Computer-Use Agents work?
**Answer:** Computer-use agents take desktop screenshots, pass images to Vision-Language Models, locate UI element coordinates, and emit mouse/keyboard actions.

---

### Q51: How does LangChain work?
**Answer:** LangChain is an open-source framework providing abstractions (Chains, Prompts, Tools, Retrievers, Memory) to assemble LLM pipelines.

---

### Q52: How does LangGraph work?
**Answer:** LangGraph builds stateful multi-agent workflows as cyclical graphs with state persistence, branching, and human-in-the-loop control.

---

### Q53: What is OKF (Open Knowledge Format)?
**Answer:** OKF is a standardized schema representation for structuring domain knowledge for agent consumption.
