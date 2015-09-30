# From Lecture 4, Heaps

class MaxHeap:
  ''' Maintains a nearly-complete binary tree of comparable elements which
      adheres to the max-heap property (every parent is larger than both of
      its children). The tree is stored in a list.
      Interface with the tree using insert, max, extract_max, and heap_sort. '''

  def __init__(self, data):
    self.data = ['*'] + data # '*' to shift indices by +1
    self._build_max_heap()

  def insert(self, item):
    self.data.append(item)
    self._build_max_heap()

  def max(self):
    # "peek" at the top node
    return self.data[1]

  def extract_max(self):
    # "pop" the top node.
    # -> switch top node with rightmost leaf
    # -> pop new rightmost leaf (old top node) -- this is the max
    # -> fix the top node -- everything else is still in max heap order
    self.data[1], self.data[-1] = self.data[-1], self.data[1]
    extracted_max = self.data.pop()
    if len(self.data) > 1:
      self._fix_node(1)
    return extracted_max

  def heap_sort(self):
    # "pop" top node repeatedly
    sorted_data = []
    while len(self.data) > 1:
      sorted_data.append(self.extract_max())
    return sorted_data

  def _left_child(self, index):
    left_index = 2*index
    if left_index > len(self.data) - 1:
      return None
    return self.data[left_index]

  def _right_child(self, index):
    right_index = 2*index + 1
    if right_index > len(self.data) - 1:
      return None
    return self.data[2*index + 1]

  def _swap(self, index1, index2):
    self.swaps = self.swaps + 1
    self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

  def _fix_node(self, index):
    # make sure (recursively) that the subtree rooted at index adheres
    # to the max-heap property
    swap_right = self.data[index] < self._right_child(index)
    swap_left = self.data[index] < self._left_child(index)

    while swap_left or swap_right:
      if swap_left:
        self._swap(index, 2*index)
        self._fix_node(2*index)
      elif swap_right:
        self._swap(index, 2*index + 1)
        self._fix_node(2*index + 1)

      swap_right = self.data[index] < self._right_child(index)
      swap_left = self.data[index] < self._left_child(index)

  def _build_max_heap(self):
    # fix all of the internal nodes, from right to left and bottom to top
    self.swaps = 0
    for i in range(len(self.data)/2, 0, -1):
      self._fix_node(i)

    print 'Built max heap after %s swaps' % self.swaps
    print self.data
