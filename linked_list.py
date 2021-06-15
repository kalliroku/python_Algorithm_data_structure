class LinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.cnt = 0
        self.root_node = None

    def push(self, value):
        if not self.cnt:
            self.root_node = LinkedListNode(value)
        else:
            node = self.root_node
            while node.next_node:
                node = node.next_node
            node.next_node = LinkedListNode(value)
        self.cnt += 1

    def remove(self, value):
        if not self.cnt:
            print("LinkedList is empty")
        else:    
            p_node = None
            node = self.root_node
            while node:
                if node.value == value:
                    break
                p_node = node
                node = node.next_node
            if node:
                if p_node:
                    p_node.next_node = node.next_node
                else:
                    self.root_node = node.next_node
                node.next_node = None
                self.cnt -= 1
                del node
                return 1
            else:
                print(f"can't find value: {{value}} in LinkedList")
                return 0

    def search(self, value):
        if not self.cnt:
            print("LinkedList is empty")
        else:
            node = self.root_node
            while node:
                if node.value == value:
                    break
                else:
                    node = node.next_node
            if node:
                return True
            else:
                return False

    def __len__(self):
        return self.cnt

    def retrive(self):
        node = self.root_node
        while node:
            print(node.value)
            node = node.next_node
        print()
