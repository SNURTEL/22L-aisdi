import pytest
import random

from lab03_trees.src import Node, make_bst

from .conftest import BST_RANDOM_RANGE_LOWER, BST_RANDOM_RANGE_UPPER, BST_RANDOM_NUM_SAMPLES, BST_RANDOM_NUM_DATASETS, \
    BST_INVALID_FIND_TEST_ITERATIONS


def make_random_datasets(num_samples=BST_RANDOM_NUM_SAMPLES):
    return [(make_bst(keys), keys) for keys in
            [random.sample(range(BST_RANDOM_RANGE_LOWER, BST_RANDOM_RANGE_UPPER), num_samples)
             for _ in range(BST_RANDOM_NUM_DATASETS)]]


def assert_is_tree_valid(root: Node):
    inorder = root.traverse_inorder()
    assert inorder == sorted(inorder, key=(lambda n: n.key))


@pytest.mark.parametrize('bst_and_keys', make_random_datasets())
def test_insert_make_random_bsts(bst_and_keys):
    bst, keys = bst_and_keys
    assert_is_tree_valid(bst)


@pytest.mark.parametrize('bst_and_keys', make_random_datasets())
def test_bst_find(bst_and_keys):
    bst, keys = bst_and_keys
    key = random.choice(keys)
    found = bst.find(key)
    assert found.key == key


@pytest.mark.parametrize('bst_and_keys', make_random_datasets(BST_INVALID_FIND_TEST_ITERATIONS))
def test_bst_find_non_existent(bst_and_keys):
    bst, keys = bst_and_keys
    invalid_key = random.choice([x for x in range(BST_RANDOM_RANGE_LOWER, BST_RANDOM_RANGE_UPPER) if x not in keys])
    with pytest.raises(AttributeError):  # should this be a KeyError?
        bst.find(invalid_key)


def test_bst_delete_leaf():
    n = make_bst([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])
    n.find(45)
    n.delete(45)
    with pytest.raises(AttributeError):
        n.find(45)
    assert_is_tree_valid(n)


def test_bst_delete_with_single_child():
    n = make_bst([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])
    n.find(7)

    n.delete(7)
    with pytest.raises(AttributeError):
        n.find(7)
    assert_is_tree_valid(n)


def test_bst_delete_intermediate():
    n = make_bst([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])
    n.find(5)

    n.delete(5)
    with pytest.raises(AttributeError):
        n.find(5)
    assert_is_tree_valid(n)


def test_bst_delete_root_single_child():
    n = make_bst((5, 3))
    n.find(5)

    n.delete(5)
    with pytest.raises(AttributeError):
        n.find(5)
    assert_is_tree_valid(n)


@pytest.mark.xfail  # this will not work in Python!
def test_bst_delete_root_no_children():
    n = make_bst((17,))
    n.find(17)

    n.delete(17)
    with pytest.raises(AttributeError):
        n.find(17)
    with pytest.raises(AssertionError):
        assert_is_tree_valid(n)


def test_delete_root_two_children():
    n = make_bst([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])
    n.find(10)

    n.delete(10)
    with pytest.raises(AttributeError):
        n.find(10)
    assert_is_tree_valid(n)
