def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, j):
        if i == j:
            return 0
        min_cost = 1e6
        for k in range(i, j):
            cost = arr[i - 1] * arr[k] * arr[j] + solve(arr, i, k) + solve(arr, k + 1, j)
            min_cost = min(min_cost, cost)
        return min_cost

    def mcm(arr):
        n = len(arr)
        return solve(arr, 1, n - 1)

    print(mcm([10, 20, 30, 40, 50]))
    print(mcm([10, 20, 30, 40]))
    print(mcm([4, 5, 3, 2]))
    print(mcm([10, 15, 20, 25]))
    print(mcm([1, 4, 3, 2]))
    print(mcm([2, 1, 3, 4]))
    print(mcm([1, 2, 3, 4, 3]))


def memoized():
    """
        Time complexity is O(n^3) and space complexity is O(n + n^2).
    """
    def solve(arr, i, j, dp):
        if i == j:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        min_cost = 1e6
        for k in range(i, j):
            cost = arr[i - 1] * arr[k] * arr[j] + solve(arr, i, k, dp) + solve(arr, k + 1, j, dp)
            min_cost = min(min_cost, cost)
        dp[i][j] = min_cost
        return dp[i][j]

    def mcm(arr):
        n = len(arr)
        dp = {i: {j: None for j in range(1, n)} for i in range(1, n)}
        return solve(arr, 1, n - 1, dp)

    print(mcm([10, 20, 30, 40, 50]))
    print(mcm([10, 20, 30, 40]))
    print(mcm([4, 5, 3, 2]))
    print(mcm([10, 15, 20, 25]))
    print(mcm([1, 4, 3, 2]))
    print(mcm([2, 1, 3, 4]))
    print(mcm([1, 2, 3, 4, 3]))


recursive()
print()
memoized()