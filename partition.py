from removeDuplicateLL import Linkedlist

def partion(ll, x):
    cur_node = ll.head
    ll.tail = ll.head
    while cur_node:
        next_node = cur_node.next
        cur_node.next = None
        if cur_node.value < x:
            cur_node.next = ll.head
            ll.head = cur_node
        else:
            ll.tail.next = cur_node
            ll.tail = cur_node
        cur_node = next_node
    if ll.tail.next is not None:
        ll.tail.next = None


custom_ll = Linkedlist()
custom_ll.generate(10, 0, 49)
print(custom_ll)
partion(custom_ll, 20)
print(custom_ll)