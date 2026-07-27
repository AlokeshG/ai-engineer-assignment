# AI Engineer Assignment

This repository contains my solution for the AI Engineer technical assessment.

---

# Repository Structure

```
ai-engineer-assignment/
│
├── part1-token-optimization/
│   ├── baseline.py
│   ├── optimized.py
│   └── sample_results.md
│
├── part2-debugging/
│
├── .github/
│   └── workflows/
│
├── README.md
└── requirements.txt
```

---

# Part 1 – Token & Cost Optimization

## Problem

The baseline multi-agent pipeline consumes approximately **100,000 input tokens per query** because every agent receives:

- Complete retrieved documents
- Full conversation history
- Long system prompts

This results in higher inference cost and increased response latency.

## Optimizations Implemented

### 1. Retrieval Chunking

Instead of sending the complete document to every agent, only the most relevant semantic chunks are retrieved.

**Benefits**

- Reduces unnecessary context
- Faster inference
- Lower API cost

### 2. Conversation Summarization

Instead of including the full chat history, the pipeline sends:

- Conversation summary
- Recent messages
- Current user query

This significantly reduces token usage while preserving context.

## Token Comparison

| Pipeline | Tokens |
|-----------|---------:|
| Original | 100,000 |
| Optimized | 18,000 |

**Overall Reduction:** **82%**

---

# Part 2 – Debugging

(To be implemented)

This section documents my structured debugging methodology for intermittent failures in multi-agent AI workflows, including timeout analysis, malformed outputs, and incorrect responses.

---

# Part 3 – CI/CD & Deployment

(To be implemented)

This section includes:

- GitHub Actions CI pipeline
- Automated staging deployment
- Secure secrets management
- Rollback strategy

---

# Technologies Used

- Python
- Git
- GitHub Actions
- Markdown

---

# Author

**Alokesh Ghosh**
