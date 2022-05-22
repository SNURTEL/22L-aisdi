from lab03_trees.src import AVLNode
from lab03_trees.src.avl import make_avl
from lab03_trees.util.tree_grapher import TreeGrapher


def main():
    tree = make_avl([4, 3, 7, 1, 5, 9, 2, 6, 8, 10])
    tg = TreeGrapher()
    tg.graph_tree(tree)


if __name__ == "__main__":
    main()
