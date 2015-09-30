# From Lecture 1, Algorithmic Thinking & Peak Finding

### ONE-DIMENSIONAL

def find_peak_1d(array):
  ''' Finds a peak in a one-dimensional array of comparable elements.
      The one-dimensional array should be represented as a list.
      A peak is greater than or equal to all adjacent elements.
      Returns the value of the peak. '''

  # Check for invalid input + base case
  if len(array) < 1:
    return empty_array_warning()
  elif len(array) == 1:
    return array[0]

  # Get middle element and adjacent elements
  middle_index = len(array)/2 # integer division -- floored
  left_index = middle_index - 1
  right_index = middle_index + 1

  middle_item = array[middle_index]
  left_item = array[left_index] if left_index > -1 else None
  right_item = array[right_index] if right_index < len(array) else None

  # Consider left subarray if there is definitely a peak to the left
  # If not, consider right subarray if there is definitely a peak to the right
  # Otherwise, the current middle element is a peak
  if left_item and left_item > middle_item:
    subarray = array[:middle_index]
    return find_peak_1d(subarray)
  elif right_item and right_item > middle_item:
    subarray = array[right_index:]
    return find_peak_1d(subarray)
  else:
    return middle_item


### TWO-DIMENSIONAL

def find_peak_2d(array):
  ''' Finds a peak in a two-dimensional array of comparable elements.
      The two-dimensional array should be represented as a list of lists.
      A peak is greater than or equal to all adjacent elements.
      Diagonals DO NOT count as adjacent.
      Returns the value of the peak. '''

  # Get array size
  num_rows = len(array)
  if (num_rows < 1):
    return empty_array_warning()

  num_cols = len(array[0])
  if (num_cols < 1):
    return empty_array_warning()

  # Locate global max of middle column
  middle_col_index = num_cols/2 # integer division -- floored
  middle_col = get_column(array, middle_col_index)
  middle_col_max = max(middle_col)
  middle_col_max_index = middle_col.index(middle_col_max)

  # Get elements to left and right of middle column's global max
  left_col_index = middle_col_index - 1
  right_col_index = middle_col_index + 1
  left_element = array[middle_col_max_index][left_col_index] if left_col_index > -1 else None
  right_element = array[middle_col_max_index][right_col_index] if right_col_index < num_cols else None

  # Consider left subarray if there is definitely a peak to the left
  # If not, consider right subarray if there is definitely a peak to the right
  # Otherwise, the global max of the current middle column is a peak
  if left_element and left_element > middle_col_max:
    subarray = select_columns(array, 0, middle_col_index)
    return find_peak_2d(subarray)
  elif right_element and right_element > middle_col_max:
    subarray = select_columns(array, right_col_index, num_cols)
    return find_peak_2d(subarray)
  else:
    return middle_col_max

def get_column(array, col_index):
  ''' Gets a single column from a two-dimensional array.
      The array should be represented as a list of lists. '''
  column = []
  for row in array:
    column.append(row[col_index])
  return column

def select_columns(array, start_index, stop_index):
  ''' Gets a subarray from a two-dimensional array.
      The array should be represented as a list of lists.
      Selects [start_index, stop_index) '''

  subarray = []
  for row in array:
    subarray.append(row[start_index:stop_index])
  return subarray

def empty_array_warning():
  print 'Array empty.'
  return None
