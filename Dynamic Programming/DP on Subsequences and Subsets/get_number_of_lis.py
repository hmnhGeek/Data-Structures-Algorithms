def get_num_longest_increasing_subsequence(arr):
    n = len(arr)
    counts = {i: 1 for i in range(n)}
    dp = {i: 1 for i in range(n)}

    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev] and dp[prev] + 1 > dp[i]:
                dp[i] = dp[prev] + 1
                counts[i] = counts[prev]
            elif arr[i] > arr[prev] and dp[prev] + 1 == dp[i]:
                counts[i] += counts[prev]

    longest_increasing_length = max(dp.values())
    num_lis = 0
    for i in range(n):
        if dp[i] == longest_increasing_length:
            num_lis += counts[i]
    return num_lis


print(get_num_longest_increasing_subsequence([50, 3, 90, 60, 80]))
print(get_num_longest_increasing_subsequence([3, 7, 4, 6]))
print(get_num_longest_increasing_subsequence([5, 7, 2, 3]))
print(get_num_longest_increasing_subsequence([2, 2, 2, 2, 2]))
print(get_num_longest_increasing_subsequence([1, 3, 5, 4, 7]))