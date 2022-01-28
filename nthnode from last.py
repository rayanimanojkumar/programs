from removeDuplicateLL import Linkedlist


def nthnode(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


custom_ll = Linkedlist()
custom_ll.generate(10, 0, 99)
print(custom_ll)
print(nthnode(custom_ll, 3))






