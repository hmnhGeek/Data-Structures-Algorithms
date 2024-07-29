# Problem link - https://www.naukri.com/code360/problems/rotated-array_1093219

def is_increasing_order(arr, low, mid, high):
    return arr[low] <= arr[mid] <= arr[high]


def is_decreasing_order(arr, low, mid, high):
    return arr[low] >= arr[mid] >= arr[high]


def min_in_rotated_sorted(arr):
    '''
        Overall time complexity is O(log(n)) and space is O(1).

        However, if there are majority duplicate elements, the time complexity
        can be O(n).

        ALGORITHM
        1. If array is blank, return None
        2. If array has only one element, return arr[0]
        3. If array has two elements, return min(arr)
        4. Initialize low and high as 0 and n-1
        5. If low <= high, move to step 6 else move to step
        6. Calculate mid.
        7. Check if low, mid and high are same. If yes, move to step 8, else step 9.
        8. Reduce the search space and continue by incrementing low and decrementing high.
        9. If array is sorted in decreasing order, return arr[high].
        10. If array is sorted in increasing order, return arr[low].
        11. Check if mid or mid + 1 could be minimum or not.
        12. Otherwise, minimum will always lie in the unsorted part.
        13. If left part is sorted, update low to mid + 1.
        14. If right part is sorted, update high to mid - 1.
        15. Go to step 5.
        16. Return arr[low] because low represents the case when almost all elements are same.
    '''

    # handle the edge cases
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return min(arr)

    # if length of the array is more than 2, use binary search to find the minimum
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = int(low + (high - low)/2)

        # if there are duplicates
        if arr[low] == arr[mid] == arr[high]:
            # shrink the search space.
            low += 1
            high -= 1
            continue

        # if the entire array is sorted,
        # then the minimum will lie at the low index.
        # return it.
        if is_increasing_order(arr, low, mid, high):
            return arr[low]

        # if the entire array is in reverse order sorted,
        # then the minimum will lie at the high index.
        # return it.
        if is_decreasing_order(arr, low, mid, high):
            return arr[high]

        # if element next to mid is smaller, then you've found the minimum value at
        # index mid + 1
        if arr[mid + 1] < arr[mid]:
            return arr[mid + 1]

        # if element just before mid is greater, then the minimum value is at index mid
        elif arr[mid] < arr[mid - 1]:
            return arr[mid]

        # otherwise, minimum will always lie in the unsorted part
        if arr[low] <= arr[mid]:
            # left part is sorted, minimum must be in the right part
            low = mid + 1
        else:
            # right part is sorted, minimum must be in the left part
            high = mid - 1

    # if the array had all the values same, eg: [3,3,3,3,3], in that case,
    # at some point high < low. Simply return low value.
    return arr[low]


print(min_in_rotated_sorted([3, 3, 3, 3, 1, 3]))
print(min_in_rotated_sorted([7, 8, 9, 10, 11, 12, 13, 1, 2, 3]))
print(min_in_rotated_sorted([3, 3, 3, 3, 3, 3]))
print(min_in_rotated_sorted([4]))
print(min_in_rotated_sorted([3, 2]))
print(min_in_rotated_sorted([4, 3, 3]))
print(min_in_rotated_sorted([4, 3, 2, 1]))
print(min_in_rotated_sorted([4, 5, 1, 2, 3]))
print(min_in_rotated_sorted([2, 3, 3]))