def rec_list_count(arr, count=0):
    """
    Counts how many items are in a list.
    :param arr: List to be counted
    :param count: Current count
    :return: total count
    """
    if len(arr) == 0:
        return count
    else:
        return rec_list_count(arr[1:], count + 1)
