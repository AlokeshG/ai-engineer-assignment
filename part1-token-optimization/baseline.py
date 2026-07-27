# baseline.py

pipeline = {
    "Planner Agent": 25000,
    "Retriever Agent": 25000,
    "Reasoning Agent": 25000,
    "Final Response Agent": 25000
}

print("=" * 50)
print("Baseline AI Pipeline")
print("=" * 50)

total_tokens = 0

for agent, tokens in pipeline.items():
    print(f"{agent}: {tokens:,} input tokens")
    total_tokens += tokens

print("-" * 50)
print(f"Total Input Tokens: {total_tokens:,}")
print("=" * 50)