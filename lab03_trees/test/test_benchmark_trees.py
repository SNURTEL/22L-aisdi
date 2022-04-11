import time
import pytest
import random
from lab03_trees.src.avl import make_avl
from lab03_trees.src.bst import make_bst
from lab03_trees.test.conftest import BENCHMARK_DATASET_RANGE_UPPER, BENCHMARK_DATASET_SAMPLE_SIZE, BENCHMARK_MAKE_FUNCTIONS, BENCHMARK_SAMPLE_SIZES


def generate_random_dataset():
    return random.sample(range(1, BENCHMARK_DATASET_RANGE_UPPER), BENCHMARK_DATASET_SAMPLE_SIZE)


DATASET = generate_random_dataset()

@pytest.mark.benchmark(
    timer=time.time,
    disable_gc=True,
    warmup=True,
)
@pytest.mark.parametrize('num_elements', BENCHMARK_SAMPLE_SIZES)
@pytest.mark.parametrize('make_function', BENCHMARK_MAKE_FUNCTIONS)
def test_benchmark_make_tree(num_elements, make_function, benchmark):
    benchmark.extra_info['friendly_name'] = 'Tree creation'
    benchmark.extra_info['function'] = make_function.__name__
    benchmark.extra_info['num_elements'] = num_elements

    keys = DATASET[:num_elements]
    benchmark.pedantic(make_function, [keys], rounds=5)


def find_n_elements(tree, num_elements):
    for i in range(num_elements):
        tree.find(DATASET[i])


@pytest.mark.benchmark(
    timer=time.time,
    disable_gc=True,
    warmup=True,
)
@pytest.mark.parametrize('num_elements', BENCHMARK_SAMPLE_SIZES)
@pytest.mark.parametrize('make_function', BENCHMARK_MAKE_FUNCTIONS)
def test_benchmark_find(num_elements, make_function, benchmark):
    def setup():
        tree = make_function(DATASET)
        return (tree, num_elements), {}

    benchmark.extra_info['friendly_name'] = 'Finding an element'
    benchmark.extra_info['function'] = make_function.__name__
    benchmark.extra_info['num_elements'] = num_elements

    benchmark.pedantic(find_n_elements, setup=setup, rounds=5)


def delete_n_elements(tree, num_elements):
    for i in range(num_elements):
        tree.delete(DATASET[i])


@pytest.mark.benchmark(
    timer=time.time,
    disable_gc=True,
    warmup=True,
)
@pytest.mark.parametrize('num_elements', BENCHMARK_SAMPLE_SIZES)
@pytest.mark.parametrize('make_function', BENCHMARK_MAKE_FUNCTIONS)
def test_benchmark_delete(num_elements, make_function, benchmark):
    def setup():
        tree = make_function(DATASET)
        return (tree, num_elements), {}

    benchmark.extra_info['friendly_name'] = 'Deleting an element'
    benchmark.extra_info['function'] = make_function.__name__
    benchmark.extra_info['num_elements'] = num_elements

    benchmark.pedantic(delete_n_elements, setup=setup, rounds=5)
