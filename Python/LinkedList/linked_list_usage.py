from LinkedList import LinkedList, reverse_linked_list, reverse_in_parts

def build_list(l):
    L = LinkedList()

    for i in l:
        L.push(i)

    return L

ll = build_list([1, 2, 3, 4, 5])

ll.show()
print("\n\nSwapping nodes 2 and 5")
node_2 = ll.head.next
node_5 = ll.tail
ll.swap(node_2, node_5)
ll.show()
print("\n\nSwapping nodes 1 and 2")
node_1 = ll.head
node_2 = ll.tail
ll.swap(node_1, node_2)
ll.show()
print("\n\nSwapping nodes 4 and 1")
node_4 = ll.head.next.next.next
node_1 = ll.tail
ll.swap(node_4, node_1)
ll.show()
print("\n\nSwapping nodes 5 and 3")
node_5 = ll.head.next
node_3 = node_5.next
ll.swap(node_5, node_3)
ll.show()
print("\n\nSwapping nodes 2 and 3")
node_2 = ll.head
node_3 = ll.head.next
ll.swap(node_2, node_3)
ll.show()
print("\n\nSwapping nodes 3 and 4")
ll.swap(ll.head, ll.tail)
ll.show()

print("\n\nReversing list")
ll.head = reverse_linked_list(ll.head)
ll.show()

print()
print()
L2 = build_list([1,2,3,4,5,6,7,8,9,10])
reverse_in_parts(L2, 6)
L2.show()
print()
print(f"head = {L2.head.data}, tail = {L2.tail.data}")