# Selection sort - faster then bubble sort
# O(N * N)

class SelectionSort(object):

  def swap(self, array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

  def sort(self, array):
    for i in range(len(array) - 1): # -1 т.к. не нужно проверять last
      index = i

      for j in range(i + 1, len(array), 1):
        if array[index] > array[j]: # ищем min item левее i
          index = j

      if index != i:
        self.swap(array, index, i)

    return array

if __name__ == '__main__':

  unsortedArray = [1, -122, 33, 0, 33, 55, 98, 2222]

  selectionSort = SelectionSort()
  sortedArray = selectionSort.sort(unsortedArray)

  print(sortedArray)



