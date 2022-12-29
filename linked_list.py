class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_with_value(self, data):
        self.size -= 1
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert(self, index, data):
        self.size += 1
        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        i = 0
        while current:
            if i == index - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            i += 1


    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def get_size(self):
        return self.size

