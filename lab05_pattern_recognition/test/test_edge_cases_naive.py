import pytest
from .conftest import BENCHMARKED_FUNCTIONS
from ..src.findN import find_n


@pytest.mark.parametrize('search_function', BENCHMARKED_FUNCTIONS)
def test_empty_string(search_function):
    assert search_function("", "aba") == []
    assert search_function("aba", "") == []
    assert search_function("", "") == []


@pytest.mark.parametrize('search_function', BENCHMARKED_FUNCTIONS)
def test_pattern_equals_text(search_function):
    assert search_function("word", "word") == [0]


@pytest.mark.parametrize('search_function', BENCHMARKED_FUNCTIONS)
def test_pattern_longer_than_text(search_function):
    assert search_function("longword", "word") == []


@pytest.mark.parametrize('search_function', BENCHMARKED_FUNCTIONS)
def test_pattern_not_in_text(search_function):
    assert search_function("word", "doesntexist") == []


NAIVE_TEST_DATA = [
    ("aba", "kaba", [1]),  # (pattern, text, expected)
    ("word", "longword", [4]),
    ("w", "wwww", [0, 1, 2, 3]),
    ("wa", "wawawa", [0, 2, 4]),
    ("ala", "alala", [0, 2]),
    ("aa", "aaab", [0, 1])
]


@pytest.mark.parametrize('test_data', NAIVE_TEST_DATA)
def test_naive(test_data):
    pattern, text, expected = test_data
    assert find_n(pattern, text) == expected
