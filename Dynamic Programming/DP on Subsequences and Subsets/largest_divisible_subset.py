def divisible_nums(x, y):
    if x is None or y is None:
        return True
    return x % y == 0 or y % x == 0


def solve_for_largest_divisible_subset(arr, index, largest_divisible_subset, prev_value):
    if index == 0:
        if divisible_nums(arr[0], prev_value):
            largest_divisible_subset += [arr[0]]
        return largest_divisible_subset

    left = []
    if divisible_nums(arr[index], prev_value):
        left = solve_for_largest_divisible_subset(arr, index - 1, largest_divisible_subset + [arr[index]], arr[index])
    right = solve_for_largest_divisible_subset(arr, index - 1, largest_divisible_subset, prev_value)
    largest_divisible_subset = max(left, right, key=len)
    return largest_divisible_subset


def get_largest_divisible_subset(arr):
    n = len(arr)
    copy = [i for i in arr]
    copy.sort()
    largest_divisible_subset = []
    return solve_for_largest_divisible_subset(copy, n - 1, largest_divisible_subset, None)


print(get_largest_divisible_subset([1, 16, 7, 8, 4]))
print(get_largest_divisible_subset([1, 2, 5]))
print(get_largest_divisible_subset([3, 3, 3]))
print(get_largest_divisible_subset([2, 4, 3, 8]))