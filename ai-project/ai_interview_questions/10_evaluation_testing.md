# Section 10: Evaluation and Testing

> Comprehensive, clear answers for all 36 Evaluation & Testing questions.

---

### Q1: What is AI Agent Evaluation?
**Answer:** Measuring an agent's capability to complete open-ended tasks, assessing success rate, step count efficiency, tool call accuracy, and error recovery.

---

### Q2: What is LLM Evaluation?
**Answer:** Systematically assessing LLM output quality across metrics like factual correctness, relevance, coherence, safety, and format adherence.

---

### Q3: What is AI Agent Observability?
**Answer:** Tracing, logging, and visualizing every execution step of an AI agent (prompts, thought steps, tool calls, responses) in real time.

---

### Q4: What is Evaluation-Driven Development (EDD)?
**Answer:** Building test evaluation suites (golden datasets) *before* writing prompts or code, driving prompt engineering and model selection via objective test score improvements.

---

### Q5: Why is AI only as good as our definition of done?
**Answer:** Because LLM tasks are open-ended and non-deterministic; without clear, quantitative evaluation criteria (definition of done), you cannot reliably detect regressions or verify quality.

---

### Q6: How do you evaluate LLM outputs, and what metrics do you use?
**Answer:** Use a combination of deterministic matching, heuristic checks (JSON validation), semantic metrics (BERTScore), and LLM-as-a-judge scoring rubrics.

---

### Q7: Compare BLEU, ROUGE, and BERTScore.
**Answer:**
- **BLEU:** $N$-gram precision (used for translation).
- **ROUGE:** $N$-gram recall (used for summarization).
- **BERTScore:** Cosine similarity of BERT embeddings (captures semantic meaning).

---

### Q8: What is G-Eval, and how does it use LLMs for evaluation?
**Answer:** G-Eval uses LLMs (like GPT-4) with Chain-of-Thought prompting and explicit scoring rubrics to evaluate text quality on a 1-5 scale with probabilities.

---

### Q9: What is LLM-as-a-Judge, and what are its limitations?
**Answer:** Using a strong LLM to grade outputs. Limitations include position bias (preferring 1st option), verbosity bias (favoring long answers), and self-enhancement bias.

---

### Q10: How do you conduct human evaluation for AI systems?
**Answer:** Create clear annotation rubrics, collect blind pairwise preferences or Likert ratings from domain experts, and measure inter-annotator agreement.

---

### Q11: What is red teaming?
**Answer:** Adversarial testing where security engineers intentionally attempt to break safety filters, trigger hallucinations, or jailbreak the LLM system.

---

### Q12: How do you detect and measure hallucinations?
**Answer:** Run NLI (Natural Language Inference) entailment models to verify if generated statements logically follow from context chunks (Ragas Faithfulness metric).

---

### Q13: What is adversarial testing?
**Answer:** Subjecting the AI system to perturbed, misspelled, ambiguous, or malicious inputs to test output robustness and safety boundaries.

---

### Q14: How to build a regression test suite for AI apps?
**Answer:** Maintain a golden dataset of test cases; automatically run evals on PR commits to ensure prompt changes do not lower accuracy scores.

---

### Q15: What are benchmark suites (MMLU, HumanEval, GSM8K)?
**Answer:** Standardized open benchmarks: MMLU (general knowledge), HumanEval (Python coding), GSM8K (grade-school math reasoning).

---

### Q16: What is benchmark contamination?
**Answer:** When benchmark test questions accidentally leak into an LLM's pre-training dataset, inflating benchmark scores without true capability gains.

---

### Q17: Model scores higher on benchmarks but users say it got worse. Why?
**Answer:** Benchmark contamination, overfitting to benchmark style, or benchmarks failing to capture real-world user distribution edge cases.

---

### Q18: How do you evaluate a RAG system end-to-end?
**Answer:** Evaluate Retrieval (Context Precision & Context Recall) and Generation (Faithfulness & Answer Relevance) separately and together.

---

### Q19: How to evaluate quality of AI agents?
**Answer:** Track Task Completion Pass Rate, Tool Selection Accuracy, Parameter Extraction Accuracy, Average Steps to Resolution, and Financial Cost.

---

### Q20: How to evaluate autonomous coding agents? Why can SWE-bench pass rates be misleading?
**Answer:** Run automated unit tests on generated code diffs. SWE-bench pass rates can be misleading due to test harness fragility and dataset leakage.

---

### Q21: Offline vs Online Evaluation.
**Answer:**
- **Offline:** Pre-deployment testing on golden eval datasets.
- **Online:** Live production monitoring of user feedback (thumbs up/down), click-through rates, and latency.

---

### Q22: How to measure factual consistency?
**Answer:** Compare output claims against ground-truth context using NLI entailment models or LLM claim verification prompts.

---

### Q23: How to evaluate multi-turn conversation quality?
**Answer:** Assess goal completion, context retention across turns, topic-switching handling, and user satisfaction over full conversation logs.

---

### Q24: Role of golden datasets in AI evaluation.
**Answer:** Golden datasets provide curated, representative test cases with reference answers used as ground truth for reliable continuous testing.

---

### Q25: Building an eval set with no labeled ground truth and expensive experts.
**Answer:** Use synthetic data generation with strong models, seed with real anonymized production queries, and have experts review only a small core subset.

---

### Q26: Implementing continuous evaluation in production.
**Answer:** Sample 1-5% of production traces asynchronously, running automated LLM-as-a-judge and guardrail scoring pipelines.

---

### Q27: How to evaluate bias in AI outputs?
**Answer:** Test outputs across demographic counterfactual inputs (swapping gender, race, or location terms) and measure statistical disparity.

---

### Q28: Comparing two models or prompts in a statistically rigorous way.
**Answer:** Conduct randomized A/B testing, run paired t-tests or bootstrap confidence intervals on eval metric scores to ensure statistical significance.

---

### Q29: Evaluating robustness across input variations.
**Answer:** Run stress testing with paraphrased queries, typos, varying text lengths, and edge-case inputs.

---

### Q30: Differences between evaluating traditional ML vs LLM applications.
**Answer:** Traditional ML uses strict deterministic metrics (Accuracy, F1, RMSE). LLMs require open-ended semantic evaluation, safety guardrails, and LLM-as-a-judge rubrics.

---

### Q31: Setting up an evaluation framework from scratch.
**Answer:** Define key metrics $\to$ Collect 50-100 representative test prompts $\to$ Create evaluation scripts (Ragas / LLM-as-a-judge) $\to$ Integrate into CI/CD pipeline.

---

### Q32: Handling conflicting audit results (passes one fairness metric, fails another).
**Answer:** Analyze trade-offs with stakeholders and align model behavior with domain-specific legal and ethical standards (e.g. Disparate Impact rule).

---

### Q33: Model became biased 6 months after deployment. How to monitor?
**Answer:** Set up continuous production drift monitoring tracking demographic distribution shifts and automated fairness checks on live logs.

---

### Q34: Auditor cannot reproduce model results. How to ensure reproducibility?
**Answer:** Fix random seeds, pin model API version parameters, record exact system prompts, temperature `0.0`, and environment dependencies.

---

### Q35: Structuring red teaming before launch.
**Answer:** Form an adversarial red team to test jailbreaks, prompt injections, PII extraction, toxic generation, and safety boundary bypasses.

---

### Q36: Red teaming a multimodal model.
**Answer:** Test cross-modal attacks (e.g. embedding malicious text inside images or combining benign text with adversarial image inputs).
