# For fun, Quick Sort

def quick_sort(array):
  if len(array) <= 1:
    # base case
    return array

  pivot_index = len(array)/2 # floored
  pivot = array[pivot_index]

  i = 0
  j = len(array)-1

  while i <= j:
    # Find i,j such that array[i] and array[j]
    # are on the wrong side of the pivot
    while array[i] < pivot:
      i = i + 1
    while array[j] > pivot:
      j = j - 1

    if i >= j:
      # all elements are in order relative to the pivot
      break
    else:
      # swap this pair of out-of-place elements and update i,j
      array[i], array[j] = array[j], array[i]
      i = i + 1
      j = j - 1

  # recurse
  split_index = len(array)/2
  left = array[:split_index]
  right = array[split_index:]
  return quick_sort(left) + quick_sort(right)
