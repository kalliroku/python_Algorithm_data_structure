class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.cnt = 0
        self.head = None
        self.tail = self.head
    
    def insert(self, value):
        new_node = Node(value)
        if not self.cnt:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.cnt += 1
    
    def retrival(self):
        if self.cnt:
            node = self.head
            while node:
                print(node.value)
                node = node.next
        else:
            print("DLL에 노드가 없습니다.")
    
    def search_forward(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            else:
                node = node.next
        return False

    def search_backward(self, value):
        node = self.tail
        while node:
            if node.value == value:
                return node
            else:
                node = node.prev
        return False
    
    def insert_before(self, value, next_value):
        if not self.cnt:
            insert(value)
        else:
            next_node = self.search_forward(next_value)
            if next_node:
                new_node = Node(value)
                prev_node = next_node.prev
                prev_node.next = new_node
                new_node.prev = prev_node
                next_node.prev = new_node
                new_node.next = next_node
                self.cnt += 1
            else:
                return False

    def insert_after(self, value, prev_value):
        if not self.cnt:
            insert(value)
        else:
            prev_node = self.search_forward(prev_value)
            if prev_node:
                new_node = Node(value)
                next_node = prev_node.next
                prev_node.next = new_node
                new_node.prev = prev_node
                next_node.prev = new_node
                new_node.next = next_node
                self.cnt += 1
            else:
                return False
            
            
    def __len__(self):
        return self.cnt
