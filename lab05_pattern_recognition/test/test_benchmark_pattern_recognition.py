import pytest
import time

from .conftest import BENCHMARKED_FUNCTIONS, BENCHMARK_SAMPLE_SIZES, TEST_FILE_PATH
from lab05_pattern_recognition.util import regex_find


@pytest.mark.benchmark(
    timer=time.time,
    disable_gc=True,
    warmup=True,
)
@pytest.mark.parametrize('num_words', BENCHMARK_SAMPLE_SIZES)
@pytest.mark.parametrize('search_function', BENCHMARKED_FUNCTIONS)
def test_benchmark_pattern_recognition(num_words, search_function, benchmark):
    text = load_test_file(TEST_FILE_PATH)
    words_to_find = text[:num_words]

    def search_for_first_n_words():
        return [search_function(pattern, text) for pattern in words_to_find]

    expected_result = [regex_find(pattern, text) for pattern in words_to_find]

    search_result = benchmark.pedantic(search_for_first_n_words, rounds=5)
    assert search_result == expected_result


def load_test_file(filepath):
    with open(filepath, mode='r', encoding='utf-8') as fp:
        words = fp.readlines()
    return '\n'.join(words)
