class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class Doublelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create_doublell(self, nodevalue):
        node = Node(nodevalue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        print( 'the DLL is created')

    def insertnode(self, nodevalue, location):
        if self .head is None:
            print('this node cannot be inserted')
        else:
            new_node = Node(nodevalue)
            if location == 1:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == -1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location-1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node

    def traverseDLL(self):
        if self.head is None:
            print('there is not any element to traverse')
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next

    def reverse_traverseDLL(self):
        if self.head is None:
            print('there is not any element to traverse')
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev

    def searchDLL(self, nodevalue):
        if self.head is None:
            print('there is not any element to the list ')
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == nodevalue:
                    return temp_node.value
                temp_node = temp_node.next
            print('the node does not exist in the list')

    def deleteDLL(self):
        if self.head is None:
            print('there is not any element in Dll')
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node= temp_node.next
            self.head = None
            self.tail = None
            print('the DLL has been deleted')

DLL = Doublelinkedlist()
DLL.create_doublell(5)
print([node.value for node in DLL])
DLL.insertnode(0, 1)
DLL.insertnode(2, -1)
DLL.insertnode(3, -1)
DLL.insertnode(10, 2)
# DLL.traverseDLL()
DLL.reverse_traverseDLL()

print([node.value for node in DLL])
print(DLL.searchDLL(10))
print(DLL.deleteDLL())



