# AI Engineer Assignment

This repository contains my solution for the AI Engineer technical assessment.

## Repository Structure

```
ai-engineer-assignment/
│
├── part1-token-optimization/
├── part2-debugging/
├── part3-cicd/
├── .github/workflows/
├── README.md
└── requirements.txt
```

---

## Part 1 – Token & Cost Optimization

Implemented two optimizations to reduce token usage in a multi-agent pipeline:

- Retrieval Chunking
- Conversation Summarization

### Results

| Metric | Before | After |
|--------|--------:|------:|
| Input Tokens | 100,000 | 18,000 |
| Reduction | - | 82% |

---

## Part 2 – Debugging

Documented a structured debugging methodology for an intermittent multi-agent pipeline.

Covered:

- Timeout investigation
- Log analysis
- Malformed JSON handling
- Incorrect output investigation
- Regression testing

---

## Part 3 – CI/CD & Deployment

Implemented a GitHub Actions workflow that:

- Runs on every push
- Sets up Python
- Installs dependencies
- Runs linting
- Runs tests
- Simulates deployment to a staging environment

Also documented:

- Secrets management
- Rollback strategy
- Deployment process

---

## Technologies Used

- Python
- Git
- GitHub Actions
- Markdown

---

## Author

**Alokesh Ghosh**