def binary_search(item_list, target):
    """
    Will search through a sorted list for a target item by dividing sections in half
    :param item_list: Sorted list to search
    :param target: requested item
    :return: index of selected item or None
    """
    low = 0
    high = len(item_list) - 1

    while low <= high:
        mid = (low + high)
        source = item_list[mid]
        if source == target:
            return mid
        if source > target:
            high = mid - 1
        else:
            low = mid + 1
    return None
