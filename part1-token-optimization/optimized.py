# optimized.py

baseline = {
    "Planner Agent": 25000,
    "Retriever Agent": 25000,
    "Reasoning Agent": 25000,
    "Final Response Agent": 25000
}

optimized = {
    "Planner Agent": 6000,
    "Retriever Agent": 3500,
    "Reasoning Agent": 4500,
    "Final Response Agent": 4000
}

print("=" * 60)
print("Token Optimization Results")
print("=" * 60)

before = sum(baseline.values())
after = sum(optimized.values())

for agent in baseline:
    print(
        f"{agent:<25} "
        f"Before: {baseline[agent]:>6,} "
        f"After: {optimized[agent]:>6,}"
    )

print("-" * 60)
print(f"Total Before : {before:,}")
print(f"Total After  : {after:,}")

reduction = ((before - after) / before) * 100

print(f"Reduction    : {reduction:.2f}%")

print("\nOptimizations Used")
print("-------------------")
print("1. Retrieval Chunking")
print("2. Conversation Summarization")