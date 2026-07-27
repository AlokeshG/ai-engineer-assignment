# Part 2 – Debugging an Intermittently Failing Multi-Agent Pipeline

## Problem Statement

A multi-agent AI workflow shows intermittent failures:

- Requests occasionally time out.
- Some responses contain malformed JSON.
- Some requests complete successfully but produce incorrect results.

The objective is to identify the root cause using a structured debugging approach.

---

# Step 1 – Reproduce the Issue

The first step is to determine whether the issue is reproducible.

Actions:
- Run the same request multiple times.
- Test with different inputs.
- Record the frequency of failures.

Goal:
Determine whether the issue is deterministic or intermittent.

---

# Step 2 – Check Application Logs

Collect logs from every component.

Examples:
- API server logs
- Agent execution logs
- LLM request logs
- Database logs
- Retrieval logs

Things to check:
- Exceptions
- Slow API calls
- Failed requests
- Retry attempts

---

# Step 3 – Identify the Failing Stage

Break the pipeline into individual stages.

Example:

User Query

↓

Planner Agent

↓

Retriever

↓

Reasoning Agent

↓

Response Generator

Run every stage independently.

This isolates where the failure occurs.

---

# Step 4 – Investigate Timeout Issues

Possible causes:

- Slow vector database search
- Large prompts
- External API latency
- Infinite loops
- Network issues

Actions:

- Measure latency for every stage.
- Add timeout logging.
- Retry transient failures.

---

# Step 5 – Validate Structured Output

Malformed JSON usually occurs when the LLM does not strictly follow the expected format.

Example:

Incorrect:

{
"name":"Alice"
"age":25
}

Solution:

- Use structured output.
- Validate responses using Pydantic.
- Retry invalid responses.

---

# Step 6 – Investigate Incorrect Results

If the output looks valid but is incorrect:

Check:

- Retrieved documents
- Prompt construction
- Agent reasoning
- Context passed between agents

Verify each intermediate output.

---

# Step 7 – Add Monitoring

Useful tools include:

- LangSmith
- OpenTelemetry
- Application logs
- Correlation IDs

These help trace every request across the workflow.

---

# Step 8 – Regression Testing

After fixing the issue:

- Re-run failing scenarios.
- Add automated tests.
- Ensure the issue no longer occurs.
- Monitor production after deployment.

---

# Conclusion

The debugging process focuses on isolating failures systematically rather than guessing. By validating every stage independently, collecting detailed logs, and adding monitoring, intermittent issues can be diagnosed and resolved efficiently.