import pytest
import random
from lab03_trees.src import make_avl, make_avl
from lab03_trees.test.util import assert_is_tree_valid, make_random_datasets
from .conftest import BST_RANDOM_RANGE_LOWER, BST_RANDOM_RANGE_UPPER, BST_INVALID_FIND_TEST_ITERATIONS


def test_make_empty_avl():
    with pytest.raises(AttributeError):
        make_avl([])


@pytest.mark.parametrize('avls_and_keys', make_random_datasets(make_avl))
def test_insert_make_random_avls(avls_and_keys):
    avl, keys = avls_and_keys
    assert_is_tree_valid(avl)


@pytest.mark.parametrize('avls_and_keys', make_random_datasets(make_avl))
def test_avl_find(avls_and_keys):
    avl, keys = avls_and_keys
    key = random.choice(keys)
    found = avl.find(key)
    assert found.key == key


@pytest.mark.parametrize('avls_and_keys', make_random_datasets(make_avl, BST_INVALID_FIND_TEST_ITERATIONS))
def test_avl_find_non_existent(avls_and_keys):
    avl, keys = avls_and_keys
    invalid_key = random.choice([x for x in range(BST_RANDOM_RANGE_LOWER, BST_RANDOM_RANGE_UPPER) if x not in keys])
    with pytest.raises(AttributeError):  # should this be a KeyError?
        avl.find(invalid_key)


def test_avl_delete_leaf():
    n = make_avl([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])
    n.find(45)
    n.delete(45)
    with pytest.raises(AttributeError):
        n.find(45)
    assert_is_tree_valid(n)


def test_avl_delete_with_single_child():
    n = make_avl([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])
    n.find(7)

    n.delete(7)
    with pytest.raises(AttributeError):
        n.find(7)
    assert_is_tree_valid(n)


def test_avl_delete_intermediate():
    n = make_avl([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])
    n.find(5)

    n.delete(5)
    with pytest.raises(AttributeError):
        n.find(5)
    assert_is_tree_valid(n)


def test_avl_delete_root_single_child():
    n = make_avl((5, 3))
    n.find(5)

    n.delete(5)
    with pytest.raises(AttributeError):
        n.find(5)
    assert_is_tree_valid(n)


@pytest.mark.xfail  # this will not work in Python!
def test_avl_delete_root_no_children():
    n = make_avl((17,))
    n.find(17)

    n.delete(17)
    with pytest.raises(AttributeError):
        n.find(17)
    with pytest.raises(AssertionError):
        assert_is_tree_valid(n)


def test_delete_root_two_children():
    n = make_avl([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])
    n.find(10)

    n.delete(10)
    with pytest.raises(AttributeError):
        n.find(10)
    assert_is_tree_valid(n)
