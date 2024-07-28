# Problem link - https://www.naukri.com/code360/problems/first-and-last-position-of-an-element-in-sorted-array_1082549

def get_occurrence(arr, k):
    '''Overall time complexity is O(log(n)) and space complexity is O(1).'''

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        # update low and high which track the first occurrence
        if arr[mid] >= k:
            # we need to find lower bound, so move left if you find
            # a number greater than or equal to k, otherwise move right.
            high = mid - 1
        else:
            low = mid + 1

    # if first occurrence was not found
    # or if low went outside the array,
    # no need to find last as well.
    if low >= len(arr) or arr[low] != k:
        return -1, -1

    # store the first occurrence as we are going to perform
    # another binary search to get the last occurrence by
    # resetting low and high values.
    first_occurrence = low
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        if arr[mid] <= k:
            # we need to find upper bound, so move right if you find
            # a number less than or equal to k, otherwise move left.
            low = mid + 1
        else:
            high = mid - 1

    return first_occurrence, low - 1


print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 2))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 6))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 8))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 13))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 11))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 15))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 16))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 5))
