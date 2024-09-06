def get_value(prev):
    if len(prev) == 0:
        return float('inf')
    return prev[0]


def get_all_lis(arr, index, prev):
    if index == 0:
        if arr[0] < get_value(prev):
            # sequences.append(prev + [arr[index]])
            return [arr[index]] + prev
        # sequences.append(prev)
        return prev

    left = []
    if arr[index] < get_value(prev):
        left = get_all_lis(arr, index - 1, [arr[index]] + prev)
    right = get_all_lis(arr, index - 1, prev)
    longest = max(left, right, key=len)
    # sequences.append(longest)
    return longest


def get_longest_increasing_subsequences(arr):
    n = len(arr)
    longest_increasing_subsequences = []

    # for each recursion stack, pass prev = [].
    longest_increasing_subsequence = get_all_lis(arr, n - 1, [])

    # get
    # result = max(longest_increasing_subsequences, key=len)
    # return result[-1:-len(result) - 1:-1]
    return longest_increasing_subsequence


print(get_longest_increasing_subsequences([10, 9, 2, 5, 3, 7, 101, 18]))
print(get_longest_increasing_subsequences([10, 20, 3, 40]))
print(get_longest_increasing_subsequences([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print(get_longest_increasing_subsequences([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(get_longest_increasing_subsequences([1]))