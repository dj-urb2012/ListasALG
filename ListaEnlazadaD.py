class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.next = next
        self.data = data
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get_size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend_node(self, data):
        new_node = Node(data)
        if self.get_size() == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def remove_first(self):
        head = self.head
        if self.get_size() == 0:
            return
        elif self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = head.next
            self.head.prev = None
            head.next = None

    def remove_last(self):
        tail = self.tail
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = tail.prev
            self.tail.next = None
            tail = None

    def iterate_from_beg(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def iterate_from_end(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev

doubly = DoublyLinkedList()