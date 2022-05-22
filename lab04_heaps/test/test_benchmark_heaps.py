import time
import pytest

from lab04_heaps.test.conftest import (BENCHMARK_DATASET_RANGE_UPPER, BENCHMARK_ROUNDS)
from lab04_heaps.test.util import make_random_arrays, ExtendedMaxKHeap

DATASET = make_random_arrays(110000, 110000, 1, BENCHMARK_DATASET_RANGE_UPPER, 1)[0]


@pytest.mark.benchmark(timer=time.time,
                       disable_gc=True,
                       warmup=True, )
@pytest.mark.parametrize('sample_size', range(1000, 11000, 2000))
@pytest.mark.parametrize('num_children', (2, 3, 4))
def test_benchmark_make_heap(num_children, sample_size, benchmark):
    benchmark.extra_info['friendly_name'] = 'Building a heap'
    benchmark.extra_info['series_name'] = f"{num_children}-ary heap"
    benchmark.extra_info['x_val'] = sample_size

    dataset = DATASET[:sample_size]
    result_heap = benchmark.pedantic(ExtendedMaxKHeap, (num_children, dataset), rounds=BENCHMARK_ROUNDS)
    assert result_heap.validate(0)


@pytest.mark.benchmark(timer=time.time,
                       disable_gc=True,
                       warmup=True, )
@pytest.mark.parametrize('sample_size', list(range(1000, 11000, 2000)))
@pytest.mark.parametrize('num_children', (2, 3, 4))
def test_benchmark_pop_from_heap(num_children, sample_size, benchmark):
    benchmark.extra_info['friendly_name'] = 'Extracting the top element'
    benchmark.extra_info['series_name'] = f"{num_children}-ary heap"
    benchmark.extra_info['x_val'] = sample_size

    def pop_n_elements(n: int, heap):
        for _ in range(n):
            heap.pop()

    def setup():
        test_heap = ExtendedMaxKHeap(num_children, DATASET.copy())
        assert test_heap.validate(0)
        return (sample_size, test_heap), {}

    benchmark.pedantic(pop_n_elements, setup=setup, rounds=BENCHMARK_ROUNDS)
