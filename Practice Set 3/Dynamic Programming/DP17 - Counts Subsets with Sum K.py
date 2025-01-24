def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, i, j):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        left = 0
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left + right

    def count(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """

    def solve(arr, i, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left + right
        return dp[i][j]

    def count(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


recursive()
print()
memoized()