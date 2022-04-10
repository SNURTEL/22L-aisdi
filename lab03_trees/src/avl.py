from bst import Node


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
        self = self
        z: AVLNode = self.l_child
        t23 = z.r_child
        z.r_child = self
        self.l_child = t23
        z.parent = self.parent
        self.parent = z
        self.recalculate_height()
        z.recalculate_height()
        return z

    def rotate_left(self):
        self = self
        new_root: AVLNode = self.r_child
        t23 = new_root.l_child
        new_root.l_child = self
        self.r_child = t23
        new_root.parent = self.parent
        self.parent = new_root
        self.recalculate_height()
        new_root.recalculate_height()
        return new_root

    def balance(self):
        balance_factor = self.get_balance_factor()
        if balance_factor >= 2:
            if self.r_child.get_balance_factor() <= 0:
                self.r_child = self.r_child.rotate_right()
            self = self.rotate_left()
        elif balance_factor <= -2:
            if self.l_child.get_balance_factor() >= 0:
                self.l_child = self.l_child.rotate_left()
            self = self.rotate_right()
        return self

    def insert(self, key):
        super().insert(key)
        self = self.balance()
        return self

