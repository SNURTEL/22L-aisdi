from src import make_avl
from util.tree_grapher import TreeGrapher


if __name__ == '__main__':
    import random

    n = make_avl(random.sample(range(0, 100), 100))
    h1 = n.get_l_child_height()
    h2 = n.get_r_child_height()

    tg = TreeGrapher()
    tg.graph_tree(n)
    pass
