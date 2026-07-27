# Part 1 – Token & Cost Optimization

## Problem Statement

The baseline multi-agent pipeline consumes approximately **100,000 input tokens per query** because each agent receives:
- The full system prompt
- Complete conversation history
- Entire retrieved documents

This increases both API cost and response latency.

---

## Optimization 1: Retrieval Chunking

### Before
Every agent receives the complete document (~25,000 tokens).

### After
Only the top relevant chunks are retrieved using semantic search.

**Estimated Tokens**

- Before: 25,000
- After: 3,500

### Quality Trade-off

Minimal. Since only relevant information is passed to the model, answer quality remains nearly unchanged while reducing unnecessary context.

---

## Optimization 2: Conversation Summarization

### Before

Every request includes the complete chat history.

### After

The pipeline sends:
- A summary of previous conversations
- Recent messages
- Current user query

**Estimated Tokens**

- Before: 20,000+
- After: 2,000

### Quality Trade-off

A small amount of long-term conversational detail may be lost, but overall response quality remains high.

---

## Token Comparison

| Agent | Before | After |
|--------|---------|-------|
| Planner | 25,000 | 6,000 |
| Retriever | 25,000 | 3,500 |
| Reasoner | 25,000 | 4,500 |
| Final Response | 25,000 | 4,000 |
| **Total** | **100,000** | **18,000** |

**Overall Reduction:** **82%**

---

## Conclusion

By retrieving only relevant context and summarizing conversation history, the pipeline reduces token usage from approximately **100K** to **18K** tokens while maintaining comparable output quality. This significantly lowers inference cost and improves response time.