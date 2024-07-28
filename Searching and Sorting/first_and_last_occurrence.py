# Problem link - https://www.naukri.com/code360/problems/first-and-last-position-of-an-element-in-sorted-array_1082549

def get_occurrence(arr, k):
    '''Overall time complexity is O(log(n)) and space complexity is O(1).'''

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        # update low and high which track the first occurrence
        if arr[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1

    # if first occurrence was not found, no need to find last as well.
    if low == -1:
        return low, low

    # if first occurrence is found, initialize last occurrence index
    # with the low value.
    last = low

    # iterate in the list till arr[last] is k.
    while last < len(arr) and arr[last] == k:
        last += 1

    # once either of the condition in the while fails,
    # last will be on one index forward position.
    # Decrement its value by 1.
    last -= 1

    # return first and last occurrences.
    return low, last


print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 2))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 6))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 8))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 13))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 11))
print(get_occurrence([2, 4, 6, 6, 8, 8, 8, 11, 13, 13, 15], 15))
