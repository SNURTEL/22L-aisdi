from copy import copy
from lab03_trees.src.bst import Node, transfer_data


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
        while parent.parent:
            parent.height = 1 + max(parent.get_l_child_height(),
                                    parent.get_r_child_height())
            parent = parent.parent

    def get_balance_factor(self):
        return self.get_r_child_height() - self.get_l_child_height()

    def rotate_right(self):
        old_self = copy(self)
        new_root: AVLNode = old_self.l_child
        t23 = new_root.r_child
        new_root.r_child = old_self
        old_self.l_child = t23
        new_root.parent = old_self.parent
        old_self.parent = new_root
        old_self.recalculate_height()
        new_root.recalculate_height()
        transfer_data(new_root, self)

    def rotate_left(self):
        old_self = copy(self)
        new_root: AVLNode = old_self.r_child
        t23 = new_root.l_child
        new_root.l_child = old_self
        old_self.r_child = t23
        new_root.parent = old_self.parent
        old_self.parent = new_root
        old_self.recalculate_height()
        new_root.recalculate_height()
        transfer_data(new_root, self)

    def balance(self):
        balance_factor = self.get_balance_factor()
        if balance_factor >= 2:
            if self.r_child.get_balance_factor() <= 0:
                self.r_child.rotate_right()
            self.rotate_left()
        elif balance_factor <= -2:
            if self.l_child.get_balance_factor() >= 0:
                self.l_child.rotate_left()
            self.rotate_right()

    def insert(self, key):
        super().insert(key)
        self = self.balance()

    def delete(self, key):
        super().delete(key)
        self = self.balance()


def make_avl(array) -> AVLNode:
    """
    Builds an AVL from a given array and returns its root
    :param array: An array of items supporting __le__, __ge__, __lt__, and __gt__
    :return: New BST's root node
    """
    root = AVLNode(array[0])
    for key in array[1:]:
        root.insert(key)

    return root
