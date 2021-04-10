from DoublyLinkedList import Node, DoublyLinkedList

a = Node({'a': 'b'})
b = Node('c')
c = Node(4)
d = Node(3)
e = Node(['d', 'e'])

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
e.previous_node = d
d.previous_node = c
c.previous_node = b
b.previous_node = a

ll = DoublyLinkedList(a)

print('LinkedList: {}.'.format(ll.view()))
print('LinkedList length: {}.'.format(ll.length()))
print('Tail value: {}.'.format(ll.tail().data))
print(ll.insert(['z', 'a'], 3))
print(ll.append(10))
print('LinkedList: {}.'.format(ll.view()))
print(ll.remove(0))
print('LinkedList: {}.'.format(ll.view()))
