class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createcsll(self,nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return 'the CSLL has been created'

    def insertcsll(self, value, location):
        if self.head is None:
            return 'the head reference is none'
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def traversecsll(self):
        if self.head is None:
            print('there is not any element for traverse')
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break


csll = CSLinkedList()
print(csll.createcsll(1))
csll.insertcsll(0, 0)
csll.insertcsll(1, 1)
csll.insertcsll(2, 1)
csll.insertcsll(4, 2)

print([node.value for node in csll])
csll.traversecsll()


