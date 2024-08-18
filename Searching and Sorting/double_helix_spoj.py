def get_idx_from(arr, elem):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        if arr[mid] == elem:
            return mid

        if arr[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1
    return None


def traverse(arr1, arr2, row, col):
    if row < 0:
        return float('-inf')
    if row == 0:
        return arr1[row] if col == 0 else arr2[row]

    left = traverse(arr1, arr2, row - 1, col)
    right = float('-inf')
    curr_val = arr1[row] if col == 0 else arr2[row]
    if col == 0:
        switch_idx = get_idx_from(arr2, curr_val)
    else:
        switch_idx = get_idx_from(arr1, curr_val)

    if switch_idx is not None:
        right = traverse(arr1, arr2, switch_idx - 1, 1 if col == 0 else 0)

    return curr_val + max(left, right)


def get_max_path_sum(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    return max(traverse(arr1, arr2, n1 - 1, 0), traverse(arr1, arr2, n2 - 1, 1))


print(get_max_path_sum([0, 2, 6, 7, 8, 9], [0, 2, 4, 5, 7, 9]))
print(get_max_path_sum([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))