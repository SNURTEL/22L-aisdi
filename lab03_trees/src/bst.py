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
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.key = key
        # self.value = value

    def __repr__(self):
        if self.l_child:
            l_key = self.l_child.key
        else:
            l_key = 'null'
        if self.r_child:
            r_key = self.r_child.key
        else:
            r_key = 'null'
        if self.parent:
            parent_key = self.parent.key
        else:
            parent_key = 'null'
        return f"{l_key} <= {self.key} < {r_key}  (parent: {parent_key})"


def make_bst(array) -> Node:
    """
    Builds a BST from a given array and return's its root
    :param array: An array of items supporting __le__, __ge__, __lt__, and __gt__
    :return: New BST's root node
    """
    root = Node(array[0])
    for key in array[1:]:
        bst_insert(root, key)

    return root


def bst_insert(root: Node, key) -> Node:
    """
    Creates a new node with a given key and insert's it into a BST rooted at the given node
    :param root: BST's root node
    :param key: A key for the new node
    :return: BST's root node
    """
    parent = None
    current = root

    while current:
        parent = current

        if key <= current.key:
            current = current.l_child
        else:
            current = current.r_child

    new_node = Node(key)
    new_node.parent = parent

    if key < parent.key:
        parent.l_child = new_node
    else:
        parent.r_child = new_node

    return root


def bst_find(root: Node, key) -> Node:  # should this be wrapped in a try / except?
    """
    Searches for a node with a particular key in the BST rooted at a given node. Throws an exception if nothing was found
    :param root: BST's root node
    :param key: A key to search for
    :return: A node with a matching key (if the tree contains duplicates, the closest node to the root will be returned)
    """
    current = root
    while current.key != key:
        if key < current.key:
            current = current.l_child
        else:
            current = current.r_child

    return current


def bst_delete(root: Node, key) -> None:
    """
    Deletes a node with a particular key from the BST rooted at the given node
    :param root: BST's root node
    :param key: A key indicating which node should be deleted (a matching node will be searched for using bst_find())
    """
    to_delete = bst_find(root, key)

    if to_delete.l_child:
        if to_delete.r_child:
            next = to_delete.r_child
            while next.l_child:
                next = next.l_child

            to_delete.key = next.key  # other attributes would have to be rewritten as well

            bst_delete(next, next.key)

        else:
            transfer_data(to_delete.l_child, to_delete)
    elif to_delete.r_child:
        transfer_data(to_delete.r_child, to_delete)
    else:
        if to_delete == root:
            del root

        if to_delete.parent.l_child == to_delete:
            to_delete.parent.l_child = None
        else:
            to_delete.parent.r_child = None


def transfer_data(source: Node, target: Node) -> None:
    """
    Transfers all data from one node to another
    :param source: Source node
    :param target: Target node
    """
    target.key = source.key
    target.l_child = source.l_child
    target.r_child = source.r_child


def bst_traverse_inorder(root: Node) -> List[Node]:
    """
    Traverses a BST in order
    :param root: BST's root node
    :return: All nodes in the BST sorted in a non-descending order
    """
    result = []
    if root:
        result = bst_traverse_inorder(root.l_child)
        result.append(root)
        result = result + bst_traverse_inorder(root.r_child)
    return result


if __name__ == '__main__':
    n = make_bst([10, 3, 12, 1, 99, 5, 7, 11, 4, 9, 0, 57, 15, 2, 13, 45, 111])

    bst_find(n, 57)

    bst_delete(n, 5)

    n1 = Node(5)
    bst_insert(n1, 3)

    bst_delete(n1, 5)

    print('aaa')
