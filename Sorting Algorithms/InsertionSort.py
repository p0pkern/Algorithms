def insertion_sort(n):
    """
    Basic insertion sort algorithm.
    :param n: List to be sorted.
    :return: Sorted list from least to greatest.
    """
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        while j >= 0 and n[j] > key:
            n[j + 1] = n[j]
            j = j - 1
        n[j + 1] = key
    return n

