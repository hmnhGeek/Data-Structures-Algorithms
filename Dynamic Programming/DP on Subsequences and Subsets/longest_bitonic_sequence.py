def get_length_of_longest_increasing_sequence(arr):
    n = len(arr)
    dp = {i: 1 for i in range(n)}

    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev] and 1 + dp[prev] > dp[i]:
                dp[i] = 1 + dp[prev]

    return dp


def get_longest_bitonic_sequence(arr):
    n = len(arr)
    dp1 = get_length_of_longest_increasing_sequence(arr)
    dp2 = get_length_of_longest_increasing_sequence(arr[-1:-len(arr)-1:-1])
    lengths = {i: dp1[i] + dp2[i] - 1 for i in range(n)}
    return max(lengths.values())


print(get_longest_bitonic_sequence([1, 2, 1, 2, 1]))
print(get_longest_bitonic_sequence([1, 2, 1, 3, 4]))