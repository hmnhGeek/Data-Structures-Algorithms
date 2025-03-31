# Problem link - https://leetcode.com/problems/subarrays-with-k-different-integers/description/
# Solution - https://www.youtube.com/watch?v=7wYGbV_LsX4&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=11


def get_distincts(mp):
    count = 0
    for i in mp:
        if mp[i] > 0:
            count += 1
    return count


def get_less_than_equal_to(arr, k):
    # This function is again similar to what is written in binary_subarray_sum.py. The basic idea is to count
    # all the subarrays in which we have the number of distinct elements <= k.

    # The time complexity would be O(N^2) and space would be O(N) because `get_distincts()` function would iterate
    # N times to find the elements whose count > 0. This can be optimized. The space will be O(N) to store each element
    # in the `mp` dictionary.

    if k < 0:
        return 0
    i, j, count = 0, 0, 0
    n = len(arr)
    distinct_count = 0
    mp = {i: 0 for i in arr}

    while j < n:
        mp[arr[j]] += 1

        while get_distincts(mp) > k:
            mp[arr[i]] -= 1
            i += 1

        distinct_count += (j - i + 1)
        j += 1

    return distinct_count


def get_k_distinct(arr, k):
    return get_less_than_equal_to(arr, k) - get_less_than_equal_to(arr, k - 1)


print(get_k_distinct([1, 2, 1, 2, 3], 2))
print(get_k_distinct([1, 2, 1, 3, 4], 3))
print(get_k_distinct([2, 1, 2, 1, 6], 2))
print(get_k_distinct([1, 2, 3, 4, 5], 1))