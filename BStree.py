# bst in python

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.val = key
        self._left = None
        self._right = None
        self.parent = None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if self._right is not None:
            self._right.parent = None
        if node:
            node.parent = self
        self._right = node

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if self._left is not None:
            self._left.parent = None
        if node:
            node.parent = self
        self._left = node

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self._left is None and self._right is None

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def has_both_children(self):
        return self.has_left_child() and self.has_right_child()

    def has_any_children(self):
        return self.has_left_child() and self.has_right_child()

    def get_succ(self):
        succ = None
        if self.right:
            succ = self.right
        while succ.left:
            succ = succ.left
        return succ

    def move_child(self):
        child = self.right if self.has_right_child() else None
        self.right = None
        if self.is_left_child():
            self.parent.left = child
        elif self.is_right_child():
            self.parent.right = child

    def display(self):
        if self is None:
            return 0
        else:
            if self.has_left_child():
                self.left.display()
            print(self.key)
            if self.has_right_child():
                self.right.display()


class BinarySearchTree:
    def __init__(self):
        self.count = 0
        self.root = None

    def insert(self, key):

        if not self.count:
            self.root = TreeNode(key)
        else:
            node = TreeNode(key)
            self.__insert(node)
        self.count += 1

    def __insert(self, node):
        point = self.root
        while True:
            if node.key < point.key:
                if point.has_left_child():
                    point = point.left
                else:
                    point.left = node
                    break
            else:
                if point.has_right_child():
                    point = point.right
                else:
                    point.right = node
                    break

    def search(self, key):
        if self.root is not None:
            res = self.__search(key)
            if res:
                return res.val
        else:
            return 0

    def __search(self, key):
        res = self.root
        while res:
            if key == res.key:
                return res
            else:
                if key < res.key:
                    res = res.left
                else:
                    res = res.right
        return res

    def delete(self, key):
        if self.count == 1 and key == self.root.key:
            self.root = None
            self.count = 0
            return
        else:
            target_del_node = self.__search(key)
            if target_del_node:
                self.count -= 1
                if target_del_node.is_leaf():
                    a = target_del_node.parent.left
                    b = target_del_node
                    if a == b:
                        target_del_node.parent.left = None
                    else:
                        target_del_node.parent.right = None
                elif target_del_node.has_both_children():
                    succ = target_del_node.get_succ()
                    succ.move_child()
                    succ.left = target_del_node.left
                    succ.right = target_del_node.right
                    if target_del_node.is_root():
                        self.root = succ
                    else:
                        if target_del_node.is_left_child:
                            target_del_node.parent.left = succ
                        else:
                            target_del_node.parent.right = succ
                else:
                    child = target_del_node.left if target_del_node.has_left_child() \
                        else target_del_node.right
                    target_del_node.left = None
                    target_del_node.right = None
                    if target_del_node.is_root():
                        self.root = child
                    else:
                        a = target_del_node.parent.left
                        b = target_del_node
                        if a == b:
                            target_del_node.parent.left = child
                        else:
                            target_del_node.parent.right = child
                del target_del_node
                return 1
            else:
                return 0

    def display(self, key=None):
        if self.count:
            if not key:
                self.root.display()
            else:
                self.search(key).display()

    def find_max_node(self):
        target_node = self.root
        while target_node.right:
            target_node = target_node.right
        return target_node

    def find_min_node(self):
        target_node = self.root
        while target_node.left:
            target_node = target_node.left
        return target_node

    def del_m(self, x):
        if self.count == 1:
            self.root = None
            self.count = 0
            return
        if self.count:
            if x == -1:
                target_del_node = self.find_min_node()
            else:
                target_del_node = self.find_max_node()
            self.count -= 1
            if target_del_node.is_leaf():
                a = target_del_node.parent.left
                b = target_del_node
                if a == b:
                    target_del_node.parent.left = None
                else:
                    target_del_node.parent.right = None
            elif target_del_node.has_both_children():
                succ = target_del_node.get_succ()
                succ.move_child()
                succ.left = target_del_node.left
                succ.right = target_del_node.right
                if target_del_node.is_root():
                    self.root = succ
                else:
                    a = target_del_node.parent.left
                    b = target_del_node
                    if a == b:
                        target_del_node.parent.left = succ
                    else:
                        target_del_node.parent.right = succ
            else:
                child = target_del_node.left if target_del_node.has_left_child() \
                    else target_del_node.right
                target_del_node.left = None
                target_del_node.right = None
                if target_del_node.is_root():
                    self.root = child
                else:
                    a = target_del_node.parent.left
                    b = target_del_node
                    if a == b:
                        target_del_node.parent.left = child
                    else:
                        target_del_node.parent.right = child
            del target_del_node
            return 1
        else:
            return 0

    def show_result(self):
        if self.count:
            print(self.find_max_node().key, self.find_min_node().key)
        else:
            print("EMPTY")
        # print("----------------------------------------")


def main():
    tree = BinarySearchTree()
    a = [3, 1, 4, -1, 0, 3, 5]
    for i in a:
        tree.insert(i)
    for _ in range(3):
        tree.del_m(1)
        tree.del_m(-1)
    tree.show_result()
    for j in a:
        tree.insert(j)
    for _ in range(8):
        tree.del_m(-1)
    tree.show_result()
    for j in a:
        tree.insert(j)
    for _ in range(8):
        tree.del_m(1)
    tree.show_result()
