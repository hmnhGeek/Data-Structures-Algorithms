def get_less_than_equal_to_sum(arr, k):
    # Time complexity is O(N) and space complexity is O(1).

    if k < 0:
        return 0
    i, j = 0, 0
    n = len(arr)
    count = 0
    sum_ = 0

    # while the j pointer is within bounds
    while j < n:
        # add current jth value
        sum_ += arr[j]

        # shrink the window from left until sum becomes equal to or less than k.
        while sum_ > k:
            sum_ -= arr[i]
            i += 1

        # number of sub arrays between this i and j would be equal to the window size; add them to the count.
        count += (j - i + 1)

        # expand the window to the right
        j += 1

    # return count
    return count


def get_binary_sum(arr, k):
    return get_less_than_equal_to_sum(arr, k) - get_less_than_equal_to_sum(arr, k - 1)


print(get_binary_sum([1, 0, 1, 1, 0, 1], 2))
print(get_binary_sum([0, 0, 0, 0, 0], 0))
print(get_binary_sum([1, 0, 1, 0, 1], 2))
print(get_binary_sum([1, 0, 1, 1, 1, 0, 1], 3))
