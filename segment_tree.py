# 세그먼트 트리
import math


class SegmentTree:
    def __init__(self, array):
        self.array = [0] + array
        self.len_array = len(self.array) - 1
        self.tree = [0] * pow(2, math.ceil(math.log2(self.len_array))+1)
        self.make_tree(1, 1, self.len_array)

    def make_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.array[start]
        else:
            self.tree[node] = self.make_tree(node*2, start, (start+end)//2) + self.make_tree(node*2+1, (start+end)//2+1, end)
        return self.tree[node]

    def __sum(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        elif left <= start and end <= right:
            return self.tree[node]
        else:
            left_sum = self.__sum(node*2, start, (start+end)//2, left, right)
            right_sum = self.__sum(node*2+1, (start+end)//2+1, end, left, right)
            return left_sum + right_sum

    def __update(self, node, start, end, index, diff):
        if index < start or index > end: return 0
        self.tree[node] += diff
        if start != end:
            self.__update(node*2, start, (start+end)//2, index, diff)
            self.__update(node*2+1, (start+end)//2+1, end, index, diff)

    def find_sum(self, left, right):
        return self.__sum(1, 1, self.len_array, left+1, right+1)

    def update(self, index, value):
        try:
            index += 1
            old_value = self.array[index]
            different = value - old_value
            self.array[index] = value
            self.__update(1, 1, self.len_array, index, different)
            return 1
        except KeyError as e:
            print(e)
            return 0


# import random
#
# seg_nums = set()
# while len(seg_nums) != 100:
#     seg_nums.add(random.randint(0, 999))
# print(seg_nums)
