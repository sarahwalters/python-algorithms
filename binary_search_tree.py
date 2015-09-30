class BST:
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
        return datum
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


class BSTNode:
  def __init__(self, datum):
    self.datum = datum

    # starts out as a leaf
    self.left_child = None
    self.right_child = None
