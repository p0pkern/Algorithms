def find_smallest(arr):
    """
    Takes in the array and returns the smallest item.
    :param arr: array
    :return: smallest item index
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    """
    Sorts a list by adding the values in order to a new list.
    :param arr: array
    :return: sorted list
    """
    new_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array

