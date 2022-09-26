class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def remove_node(self, data_target):
        current_node = self.head
        if current_node is not None:
            if current_node.data == data_target:
                self.head = current_node.next  
                current_node = None
                return

        while current_node is not None:
            if current_node.data == data_target:
                break
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return None

        prev.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        
    def get_size(self):
        current_node = self.head 
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

singly = SinglyLinkedList()