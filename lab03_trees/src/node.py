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
