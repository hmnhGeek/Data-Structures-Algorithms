def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n)
    """

    def solve(arr, index, target):
        if target == 0:
            return 0
        if index == 0:
            return target//arr[0] if target % arr[0] == 0 else 1e6
        left = 1e6
        if arr[index] <= target:
            left = 1 + solve(arr, index, target - arr[index])
        right = solve(arr, index - 1, target)
        return min(left, right)

    def min_coins(arr, k):
        n = len(arr)
        ans = solve(arr, n - 1, k)
        return ans if ans != 1e6 else -1

    print(min_coins([1, 2, 3], 7))
    print(min_coins([1], 0))
    print(min_coins([12, 1, 3], 4))
    print(min_coins([2, 1], 11))
    print(min_coins([1, 2, 5], 11))
    print(min_coins([2], 3))
    print(min_coins([1,], 0))
    print(min_coins([25, 10, 5], 30))
    print(min_coins([9, 6, 5, 1], 19))
    print(min_coins([5, 1], 0))
    print(min_coins([4, 6, 2], 5))


def memoized():
    """
        Time complexity is O(n * target) and space complexity is O(n + n * target).
    """

    def solve(arr, index, target, dp):
        if target == 0:
            return 0
        if index == 0:
            return target//arr[0] if target % arr[0] == 0 else 1e6
        if dp[index][target] is not None:
            return dp[index][target]
        left = 1e6
        if arr[index] <= target:
            left = 1 + solve(arr, index, target - arr[index], dp)
        right = solve(arr, index - 1, target, dp)
        dp[index][target] = min(left, right)
        return dp[index][target]

    def min_coins(arr, k):
        n = len(arr)
        dp = {i: {j: None for j in range(k + 1)} for i in range(n)}
        ans = solve(arr, n - 1, k, dp)
        return ans if ans != 1e6 else -1

    print(min_coins([1, 2, 3], 7))
    print(min_coins([1], 0))
    print(min_coins([12, 1, 3], 4))
    print(min_coins([2, 1], 11))
    print(min_coins([1, 2, 5], 11))
    print(min_coins([2], 3))
    print(min_coins([1,], 0))
    print(min_coins([25, 10, 5], 30))
    print(min_coins([9, 6, 5, 1], 19))
    print(min_coins([5, 1], 0))
    print(min_coins([4, 6, 2], 5))


recursive()
print()
memoized()