def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def min_coins(arr, target):
        n = len(arr)
        coins = solve(arr, n - 1, target)
        if coins == 1e6:
            return -1
        return coins

    def solve(arr, i, j):
        if j == 0:
            return 0
        if i == 0:
            if j % arr[0] == 0:
                return j // arr[0]
            return 1e6
        left = 1e6
        if j >= arr[i]:
            left = 1 + solve(arr, i, j - arr[i])
        right = solve(arr, i - 1, j)
        return min(left, right)

    print(min_coins([1, 2, 3], 7))
    print(min_coins([1], 0))
    print(min_coins([12, 1, 3], 4))
    print(min_coins([2, 1], 11))
    print(min_coins([1, 2, 5], 11))
    print(min_coins([2], 3))
    print(min_coins([1, ], 0))
    print(min_coins([25, 10, 5], 30))
    print(min_coins([9, 6, 5, 1], 19))
    print(min_coins([5, 1], 0))
    print(min_coins([4, 6, 2], 5))


def memoized():
    """
        Time complexity is O(n*target) and space complexity is O(n + n*target).
    """
    def min_coins(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        coins = solve(arr, n - 1, target, dp)
        if coins == 1e6:
            return -1
        return coins

    def solve(arr, i, j, dp):
        if j == 0:
            return 0
        if i == 0:
            if j % arr[0] == 0:
                return j // arr[0]
            return 1e6
        if dp[i][j] is not None:
            return dp[i][j]
        left = 1e6
        if j >= arr[i]:
            left = 1 + solve(arr, i, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = min(left, right)
        return dp[i][j]

    print(min_coins([1, 2, 3], 7))
    print(min_coins([1], 0))
    print(min_coins([12, 1, 3], 4))
    print(min_coins([2, 1], 11))
    print(min_coins([1, 2, 5], 11))
    print(min_coins([2], 3))
    print(min_coins([1, ], 0))
    print(min_coins([25, 10, 5], 30))
    print(min_coins([9, 6, 5, 1], 19))
    print(min_coins([5, 1], 0))
    print(min_coins([4, 6, 2], 5))


def tabulation():
    """
        Time complexity is O(n*target) and space complexity is O(n*target).
    """
    def min_coins(arr, target):
        n = len(arr)
        dp = {i: {j: 1e6 for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 0
        for j in dp[0]:
            if j % arr[0] == 0:
                dp[0][j] = j // arr[0]
        for i in range(1, n):
            for j in range(target + 1):
                left = 1e6
                if j >= arr[i]:
                    left = 1 + dp[i][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = min(left, right)
        coins = dp[n - 1][target]
        if coins == 1e6:
            return -1
        return coins

    print(min_coins([1, 2, 3], 7))
    print(min_coins([1], 0))
    print(min_coins([12, 1, 3], 4))
    print(min_coins([2, 1], 11))
    print(min_coins([1, 2, 5], 11))
    print(min_coins([2], 3))
    print(min_coins([1, ], 0))
    print(min_coins([25, 10, 5], 30))
    print(min_coins([9, 6, 5, 1], 19))
    print(min_coins([5, 1], 0))
    print(min_coins([4, 6, 2], 5))


def space_optimized():
    """
        Time complexity is O(n*target) and space complexity is O(target).
    """
    def min_coins(arr, target):
        n = len(arr)
        prev = {j: 1e6 for j in range(target + 1)}
        prev[0] = 0
        for j in prev:
            if j % arr[0] == 0:
                prev[j] = j // arr[0]
        for i in range(1, n):
            curr = {j: 1e6 for j in range(target + 1)}
            curr[0] = 0
            for j in range(target + 1):
                left = 1e6
                if j >= arr[i]:
                    left = 1 + curr[j - arr[i]]
                right = prev[j]
                curr[j] = min(left, right)
            prev = curr
        coins = prev[target]
        if coins == 1e6:
            return -1
        return coins

    print(min_coins([1, 2, 3], 7))
    print(min_coins([1], 0))
    print(min_coins([12, 1, 3], 4))
    print(min_coins([2, 1], 11))
    print(min_coins([1, 2, 5], 11))
    print(min_coins([2], 3))
    print(min_coins([1, ], 0))
    print(min_coins([25, 10, 5], 30))
    print(min_coins([9, 6, 5, 1], 19))
    print(min_coins([5, 1], 0))
    print(min_coins([4, 6, 2], 5))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
