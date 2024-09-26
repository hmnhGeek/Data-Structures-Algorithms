def count_less_than_equal_to(arr, k):
    if k < 0:
        return 0
    i, j, count = 0, 0, 0
    n = len(arr)
    s = 0

    while j < n:
        s += (arr[j] % 2)

        while s > k:
            s -= (arr[i] % 2)
            i += 1

        count += (j - i + 1)
        j += 1

    return count


def get_count_nice_subarrays(arr, k):
    return count_less_than_equal_to(arr, k) - count_less_than_equal_to(arr, k - 1)


print(get_count_nice_subarrays([1, 1, 2, 1, 1], 3))
print(get_count_nice_subarrays([2, 4, 6], 1))
print(get_count_nice_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
