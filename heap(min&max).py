class Heap:
    def __init__(self):
        self.array = list()
        self.array.append(None)

    def insert(self, value):
        return self._insert(value)

    def _insert(self, value):
        if len(self.array) == 1:
            self.array.append(value)
            return 1
        else:
            self.array.append(value)
            node_idx = len(self.array) - 1
            p_node_idx = node_idx // 2
            heap = self.array
            while node_idx > 1 and heap[node_idx] < heap[p_node_idx]:
                heap[node_idx], heap[p_node_idx] = heap[p_node_idx], heap[node_idx]
                node_idx = p_node_idx
                p_node_idx = node_idx // 2
            return 1

    def get_child_idx(self, node_idx):
        heap = self.array
        child_idx = None
        if node_idx * 2 < len(heap):
            child_idx = node_idx * 2
            if child_idx + 1 < len(heap) and heap[child_idx] > heap[child_idx + 1]:
                child_idx += 1
        return child_idx

    def pop(self):
        return self._pop()

    def _pop(self):
        heap = self.array
        if len(heap) == 1:
            print(0)
            return 0
        elif len(heap) == 2:
            return print(heap.pop())
        else:
            ret = heap[1]
            heap[1] = heap.pop()
            node_idx = 1
            child_idx = self.get_child_idx(node_idx)
            while child_idx and heap[node_idx] > heap[child_idx]:
                heap[node_idx], heap[child_idx] = heap[child_idx], heap[node_idx]
                node_idx = child_idx
                child_idx = self.get_child_idx(node_idx)
            return print(ret)

class MaxHeap(Heap):
    
    def insert(self, value):
        return self._insert(-value)
    
    def pop(self):
        return self._pop() * -1
