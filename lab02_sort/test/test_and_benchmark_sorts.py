import pytest
import random
import time

from .conftest import (BENCHMARKED_FUNCTIONS, CONTROL_REPS, SAMPLE_RANGE_LOWER,
                       SAMPLE_RANGE_UPPER, NUM_SAMPLES, BENCHMARK_SAMPLE_SIZES,
                       TEST_FILE_PATH)
# region randomized control runs


# alternatively, this can be parametrized with generated datasets
@pytest.mark.parametrize("sorting_function", BENCHMARKED_FUNCTIONS)
def test_control_runs(sorting_function):
    test_data = get_test_datasets()
    for unsorted, expected_result in test_data:
        assert sorting_function(unsorted) == expected_result


def get_test_datasets():
    return [build_single_dataset() for _ in range(CONTROL_REPS)]


def build_single_dataset():
    randomized_data = random.sample(
        range(SAMPLE_RANGE_LOWER, SAMPLE_RANGE_UPPER), NUM_SAMPLES)
    sorted_data = list(sorted(randomized_data.copy()))
    return randomized_data, sorted_data

# endregion


# region benchmarking
@pytest.mark.benchmark(
    timer=time.time,
    disable_gc=True,
    warmup=True,  # produces unreliable results
)
@pytest.mark.parametrize('num_words', BENCHMARK_SAMPLE_SIZES)
@pytest.mark.parametrize('sorting_function', BENCHMARKED_FUNCTIONS)
def test_benchmark_the_tadeusz(num_words, sorting_function, benchmark):
    unsorted = load_the_tadeusz(TEST_FILE_PATH)[:num_words]
    expected_result = list(sorted(unsorted.copy()))

    sort_result = benchmark.pedantic(sorting_function, [unsorted], rounds=5)
    assert sort_result == expected_result


def load_the_tadeusz(filepath):
    with open(filepath, mode='r', encoding='utf-8') as fp:
        words = [word for line in [line.split(' ')
                 for line in fp.readlines()] for word in line]
    return words
# endregion
