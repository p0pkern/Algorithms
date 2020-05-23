def merge_sort(A):
    """
    :param A: Unsorted list to be merge sorted
    :return: Sorted list
    """
    if len(A) > 1:
        mid = len(A) // 2       # Divide the list in half
        L = A[:mid]             # Assign first half to L
        R = A[mid:]             # Assign last half to R
        i = j = k = 0

        merge_sort(L)           # Perform recursive sort until len(L) = 1
        merge_sort(R)           # Perform recursive sort until Len(R) = 1

        while i < len(L) and j < len(R): # Initial sort
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L): # Clean up for leftover values L
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R): # Clean up for leftover values R
            A[k] = R[j]
            j += 1
            k += 1
    return A

print(merge_sort([9,5,2,4,5,7,6,3,2,3,45,6,7,8,8,4,356,7,86,39]))