# max heap logic with out node

class MaxHeap():
    blank = -int(1e15)

    def __init__(self):
        self.array = [0]
        self.element_count = 0

    def arrange_up_max_heap(self, push_element_index):
        child = push_element_index
        while child > 1:
            parent = child // 2
            if self.array[child] > self.array[parent]:
                self.array[child], self.array[parent] = self.array[parent], self.array[child]
            child = parent

    def push(self, x):
        try:
            self.array[self.element_count + 1] = x
        except IndexError:
            self.array.append(x)
        finally:
            self.element_count += 1
            self.arrange_up_max_heap(self.element_count)

    def arrange_down_max_heap(self):
        parent = 1
        child = 2
        while child <= self.element_count:
            if child < self.element_count and self.array[child] < self.array[child + 1]:
                child += 1
            if self.array[child] > self.array[parent]:
                self.array[child], self.array[parent] = self.array[parent], self.array[child]
            parent = child
            child = parent * 2

    def del_heap(self):
        if not self.element_count:
            ret = 0
        else:
            ret = self.array[1]
            self.array[1] = self.array[self.element_count]
            self.array[self.element_count] = self.blank
            self.arrange_down_max_heap()
            self.element_count -= 1
        return ret
