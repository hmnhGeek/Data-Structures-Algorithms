def recursive():
    def solve(arr, i, j):
        if j == 0:
            return False
        if i == 0:
            return arr[0] == j

        left = False
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(subset_sum([1, 2, 3, 4], 9))
    print(subset_sum([1, 2, 3, 4], 5))


def memoized():
    def solve(arr, i, j, dp):
        if j == 0:
            return False
        if i == 0:
            return arr[0] == j

        if dp[i][j] is not None:
            return dp[i][j]

        left = False
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left or right
        return dp[i][j]

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([1, 2, 3, 4], 9))
    print(subset_sum([1, 2, 3, 4], 5))


recursive()
print()
memoized()