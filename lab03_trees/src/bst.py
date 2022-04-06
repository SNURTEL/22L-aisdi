class Node:
    def __init__(self, key):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.key = key

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
        return f"{l_key} <= {self.key} < {r_key}        parent: {parent_key}"


def bst_insert(root: Node, key) -> None:
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


def bst_find(root: Node, key):  # should this be wrapped in a try / except?
    current = root
    while current.key != key:
        if key < current.key:
            current = current.l_child
        else:
            current = current.r_child

    return current


def bst_lowest(root: Node) -> Node:
    while root.l_child:
        root = root.l_child
    return root


def bst_delete(root: Node, key):  # FIXME consider deleting root with a single child
    to_delete = bst_find(root, key)

    if to_delete.l_child:
        if to_delete.r_child:
            next = to_delete.r_child
            while next.l_child:
                next = next.l_child

            to_delete.key = next.key  # other attributes would have to be rewritten as well

            bst_delete(next, next.key)

        else:
            if to_delete.parent.l_child == to_delete:
                to_delete.parent.l_child = to_delete.l_child
            else:
                to_delete.parent.r_child = to_delete.l_child

    elif to_delete.r_child:
        if to_delete.parent.l_child == to_delete:
            to_delete.parent.l_child = to_delete.r_child
        else:
            to_delete.parent.r_child = to_delete.r_child
    else:
        del to_delete


if __name__ == '__main__':
    n = Node(10)
    bst_insert(n, 3)
    bst_insert(n, 12)
    bst_insert(n, 1)
    bst_insert(n, 99)
    bst_insert(n, 5)
    bst_insert(n, 7)
    bst_insert(n, 11)
    bst_insert(n, 4)
    bst_insert(n, 9)
    bst_insert(n, 0)
    bst_insert(n, 57)
    bst_insert(n, 15)
    bst_insert(n, 2)
    bst_insert(n, 13)
    bst_insert(n, 45)
    bst_insert(n, 111)

    bst_find(n, 57)

    bst_delete(n, 5)

    print('aaa')
