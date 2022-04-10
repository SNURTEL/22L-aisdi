from src.bst import make_bst
from util.tree_grapher import TreeGrapher


if __name__ == '__main__':
    import random

    n = make_bst(random.sample(range(0, 500), 100))

    tg = TreeGrapher()
    tg.graph_tree(n)
