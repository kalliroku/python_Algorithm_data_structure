import sys
import math


class SegmentTree:
    def __init__(self, array: list):
        self.list = array
        self.len_li = len(self.list)
        self.tree = [None] * pow(2, math.ceil(math.log2(self.len_li))+1)
        self.len_tree = len(self.tree)-1
        self.list = [None] + self.list
        self.__make_tree(1, 1, self.len_li)

    def __make_tree(self, position, start, end):
        if start == end:
            self.tree[position] = self.list[start]
        else:
            left_tree_sum = self.__make_tree(position*2, start, (start+end)//2)
            right_tree_sum = self.__make_tree(position*2+1, (start+end)//2+1, end)
            self.tree[position] = left_tree_sum + right_tree_sum
        return self.tree[position]

    def __update(self, position, index, start, end, diff):
        if index < start or end < index:
            return
        self.tree[position] += diff
        if start != end:
            self.__update(position*2, index, start, (start+end)//2, diff)
            self.__update(position*2+1, index, (start+end)//2+1, end, diff)

    def update(self, index, value):
        self.__update(1, index, 1, self.len_li, value - self.list[index])
        self.list[index] = value

    def __sum(self, left, right, start, end, position=1):
        if start > right or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[position]
        left_sum = self.__sum(left, right, start, (start+end)//2, position*2)
        right_sum = self.__sum(left, right, (start+end)//2+1, end, position*2+1)
        return left_sum + right_sum

    def range_sum(self, left, right):
        return self.__sum(left, right, 1, self.len_li)
