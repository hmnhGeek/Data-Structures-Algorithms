def binary_search(arr, elem):
    """

    :param arr: array in which the element is to be searched
    :param elem: integer that needs to be searched in the array
    :return: the index from the array of that element which is either equal to or just greater than this element
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] >= elem:
            high = mid - 1
        else:
            low = mid + 1
    return low


def get_longest_increasing_subsequence(arr):
    result = []
    for elem in arr:
        index_to_insert_at = binary_search(result, elem)
        if index_to_insert_at == len(result):
            result.append(elem)
        else:
            result[index_to_insert_at] = elem
    return len(result)


print(get_longest_increasing_subsequence([1, 7, 8, 4, 5, 6, -1, 9]))
print(get_longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
print(get_longest_increasing_subsequence([1, 2, 2]))
print(get_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(get_longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))
print(get_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))
