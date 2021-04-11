from LinkedList import Node, LinkedList

a = Node({'a': 'b'})
b = Node('c')
c = Node(4)
d = Node(3)
e = Node(['d', 'e'])

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

ll = LinkedList(a)


print('LinkedList: {}.'.format(ll.view()))
print('LinkedList length: {}.'.format(ll.length()))
print('Tail value: {}.'.format(ll.tail().data))
print(ll.insert(['z', 'a'], 3))
print(ll.append(10))
print('LinkedList: {}.'.format(ll.view()))
print(ll.remove())
print('LinkedList: {}.'.format(ll.view()))
