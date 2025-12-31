def recursive():
    def target_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    def solve(arr, i, j):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        left = 0
        if j >= arr[i]:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left + right

    print(target_sum([1, 2, 3, 1], 3))


def memoized():
    def target_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    def solve(arr, i, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if j >= arr[i]:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left + right
        return dp[i][j]

    print(target_sum([1, 2, 3, 1], 3))


recursive()
memoized()