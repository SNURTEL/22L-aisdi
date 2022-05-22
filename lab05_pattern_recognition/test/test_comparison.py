from typing import List, Tuple
import random
from ..src import find_kmp, find_kr, find_n
import pytest
from .conftest import COMPARISON_DATASET_ALPHABET, COMPARISON_PATTERN_SIZES, COMPARISON_TEXT_SIZES, DATASETS_PER_SIZE


def generate_random_datasets() -> List[Tuple[str]]:
    result = []
    for n in COMPARISON_TEXT_SIZES:
        for m in COMPARISON_PATTERN_SIZES:
            if m > n:
                break
            for _ in range(DATASETS_PER_SIZE):
                text = generate_random_string_from_alphabet(n)
                pattern = generate_random_string_from_alphabet(m)
                result.append((pattern, text))
    return result


def generate_random_string_from_alphabet(n):
    result = ""
    for _ in range(n):
        result += random.choice(COMPARISON_DATASET_ALPHABET)
    return result


@pytest.mark.parametrize("dataset", generate_random_datasets())
def test_comparison(dataset):
    pattern, text = dataset
    assert find_kmp(pattern, text) == find_kr(pattern, text) == find_n(pattern, text)
