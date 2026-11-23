# Section 3: Prompt Engineering

> Comprehensive, clear answers for all 30 Prompt Engineering questions.

---

### Q1: What is prompt engineering, and why is it critical for AI applications?
**Answer:** Prompt engineering is the craft of designing, structuring, and refining textual inputs to guide LLMs toward desired outputs without altering model weights. It is critical because LLM outputs are highly sensitive to phrasing, formatting, and context structure.

---

### Q2: Explain zero-shot, one-shot, and few-shot prompting with examples.
**Answer:**
- **Zero-Shot:** Giving instructions without examples (`"Translate 'hello' to Spanish."`).
- **One-Shot:** Providing 1 input-output example before the prompt.
- **Few-Shot:** Providing 2-5 input-output examples (`"Positive -> Happy\nNegative -> Sad\nNeutral -> Okay"`). Grounded output formatting and style.

---

### Q3: What is chain-of-thought (CoT) prompting, and when should you use it?
**Answer:** CoT prompting instructs the model to break down complex tasks by writing out intermediate logical steps (`"Let's think step by step"`) before outputting the final answer. Use it for math, logic, and multi-step reasoning problems.

---

### Q4: Explain self-consistency prompting and how it improves reasoning.
**Answer:** Self-consistency generates multiple independent CoT reasoning paths for the same prompt using non-zero temperature, then selects the final answer via majority voting/consensus, filtering out random reasoning errors.

---

### Q5: What is tree-of-thought (ToT) prompting?
**Answer:** ToT prompting extends CoT by exploring a tree of intermediate thoughts, allowing the model to evaluate multiple choices at each step, look ahead, and backtrack when a reasoning branch fails.

---

### Q6: What is ReAct (Reasoning + Acting) prompting, and how does it work?
**Answer:** ReAct alternates between `Thought` (reasoning about next step), `Action` (invoking a specific tool with arguments), and `Observation` (receiving tool results) to solve dynamic tasks.

---

### Q7: What is a system prompt, and how does it influence model behavior?
**Answer:** A system prompt is top-level background metadata and instructions passed to the LLM that defines its role, persona, safety boundaries, constraints, and output guidelines across all user turns.

---

### Q8: How do you structure prompts for consistent structured output (JSON, XML)?
**Answer:**
1. Specify strict JSON/XML schema in system prompt.
2. Provide a few-shot example matching exact schema.
3. Use constrained decoding libraries (Pydantic / Instructor / Outlines).

---

### Q9: What is prompt injection, and how do you defend against it?
**Answer:**
- **Prompt Injection:** Attack where user input overwrites system prompt rules (`"Ignore previous instructions..."`).
- **Defenses:** Separate user input inside XML tags (`<user_input>`), use input guardrail models (Llama Guard), and enforce tool privilege limits.

---

### Q10: What is jailbreaking in LLMs, and what are common jailbreak techniques?
**Answer:** Jailbreaking bypasses model safety filters (e.g. roleplaying as an unrestricted persona like DAN, base64 encoding instructions, or prefix injection).

---

### Q11: How do you optimize prompts for cost and latency?
**Answer:** Trim unnecessary filler words, use prompt caching for static system prompts, replace long few-shot examples with clear rules, and use smaller model routing for simple queries.

---

### Q12: What is the difference between prompt engineering and prompt tuning?
**Answer:**
- **Prompt Engineering:** Manually editing text strings (hard prompts) without changing model parameters.
- **Prompt Tuning:** Training soft embedding vectors (continuous prompt tokens) appended to inputs via gradient descent while base model weights stay frozen.

---

### Q13: What is a prompt template, and how do you design one for production use?
**Answer:** A prompt template is a parameterized string template (e.g., using Jinja2 or F-strings) that dynamically injects user variables into a tested prompt format. Production templates should include explicit delimiters, variable validation, and fallback instructions.

---

### Q14: How do you handle multi-turn conversations with LLMs?
**Answer:** Append historical turns in `[{"role": "user", ...}, {"role": "assistant", ...}]` list format, trimming older turns or summarizing conversation state when reaching token limits.

---

### Q15: What is role prompting, and when is it effective?
**Answer:** Role prompting instructs the model to adopt a specific persona (`"You are an expert Senior Python Engineer"`). It sets domain context, tone, and appropriate detail depth.

---

### Q16: What is prompt chaining, and how do you design a chain of prompts for complex tasks?
**Answer:** Prompt chaining breaks a complex task into sequential smaller LLM calls where the output of Prompt 1 becomes the input for Prompt 2, ensuring higher accuracy and easier debugging.

---

### Q17: How do you evaluate and iterate on prompt quality?
**Answer:** Build an evaluation test suite (golden dataset), run automated eval metrics (LLM-as-a-judge / string matching), compare baseline vs new prompt versions, and track failure edge cases.

---

### Q18: What are meta-prompts, and how can they be used to generate prompts?
**Answer:** Meta-prompts are prompts that instruct an LLM to write, optimize, or debug another prompt based on desired goals and requirements.

---

### Q19: What are common failure modes in prompting, and how do you debug them?
**Answer:** Common failure modes include instruction ignoring, hallucination, output format drift, and verbosity. Debug by inspecting intermediate reasoning, isolating variable inputs, and adding few-shot examples.

---

### Q20: How do you handle edge cases and adversarial inputs in prompt design?
**Answer:** Include explicit fallback instructions (`"If input is invalid, respond 'Invalid input'"`), add adversarial examples into few-shot prompts, and validate inputs via input guardrails.

---

### Q21: What is the "lost in the middle" problem in long-context prompting?
**Answer:** LLMs pay maximum attention to information located at the beginning and end of long context prompts; facts placed in the middle are frequently missed.

---

### Q22: What are output parsers, and why are they needed for production applications?
**Answer:** Output parsers extract, validate, and transform raw LLM text outputs into typed code objects (Pydantic objects, dicts) and trigger retries on formatting errors.

---

### Q23: How do you handle multi-language prompting effectively?
**Answer:** Provide instructions in the target language, use multilingual few-shot examples, or translate user queries to English before LLM processing and back to target language.

---

### Q24: Your few-shot prompting gives inconsistent results across similar inputs. How do you stabilize it?
**Answer:** Standardize example formatting, balance class distribution across few-shot examples, order examples from simple to complex, and set temperature to `0.0`.

---

### Q25: Your LLM classification system is too sensitive to prompt wording changes. How do you reduce prompt sensitivity?
**Answer:** Use few-shot examples, set temperature to `0.0`, enforce strict JSON output schemas, and use fine-tuning or prompt ensembling.

---

### Q26: Your chatbot's system prompt containing proprietary business logic is being leaked. How do you prevent it?
**Answer:** Add post-processing output filters that check for system prompt substrings, instruct model in system prompt never to reveal rules, and move secret logic into backend tool execution code.

---

### Q27: Your LLM agent is vulnerable to prompt injection that reveals system prompt. How do you defend it?
**Answer:** Isolate untrusted input in structural tags (`<user_data>`), run input safety classifiers, and enforce tool permission boundaries.

---

### Q28: Your CoT prompting is not improving accuracy on reasoning tasks. What do you fix?
**Answer:** Provide explicit step-by-step few-shot CoT examples, ask model to double-check intermediate math, or switch to a stronger reasoning model (e.g. DeepSeek-R1 / o1).

---

### Q29: Your AI system works in English but fails for other languages. How do you add multilingual support?
**Answer:** Incorporate native multilingual prompts, use high-performing multilingual models (Llama 3 / Qwen), or add an explicit translation pre-step.

---

### Q30: Your zero-shot cross-lingual transfer from English fails on other languages. How do you fix it?
**Answer:** Add few-shot examples in the target language and fine-tune or prompt the model using target-language instructions.
