from lab03_trees.src import Node


class AVLNode(Node):

    def __init__(self, key):
        self.height = 1
        super().__init__(key)

    def get_r_child_height(self):
        if self.r_child:
            return self.r_child.height
        return 0

    def get_l_child_height(self):
        if self.l_child:
            return self.l_child.height
        return 0

    def recalculate_height(self):
        parent = self
        while parent:
            parent.height = 1 + max(parent.get_l_child_height(),
                                    parent.get_r_child_height())
            parent = parent.parent

    def get_balance_factor(self):
        return self.get_r_child_height() - self.get_l_child_height()

    def rotate_right(self):
        t1 = self.l_child.l_child
        t23 = self.l_child.r_child
        t4 = self.r_child
        new_root_key = self.l_child.key
        self.r_child = AVLNode(self.key)
        self.r_child.parent = self
        self.key = new_root_key
        self.l_child = t1
        self.r_child.l_child = t23
        self.r_child.r_child = t4
        if t1:
            t1.parent = self
        if t23:
            t23.parent = self.r_child
        if t4:
            t4.parent = self.r_child
        self.r_child.recalculate_height()

    def rotate_left(self):
        t1 = self.l_child
        t23 = self.r_child.l_child
        t4 = self.r_child.r_child
        new_root_key = self.r_child.key
        self.l_child = AVLNode(self.key)
        self.l_child.parent = self
        self.key = new_root_key
        self.r_child = t4
        self.l_child.r_child = t23
        self.l_child.l_child = t1
        if t1:
            t1.parent = self.l_child
        if t23:
            t23.parent = self.l_child
        if t4:
            t4.parent = self
        self.l_child.recalculate_height()

    def balance(self):
        parent = self
        while parent:
            if parent.r_child or parent.l_child:
                balance_factor = parent.get_balance_factor()
                if balance_factor >= 2:
                    if parent.r_child.get_balance_factor() <= -1:
                        parent.r_child.rotate_right()
                    parent.rotate_left()
                elif balance_factor <= -2:
                    if parent.l_child.get_balance_factor() >= 1:
                        parent.l_child.rotate_left()
                    parent.rotate_right()
            parent = parent.parent


def make_avl(array) -> AVLNode:
    """
    Builds an AVL from a given array and returns its root
    :param array: An array of items supporting __le__, __ge__, __lt__, and __gt__
    :return: New BST's root node
    """
    if len(array) == 0:
        raise AttributeError("Cannot create a tree from an empty list")

    root = AVLNode(array[0])
    for key in array[1:]:
        root.insert(key)

    return root
