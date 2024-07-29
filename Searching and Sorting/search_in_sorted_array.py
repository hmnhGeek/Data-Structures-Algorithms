def check_in_rotated_sorted(arr, target):
    # The time complexity is still O(log(n)) as its just a binary search
    # with only a slight modification to the reduction of search space.
    # Space complexity is O(1).

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)

        if arr[mid] == target:
            return mid

        # check if left part is sorted
        if arr[low] <= arr[mid]:
            # left part is indeed sorted
            if arr[low] <= target <= arr[mid]:
                # if target lies in the left sorted part, reduce high value
                high = mid - 1
            else:
                # target is not in the sorted left part.
                low = mid + 1

        # check if the right part is sorted
        elif arr[mid] <= arr[high]:
            if arr[mid] <= target <= arr[high]:
                # target lies in the right sorted part
                low = mid + 1
            else:
                # target does not lie in the right sorted part.
                high = mid - 1

    return low if arr[low] == target else -1


print(check_in_rotated_sorted([8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7], 9))
print(check_in_rotated_sorted([8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7], 11))
print(check_in_rotated_sorted([7, 8, 9, 1, 2, 3, 4, 5, 6], 11))
print(check_in_rotated_sorted([7, 8, 9, 1, 2, 3, 4, 5, 6], 9))