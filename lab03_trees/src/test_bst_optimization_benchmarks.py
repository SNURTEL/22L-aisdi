from bst import *
import pytest
import random
import time


@pytest.mark.benchmark(
    disable_gc=True,
    timer=time.time
)
def test_benchmark_find(benchmark):
    n = Node(random.randint(0, 50000))
    test_keys = random.sample(range(50000), 5000)
    for k in test_keys:
        bst_insert(n, Node(k))

    benchmark.pedantic(bst_find, (n, random.choice(test_keys)), warmup_rounds=50000, rounds=2000, iterations=100)
