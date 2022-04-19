import random

import pytest

from .conftest import (MIN_RANDOM_ARRAY_LENGTH,
                       MAX_RANDOM_ARRAY_LENGTH,
                       MIN_RANDOM_ARRAY_VALUE,
                       MAX_RANDOM_ARRAY_VALUE,
                       RANDOM_ARRAY_COUNT,
                       MIN_RANDOM_CHILDREN_COUNT,
                       MAX_RANDOM_CHILDREN_COUNT)

from lab04_heaps.test.util import ExtendedMaxKHeap, make_random_arrays
from lab04_heaps.src.heap import HeapError


@pytest.mark.parametrize('array', make_random_arrays(MIN_RANDOM_ARRAY_LENGTH,
                                                     MAX_RANDOM_ARRAY_LENGTH,
                                                     MIN_RANDOM_ARRAY_VALUE,
                                                     MAX_RANDOM_ARRAY_VALUE,
                                                     RANDOM_ARRAY_COUNT))
def test_build_heap(array):
    children_count = random.randint(MIN_RANDOM_CHILDREN_COUNT, MAX_RANDOM_CHILDREN_COUNT)
    h = ExtendedMaxKHeap(children_count, list(array))
    try:
        h.validate(0)
    except AssertionError as e:
        print(f"SOURCE ARRAY: {array}")
        print(f"HEAP: {h.array}\nNUM CHILDREN: {h._children_count}")
        raise e


@pytest.mark.parametrize('array', make_random_arrays(MIN_RANDOM_ARRAY_LENGTH,
                                                     MAX_RANDOM_ARRAY_LENGTH,
                                                     MIN_RANDOM_ARRAY_VALUE,
                                                     MAX_RANDOM_ARRAY_VALUE,
                                                     RANDOM_ARRAY_COUNT))
def test_insert_into_heap(array):
    children_count = random.randint(MIN_RANDOM_CHILDREN_COUNT, MAX_RANDOM_CHILDREN_COUNT)
    h = ExtendedMaxKHeap(children_count, array)
    root = h.array[0]
    extracted_val = h.extract()
    h.validate(0)
    assert extracted_val == root


@pytest.mark.parametrize('array', make_random_arrays(MIN_RANDOM_ARRAY_LENGTH,
                                                     MAX_RANDOM_ARRAY_LENGTH,
                                                     MIN_RANDOM_ARRAY_VALUE,
                                                     MAX_RANDOM_ARRAY_VALUE,
                                                     RANDOM_ARRAY_COUNT))
def test_extract_from_heap(array):
    children_count = random.randint(MIN_RANDOM_CHILDREN_COUNT, MAX_RANDOM_CHILDREN_COUNT)
    h = ExtendedMaxKHeap(children_count, array)
    h.insert(random.randint(MIN_RANDOM_ARRAY_VALUE, MAX_RANDOM_ARRAY_VALUE))
    h.validate(0)


@pytest.mark.parametrize('children_count', list(range(MIN_RANDOM_CHILDREN_COUNT, MAX_RANDOM_CHILDREN_COUNT)))
def test_extract_from_empty_heap(children_count):
    h = ExtendedMaxKHeap(children_count)
    with pytest.raises(HeapError):
        h.extract()


def test_zero_children():
    with pytest.raises(HeapError):
        h = ExtendedMaxKHeap(0)


@pytest.mark.parametrize('array', make_random_arrays(MIN_RANDOM_ARRAY_LENGTH,
                                                     MAX_RANDOM_ARRAY_LENGTH,
                                                     MIN_RANDOM_ARRAY_VALUE,
                                                     MAX_RANDOM_ARRAY_VALUE,
                                                     RANDOM_ARRAY_COUNT))
def test_unary_heap_build(array):
    h = ExtendedMaxKHeap(1, array)
    h.validate(0)
    assert h.array == sorted(array, reverse=True)


@pytest.mark.parametrize('array', make_random_arrays(MIN_RANDOM_ARRAY_LENGTH,
                                                     MAX_RANDOM_ARRAY_LENGTH,
                                                     MIN_RANDOM_ARRAY_VALUE,
                                                     MAX_RANDOM_ARRAY_VALUE,
                                                     RANDOM_ARRAY_COUNT))
def test_unary_heap_insert(array):
    h = ExtendedMaxKHeap(1, array)
    root = h.array[0]
    extracted_val = h.extract()
    h.validate(0)
    assert extracted_val == root


@pytest.mark.parametrize('array', make_random_arrays(MIN_RANDOM_ARRAY_LENGTH,
                                                     MAX_RANDOM_ARRAY_LENGTH,
                                                     MIN_RANDOM_ARRAY_VALUE,
                                                     MAX_RANDOM_ARRAY_VALUE,
                                                     RANDOM_ARRAY_COUNT))
def test_unary_heap_extract(array):
    h = ExtendedMaxKHeap(1, array)
    h.insert(random.randint(MIN_RANDOM_ARRAY_VALUE, MAX_RANDOM_ARRAY_VALUE))
    h.validate(0)
