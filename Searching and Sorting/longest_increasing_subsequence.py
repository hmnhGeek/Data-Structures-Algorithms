def binary_search(arr, elem):
    """

    :param arr: array in which the element is to be searched
    :param elem: integer that needs to be searched in the array
    :return: the index from the array of that element which is either equal to or just greater than this element
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(low + (high - low)/2)
        if arr[mid] >= elem:
            high = mid - 1
        else:
            low = mid + 1
    return low

