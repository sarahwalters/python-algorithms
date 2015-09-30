# From Lecture 3, Insertion Sort & Merge Sort

class MergeSortArray:
  ''' Maintains a sorted one-dimensional array of comparable elements using merge sort.
      The one-dimensional array is represented as a list.
      Interface with the array using insert, remove, and display. '''

  def __init__(self, array):
    self.array = array
    self.split_counter = 0
    print self.__sort()

  def insert(self, element):
    self.array.append(element)
    print self.__sort()

  def remove(self, element):
    self.array.remove(element)

  def display(self):
    return self.array

  def __sort(self, array=None):
    top_level = not array
    self.split_counter = 0 if top_level else self.split_counter
    array = array if array else self.array

    if len(array) == 1:
      # Base case
      if top_level:
        print 'Sorted array in 0 splits'
      return array
    else:
      # Sort left and right subarrays and merge
      middle_index = len(array)/2
      self.split_counter = self.split_counter + 1
      left_subarray = self.__sort(array=array[:middle_index])
      right_subarray = self.__sort(array=array[middle_index:])
      merged = self.__merge(left_subarray, right_subarray)

      # If this is the outermost array, print stats
      if top_level:
        self.array = merged
        print 'Sorted array in %s splits' % self.split_counter
      return merged

  def __merge(self, arr1, arr2):
    merged = []
    len1 = len(arr1) > 0
    len2 = len(arr2) > 0

    # "Two-finger" merge algorithm
    # Works because we know both lists are sorted
    while len1 or len2:
      if (not len2) or (len1 and arr1[0] <= arr2[0]):
        merged.append(arr1.pop(0))
      else:
        merged.append(arr2.pop(0))

      len1 = len(arr1) > 0
      len2 = len(arr2) > 0

    return merged
