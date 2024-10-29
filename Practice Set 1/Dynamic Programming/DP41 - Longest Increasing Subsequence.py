def recursive():
    def solve(arr, index, prev):
        if index < 0:
            return 0

        left = 0
        if arr[index] < prev:
            left = 1 + solve(arr, index - 1, arr[index])
        right = solve(arr, index - 1, prev)
        return max(left, right)

    def longest_increasing_subsequence(arr):
        n = len(arr)
        return solve(arr, n - 1, 1e6)

    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(longest_increasing_subsequence([1, 2, 2]))


def memoized():
    def solve(arr, index, prev, dp):
        if index == 0:
            return 0

        if dp[index][prev] is not None:
            return dp[index][prev]

        left = 0
        if arr[index - 1] < prev:
            left = 1 + solve(arr, index - 1, arr[index - 1], dp)
        right = solve(arr, index - 1, prev, dp)
        dp[index][prev] = max(left, right)
        return dp[index][prev]

    def longest_increasing_subsequence(arr):
        n = len(arr)
        maxval = max(arr)
        dp = {i: {j: None for j in arr} for i in range(n + 1)}
        for i in dp:
            dp[i][maxval + 1] = None

        return solve(arr, n - 1, maxval + 1, dp)

    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(longest_increasing_subsequence([1, 2, 2]))


recursive()
print()
memoized()