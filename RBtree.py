# rb_tree try based on BStree in python

# 5 properties
# 1. each node is either red or black
# 2. The root node color is black
# 3. Each leaf node is black
# 4. if a node is red, its' child node are black
# 5. For each node, the simple path from that node to all its descendant leaf nodes contains the same number of black

import bstreetry
BLACK = 0
RED = 1


class RbNode(bstreetry.TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.color = RED
        # 속성 값 업데이트를 어떻게 해야 할까?? 궁금하지만 일단 패스
        self.b_height = 1

    def change_color(self):
        if self.is_root():
            self.color = BLACK
        else:
            self.color = RED if self.color == BLACK else BLACK

    @property
    def uncle(self):
        if self.parent.is_root():
            return None
        else:
            if self.parent.parent.left == self.parent:
                return self.parent.parent.right
            else:
                return self.parent.parent.left

    @property
    def grand_parent(self):
        return None if self.parent.is_root() else self.parent.parent

    @property
    def grand_grand_parent(self):
        return self.parent.gran_parent

    @property
    def sibling(self):
        if self.is_root():
            return None
        if self.is_left_child():
            return self.parent.right
        elif self.is_right_child():
            return self.parent.left

    def color_promotion(self):
        # 두 자식 노드가(있고), 모두 빨강일 경우
        if self.has_both_children() and self.left.color == RED and self.right.color == RED:
            self.color = RED
            self.left.color = BLACK
            self.right.color = BLACK
            if self.is_root():
                self.color = BLACK

    def color_demotion(self):
        pass



# class TreeNode:
#
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self._left = None
#         self._right = None
#         self.parent = None
#
#     @property
#     def right(self):
#         print(a)
#         return self._right
#
#     @right.setter
#     def right(self, node):
#         if self._right is not None:
#             self._right.parent = None
#         if node:
#             node.parent = self
#         self._right = node
#
#     @property
#     def left(self):
#         return self._left
#
#     @left.setter
#     def left(self, node):
#         if self._left is not None:
#             self._left.parent = None
#         if node:
#             node.parent = self
#         self._left = node
#
#     def is_root(self):
#         return self.parent is None
#
#     def is_leaf(self):
#         return self._left is None and self._right is None
#
#     def is_left_child(self):
#         return self.parent and self.parent.left == self
#
#     def is_right_child(self):
#         return self.parent and self.parent.right == self
#
#     def has_left_child(self):
#         return self.left is not None
#
#     def has_right_child(self):
#         return self.right is not None
#
#     def has_both_children(self):
#         return self.has_left_child() and self.has_right_child()
#
#     def has_any_children(self):
#         return self.has_left_child() and self.has_right_child()
#
#     def get_succ(self):
#         succ = None
#         if self.right:
#             succ = self.right
#         while succ.left:
#             succ = succ.left
#         return succ
#
#     def move_child(self):
#         child = self.right if self.has_right_child() else None
#         self.right = None
#         if self.is_left_child():
#             self.parent.left = child
#         elif self.is_right_child():
#             self.parent.right = child
#
#     def display(self):
#         if self is None:
#             return 0
#         else:
#             if self.has_left_child():
#                 self.left.display()
#             print(self.key)
#             if self.has_right_child():
#                 self.right.display()
class RedBlackTree(bstreetry.BinarySearchTree):
    def __init__(self):
        super().__init__()

    def insert(self, key):
        node = RbNode(key)
        if self.root is None:
            self.root = node
            node.color = BLACK
        else:
            target_node = self.root
            grand_grand_parent = grand_parent = parent = None

            # 삽입 자리를 찾을 때까지 반복문 수행
            while target_node is not None:
                # coloring 이 필요한 경우 진행,
                target_node.color_promotion()
                # double red 발생 시 rotation
                if parent is not None and parent.color == RED:
                    # key 값 기준으로 gp와 p의 비교 값이 다를 경우 double rotation
                    if key >= grand_parent != key >= parent:
                        parent = self.rotation(key, grand_parent)
                    # 같을 경우 single rotation
                    target_node = self.rotation(key, grand_grand_parent)
                    # rotation 종료 후 깔맞춤
                    grand_parent.color = RED
                    target_node.color = BLACK
                self.root.color = BLACK
                # 내려 가면서 족보 갱신
                grand_grand_parent = grand_parent
                grand_parent = parent
                parent = target_node
                # 아래 노드로 이동하고 while문 재실행
                target_node = target_node.right if key >= target_node else target_node.left

            # 트리 말단에 노드 삽입
            if key >= parent.key:
                parent.right = node
            else:
                parent.left = node
            if parent.color == RED:
                if key >= grand_parent.key != key >= parent.key:
                    parent = self.rotation(key, grand_parent)
                self.rotation(key, grand_grand_parent)
                grand_parent.color = RED
                parent.color = BLACK
        self.root.color = BLACK
        self.count += 1
        return 1

    def rotation(self, key, pivot_node):
        # case1. target_node's gp is root
        if pivot_node is None:
            child = self.root
        # case2. target_node's gp is not root
        else:
            if key >= pivot_node.key:
                child = pivot_node.right
            else:
                child = pivot_node.left
        if key >= child.key:  # right-rotation
            grand_child = child.right
            child.right = grand_child.left
            grand_child.left = child
        else:  # left-rotation
            grand_child = child.left
            child.left = grand_child.right
            grand_child.right = child
        # link rotated sub tree to pivot
        # case1. child was root node
        if pivot_node is None:
            self.root = grand_child
            grand_child.parent = None
        else:
            # case 2-1 child was right child
            if key >= pivot_node.key:
                pivot_node.right = grand_child
            # case 2-2 child was left child
            else:
                pivot_node.left = grand_child
        return grand_child

    # # 초기 작성한 방법
    # def __right_rotation(self, node):
    #     p = node.parent
    #     g = node.grand_parent
    #     u = node.uncle
    #     g.left = u
    #     if g.parent is not None:  # g != root case
    #         if g.is_left_child():
    #             g.parent.left = p
    #         elif g.is_right_child():
    #             g.parent.right = p
    #     else:
    #         self.root = p
    #     p.right = g
    #
    # def __left_rotation(self,  node):
    #     p = node.parent
    #     g = node.grand_parent
    #     u = node.uncle
    #     g.right = u
    #     if g.parent is not None:  # g != root case
    #         if g.is_left_child():
    #             g.parent.left = p
    #         elif g.is_right_child():
    #             g.parent.right = p
    #     else:
    #         self.root = p
    #     p.left = g
    #
    # def __left_right_rotation(self, node):
    #     p = node.parent
    #     g = node.grand_parent
    #     p.right = node.left
    #     g.left = node
    #     node.left = p
    #     # 회전을 하면서 node와 node.parent의 위계가 교환 됨
    #     self.__right_rotation(p)
    #
    # def __right_left_rotation(self, node):
    #     p = node.parent
    #     g = node.grand_parent
    #     p.left = node.right
    #     g.right = node
    #     node.right = p
    #     # 회전을 하면서 node와 node.parent의 위계가 교환 됨
    #     self.__left_rotation(p)

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


if __name__ == '__main__':
    main()
