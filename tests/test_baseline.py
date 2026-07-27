from part1_token_optimization.baseline import pipeline

def test_pipeline_exists():
    assert len(pipeline) == 4

def test_total_tokens():
    assert sum(pipeline.values()) == 100000