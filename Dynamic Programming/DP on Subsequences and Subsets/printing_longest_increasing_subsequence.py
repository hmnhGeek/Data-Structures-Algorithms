# Problem link - https://www.geeksforgeeks.org/construction-of-longest-increasing-subsequence-using-dynamic-programming/
# Solution - https://www.youtube.com/watch?v=IFfYfonAFGc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=43


def get_front_value_from(prev):
    if len(prev) == 0:
        return float('inf')
    return prev[0]


def get_all_lis(arr, index, prev):
    # if you've reached index 0, there are 2 options:
    # 1. if arr[0] is less than the front value in prev, then you can add arr[0] to front of prev and return
    # 2. if not, then simply return whatever is there in prev.
    if index == 0:
        if arr[0] < get_front_value_from(prev):
            return [arr[index]] + prev
        return prev

    # initially assume that we cannot consider arr[index] into the prev
    left = []
    if arr[index] < get_front_value_from(prev):
        # if the arr[index] is less than front value of prev, prepend it to prev and recurse on next index.
        left = get_all_lis(arr, index - 1, [arr[index]] + prev)

    # do not consider arr[index] in prev, simply recurse on next index with same prev.
    right = get_all_lis(arr, index - 1, prev)

    # return the array with larger size.
    return max(left, right, key=len)


def get_longest_increasing_subsequences(arr):
    # Time complexity is O(2^n) and space complexity is O(n) for the longest increasing subsequence.
    n = len(arr)
    # for each recursion stack, pass prev = [].
    return get_all_lis(arr, n - 1, [])


print(get_longest_increasing_subsequences([10, 9, 2, 5, 3, 7, 101, 18]))
print(get_longest_increasing_subsequences([10, 20, 3, 40]))
print(get_longest_increasing_subsequences([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print(get_longest_increasing_subsequences([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(get_longest_increasing_subsequences([1]))