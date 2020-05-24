def rec_binary_search(item_list, target, low=0, high=None, source=None, mid=None):
    """
    Recursive version of the binary search algorithm
    :param item_list: List to search from
    :param target: Target item to find
    :return: target item index
    """
    if len(item_list) == 1 or source == target:
        if source == target:
            return mid
        else:
            return None
    if high is None:                #Sets the initial values of high and mid
        high = len(item_list)-1
        mid = (low + high)
        return rec_binary_search(item_list, target, low, high=mid-1, source=item_list[mid], mid=mid)
    if low <= high:
        if source > target:
            mid = (low + high)
            return rec_binary_search(item_list, target, low, high=mid-1, source=item_list[mid], mid=mid)
        else:
            mid = (low + high)
            return rec_binary_search(item_list, target, low=mid+1, high=high, source=item_list[mid], mid=mid)


print(rec_binary_search([1,2,3,4,5], 4))