# Debugging Workflow

```text
Issue Reported
      │
      ▼
Reproduce the Issue
      │
      ▼
Collect Logs
      │
      ▼
Identify Failing Stage
      │
      ▼
Timeout?
      │
      ├── Yes → Check API latency, retries, network
      │
      ▼
Malformed Output?
      │
      ├── Yes → Validate JSON, retry, schema validation
      │
      ▼
Wrong Data?
      │
      ├── Yes → Verify retrieval, prompts, intermediate outputs
      │
      ▼
Apply Fix
      │
      ▼
Regression Testing
      │
      ▼
Deploy & Monitor
```