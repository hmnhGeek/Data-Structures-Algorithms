# Problem link - https://leetcode.com/problems/count-number-of-nice-subarrays/description/
# Solution - https://www.youtube.com/watch?v=j_QOv9OT9Og&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=10


def count_less_than_equal_to(arr, k):
    # Time complexity is O(N) and space complexity is O(1).
    # This code is exactly same as that of binary_subarray_sum.py.
    if k < 0:
        return 0
    i, j, count = 0, 0, 0
    n = len(arr)
    s = 0

    while j < n:
        # The difference is that instead of a binary array, we convert the value to 1 or a 0 based on modulo check.
        s += (arr[j] % 2)
        while s > k:
            # same modulo check here.
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
