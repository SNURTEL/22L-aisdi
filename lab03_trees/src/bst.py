from __future__ import annotations
from abc import abstractmethod
from typing import List


class Node:
    """
    Class representing a node in a binary search tree
    """
    def __init__(self, key):
        """
        Inits class Node
        :param key: Node's key
        """
        self.l_child: Node = None
        self.r_child: Node = None
        self.parent: Node = None
        self.key = key
        # self.value = value

    def __repr__(self):
        l_key = self.l_child.key if self.l_child else "null"
        r_key = self.r_child.key if self.r_child else "null"
        parent_key = self.parent.key if self.parent else "null"
        return f"{l_key} <= {self.key} < {r_key}  (parent: {parent_key})"

    def insert(self, key) -> Node:
        """
        Creates a new node with a given key and inserts it into a BST rooted at the given node
        :param key: A key for the new node
        :return: BST's root node
        """
        parent = None
        current = self

        while current:
            parent = current

            if key <= current.key:
                current = current.l_child
            else:
                current = current.r_child

        new_node = type(self)(key)
        new_node.parent = parent

        if key < parent.key:
            parent.l_child = new_node
        else:
            parent.r_child = new_node

        parent.recalculate_height()

        return self

    def find(self, key) -> Node:  # should this be wrapped in a try / except?
        """
        Searches for a node with a particular key in the BST rooted at a given node. Throws an exception if nothing was found
        :param key: A key to search for
        :return: A node with a matching key (if the tree contains duplicates, the closest node to the root will be returned)
        """
        current = self
        while current.key != key:
            if key < current.key:
                current = current.l_child
            else:
                current = current.r_child

        return current

    def delete(self, key) -> None:
        """
        Deletes a node with a particular key from the BST rooted at the given node
        :param key: A key indicating which node should be deleted (a matching node will be searched for using bst_find())
        """
        to_delete = self.find(key)

        if to_delete.l_child and to_delete.r_child:
            next = to_delete.r_child
            while next.l_child:
                next = next.l_child

            to_delete.key = next.key  # other attributes would have to be rewritten as well
            if not next.r_child and not next.l_child:
                del next
            else:
                next.delete(next.key)
        elif to_delete.l_child and not to_delete.r_child:
            transfer_data(to_delete.l_child, to_delete)
        elif to_delete.r_child:
            transfer_data(to_delete.r_child, to_delete)
        else:
            if to_delete.parent.l_child == to_delete:
                to_delete.parent.l_child = None
            else:
                to_delete.parent.r_child = None
        if to_delete.parent:
            to_delete.parent.recalculate_height()

    def traverse_inorder(self) -> List[Node]:
        """
        Traverses a BST in order
        :return: All nodes in the BST sorted in a non-descending order
        """
        result: list = []
        if self:
            if self.l_child:
                result = self.l_child.traverse_inorder()
            result.append(self)
            if self.r_child:
                result = result + self.r_child.traverse_inorder()
        return result

    @abstractmethod
    def recalculate_height(self):
        pass


def transfer_data(source: Node, target: Node) -> None:
    """
    Transfers all data from one node to another
    :param source: Source node
    :param target: Target node
    """
    target.key = source.key
    target.l_child = source.l_child
    target.r_child = source.r_child


def make_bst(array) -> Node:
    """
    Builds a BST from a given array and return's its root
    :param array: An array of items supporting __le__, __ge__, __lt__, and __gt__
    :return: New BST's root node
    """
    root = Node(array[0])
    for key in array[1:]:
        root.insert(key)

    return root


if __name__ == '__main__':
    n = make_bst([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])

    n.find(57)

    n.delete(5)

    n1 = Node(5)

    n1.insert(3)

    n1.delete(5)

    print('aaa')
