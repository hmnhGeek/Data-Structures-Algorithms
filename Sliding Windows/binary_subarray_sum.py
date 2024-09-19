def get_less_than_equal_to_sum(arr, k):
    if k < 0:
        return 0
    i, j = 0, 0
    n = len(arr)
    count = 0
    sum_ = 0

    while j < n:
        sum_ += arr[j]

        while sum_ > k:
            sum_ -= arr[i]
            i += 1

        count += (j - i + 1)
        j += 1
    return count


def get_binary_sum(arr, k):
    return get_less_than_equal_to_sum(arr, k) - get_less_than_equal_to_sum(arr, k - 1)


print(get_binary_sum([1, 0, 1, 1, 0, 1], 2))
print(get_binary_sum([0, 0, 0, 0, 0], 0))
print(get_binary_sum([1, 0, 1, 0, 1], 2))
print(get_binary_sum([1, 0, 1, 1, 1, 0, 1], 3))
