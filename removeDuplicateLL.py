
from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.head = None

    def __str__(self):
        return str(self.value)


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' --> '.join(values)

    def add(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

    def removeduplicate(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            visited = set([current_node.value])
            while current_node.next:
                if current_node.next.value in visited:
                    current_node.next = current_node.next.next
                else:
                    visited.add(current_node.next.value)
                    current_node = current_node.next
            return self


custom_ll = Linkedlist()
custom_ll.generate(10, 0, 99)
print(custom_ll)
print(custom_ll.removeduplicate())


