class BST:
  ''' Maintains an unbalanced binary tree of comparable elements. All nodes in
      the left subtree of a node have data smaller than the node's datum. All
      nodes in the right subtree have data greater than or equal to the node's datum.
      Interface with the tree using insert and search. '''

  def __init__(self, data):
    self.root = None
    for datum in data:
      self.insert(datum)

  def insert(self, datum):
    if not self.root:
      self.root = BSTNode(datum)
      return
    else:
      current = self.root
      while True:
        if current.datum > datum: # go left
          if current.left_child:
            current = current.left_child
          else:
            current.left_child = BSTNode(datum)
            return
        else: # go right
          if current.right_child:
            current = current.right_child
          else:
            current.right_child = BSTNode(datum)
            return

  def search(self, datum):
    if not self.root:
      print "%s not in tree after %s steps" % (datum, 0)
      return

    current = self.root
    steps = 0
    while True:
      if datum == current.datum:
        print "%s found in tree after %s steps" % (datum, steps)
        return current
      elif datum < current.datum:
        if not current.left_child:
          print "%s not in tree after %s steps" % (datum, steps)
          return
        current = current.left_child
        steps = steps + 1
      else:
        if not current.right_child:
          print "%s not in tree after %s steps" % (datum, steps)
          return
        current = current.right_child
        steps = steps + 1

  def traverse_in_order(self, current=None):
    current = current if current else self.root
    if current.left_child:
      self.traverse_in_order(current.left_child)
    current.display()
    if current.right_child:
      self.traverse_in_order(current.right_child)


class AugmentedBST(BST):
  ''' A BST augmented with the rank of each node, where the rank is the number of
      data in the tree which are <= the node's datum. '''

  def __init__(self, data):
    BST.__init__(self, data)

  def insert(self, datum):
    if not self.root:
      self.root = RankAugmentedBSTNode(datum)
      return
    else:
      current = self.root
      while True:
        if current.datum > datum: # go left
          current.increment_rank()
          if current.left_child:
            current = current.left_child
          else:
            current.left_child = RankAugmentedBSTNode(datum, current.rank - 1)
            return
        else: # go right
          if current.right_child:
            current = current.right_child
          else:
            current.right_child = RankAugmentedBSTNode(datum, current.rank + 1)
            return


class BSTNode:
  def __init__(self, datum):
    self.datum = datum

    # starts out as a leaf
    self.left_child = None
    self.right_child = None

  def display(self):
    print self.datum


class RankAugmentedBSTNode(BSTNode):
  def __init__(self, datum, rank=1):
    BSTNode.__init__(self, datum)
    self.rank = rank # how many data in the tree are <= this node's datum

  def increment_rank(self):
    self.rank = self.rank + 1

    # Also increment the rank of everything in the right subtree
    if self.right_child:
      self.right_child.increment_rank()
      if self.right_child.left_child:
        self.right_child.left_child.increment_rank()

  def display(self):
    print 'Rank %s: %s' % (self.rank, self.datum)
