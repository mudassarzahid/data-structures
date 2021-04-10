class Node():
  def __init__(self, data):
    self.data = data
    self.previous_node = None
    self.next_node = None


class DoublyLinkedList():
  def __init__(self, head=None):
    self.head = head

  def length(self):
    count = 0
    runner = self.head
    while runner:
      runner = runner.next_node
      count += 1
    return count

  def view(self):
    string = ''
    runner = self.head
    while runner:
      string += "({})".format(runner.data)
      runner = runner.next_node
      if runner:
        string += ' <--> '
    return string

  def tail(self):
    runner = self.head
    while runner.next_node:
      runner = runner.next_node
    return runner

  def insert(self, data, position=0):
    # edge case: negative position
    if position < 0:
      return 'Invalid position!'

    new_node = Node(data)

    # insert at head, default
    if position == 0:
      old_head = self.head
      self.head = new_node
      old_head.previous_node = new_node
      new_node.next_node = old_head

    # insert elsewhere
    else:
      following_node = self.head
      for i in range(position):
        previous_node = following_node
        if previous_node == None:
          return 'Invalid position!'
        following_node = following_node.next_node

      previous_node.next_node = new_node
      new_node.previous_node = previous_node
      new_node.next_node = following_node
      following_node.previous_node = new_node

    return "Inserted node with value = {} at position = {}.".format(data, position)

  def append(self, data):
    new_node = Node(data)
    old_tail = self.tail()
    old_tail.next_node = new_node
    new_node.previous_node = old_tail

    return "Appended node with value = {} to DoublyLinkedList.".format(data)

  def remove(self, position=0):
     # edge case: negative position
    if position < 0:
      return 'Invalid position!'

    # remove head, default
    if position == 0:
      previous_node = self.head
      previous_node.data = self.head.data
      if self.head.next_node:
        self.head = self.head.next_node
        self.head.previous_node = None
      else:
        self.head = None

    # remove elsewhere
    else:
      following_node = self.head
      for i in range(position):
        previous_node = following_node
        if following_node.next_node == None:
          return 'Invalid position!'
        following_node = following_node.next_node

      previous_node.next_node = following_node.next_node
      following_node.previous_node = previous_node

    return "Removed node at position {} (value = {}).".format(position, previous_node.data)
