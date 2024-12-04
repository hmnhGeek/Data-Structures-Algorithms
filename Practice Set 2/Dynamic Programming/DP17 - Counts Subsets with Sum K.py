def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, target):
        if target == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == target else 0

        left = 0
        if arr[i] <= target:
            left = solve(arr, i - 1, target - arr[i])
        right = solve(arr, i - 1, target)
        return left + right

    def count(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

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
        Time complexity is O(nk) and space complexity is O(n + nk).
    """
    def solve(arr, i, target, dp):
        if target == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == target else 0

        if dp[i][target] is not None:
            return dp[i][target]

        left = 0
        if arr[i] <= target:
            left = solve(arr, i - 1, target - arr[i], dp)
        right = solve(arr, i - 1, target, dp)
        dp[i][target] = left + right
        return dp[i][target]

    def count(arr, k):
        n = len(arr)
        dp = {i: {j: None for j in range(k + 1)} for i in range(n)}
        return solve(arr, n - 1, k, dp)

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
