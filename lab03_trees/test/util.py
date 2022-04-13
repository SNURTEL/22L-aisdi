import random
from lab03_trees.src import Node, AVLNode
from .conftest import (BST_RANDOM_RANGE_LOWER, BST_RANDOM_RANGE_UPPER,
                       BST_RANDOM_NUM_SAMPLES, BST_RANDOM_NUM_DATASETS)


def make_random_datasets(make_func, num_samples=BST_RANDOM_NUM_SAMPLES):
    return [(make_func(keys), keys) for keys in
            [random.sample(range(BST_RANDOM_RANGE_LOWER, BST_RANDOM_RANGE_UPPER), num_samples)
             for _ in range(BST_RANDOM_NUM_DATASETS)]]


def assert_is_tree_valid(root: Node):
    inorder = root.traverse_inorder()
    assert inorder == sorted(inorder, key=(lambda n: n.key))
    if isinstance(root, AVLNode):
        assert -1 <= root.get_balance_factor() <= 1
