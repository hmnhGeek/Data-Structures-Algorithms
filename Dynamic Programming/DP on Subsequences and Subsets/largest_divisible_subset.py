def divisible_nums(x, y):
    if x is None or y is None:
        return True
    return x % y == 0 or y % x == 0


def solve_for_largest_divisible_subset(arr, index, largest_divisible_subset, prev_value):
    # The time complexity of this solution is O(2^n) and space would be O(n + n) {one extra `n` for largest subset arr}.

    # if you've reached index 0
    if index == 0:
        # check if 0th index element and previous value are divisible or not.
        if divisible_nums(arr[0], prev_value):
            # if yes, then add the 0th element to the largest subset
            largest_divisible_subset += [arr[0]]
        # finally, return the largest subset
        return largest_divisible_subset

    # assuming left recursion is not possible
    left = []
    # however, if array element at this index and previous value are divisible, then do a left recursion
    if divisible_nums(arr[index], prev_value):
        # do a left recursion by going to one lower index, adding the current element into the largest subset and
        # updating the prev_value to current element.
        left = solve_for_largest_divisible_subset(arr, index - 1, largest_divisible_subset + [arr[index]], arr[index])

    # do a right recursion by simply avoiding the current index element into the largest subset and keep the same
    # prev_value
    right = solve_for_largest_divisible_subset(arr, index - 1, largest_divisible_subset, prev_value)

    # finally, update the largest subset with the max list obtained from the left or right recursion and return it.
    largest_divisible_subset = max(left, right, key=len)
    return largest_divisible_subset


def get_largest_divisible_subset(arr):
    n = len(arr)
    # create a copy of the original array to avoid changing the input array
    copy = [i for i in arr]
    # sort the copied array
    copy.sort()

    # solve the problem starting from last index using recursion
    return solve_for_largest_divisible_subset(copy, n - 1, [], None)


print(get_largest_divisible_subset([1, 16, 7, 8, 4]))
print(get_largest_divisible_subset([1, 2, 5]))
print(get_largest_divisible_subset([3, 3, 3]))
print(get_largest_divisible_subset([2, 4, 3, 8]))