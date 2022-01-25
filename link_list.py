class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node: 
            yield node
            node = node.next

    def insertsll(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                    next_node = temp_node.next
                    temp_node.next = new_node
                    new_node.next = next_node
                    # if temp_node == self.tail:
                    #     self.tail = new_node




sll = SLinkedList()
sll.insertsll(1, 1)
sll.insertsll(2, 1)
sll.insertsll(3, 1)
sll.insertsll(4, 1)
sll.insertsll(0, 0)
# sll.insertsll(50, 0)
sll.insertsll(10, 2)

print([node.value for node in sll])























































# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.data,  end='-->')
#             temp = temp.next
#         print('None')
#
#     def search(self, data, head, index):
#         if head.data == data:
#             print(index)
#         else:
#             if head.next:
#                 return self.search(head.next, data, index+1)
#             else:
#                 raise ValueError('Node is not in linkedlist')
#
#     def size(self):
#         if self.head == None:
#             return 0
#         current = self.head
#         size = 0
#         while current:
#             size += 1
#             current = current.next
#         return size
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#
#
#
#
#
#
# llist = LinkedList()
# llist.head = Node('a')
# s_n = Node('b')
# t_n = Node('c')
# f_n = s_n
# s_n = t_n
# llist.print_list()





































# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print_ll(self):
#         if self.head is None:
#             print('linked list is empty')
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, '-->', end=' ')
#                 n = n.ref
#
#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node
#
#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node
#
#     def del_position(self, head, position):
#         temp = head
#         if position == 0:
#             return temp.ref
#
#         while position - 1 > 0:
#             head = head.ref
#             position -= 1
#         head.ref = head.ref.ref
#         return temp
#
#
# ll1 = LinkedList()
# ll1.add_begin(10)
# ll1.add_begin(20)
# ll1.add_begin(30)
# ll1.add_end(40)
# ll1.add_end(50)
# ll1.del_position(2)
# ll1.print_ll()













# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#
#     def insert_after(self, prev_node, new_data):
#
#         if prev_node is None:
#             print('the prev node must be in linked list ')
#             return
#         new_node = Node(new_data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node
#
#     def append(self, new_data):
#         new_node = Node(new_data)
#
#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
#
#     def printlist(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next
#
#
# if __name__ == '__main__':
#     llist = LinkedList()
#     llist.append(6)
#     llist.push(4)
#     llist.push(5)
#     llist.append(3)
#     llist.insert_after(llist.head.next, 2)
#     llist.printlist()
#
#
#
#
#
