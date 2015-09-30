# From Lecture 3, Insertion Sort & Merge Sort

class InsertionSortArray:
  ''' Maintains a sorted one-dimensional array of comparable elements using insertion sort.
      The one-dimensional array is represented as a list.
      Interface with the array using insert, remove, and display. '''

  def __init__(self, array):
    self.array = array
    self.length = len(array)
    self.__sort()

  def insert(self, element):
    self.array.append(element)
    self.__sort()

  def remove(self, element):
    self.array.remove(element)

  def display(self):
    return self.array

  def __swap(self, loc1, loc2):
    self.array[loc1], self.array[loc2] = self.array[loc2], self.array[loc1]

  def __sort(self):
    num_swaps = 0
    for i, element in enumerate(self.array):
      while i > 0 and element < self.array[i-1]:
        self.__swap(i, i-1)
        num_swaps = num_swaps + 1
        i = i - 1

    print 'Sorted array in %s swaps' % num_swaps
    print self.array
