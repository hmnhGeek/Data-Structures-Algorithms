def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, i, j):
        if j == 0:
            return 0
        if i == 0:
            if j % arr[0] == 0:
                return j // arr[0]
            else:
                return 1e6
        left = 1e6
        if arr[i] <= j:
            left = 1 + solve(arr, i, j - arr[i])
        right = solve(arr, i - 1, j)
        return min(left, right)

    def min_coins(arr, target):
        n = len(arr)
        ans = solve(arr, n - 1, target)
        if ans != 1e6:
            return ans
        return -1

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
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """

    def solve(arr, i, j, dp):
        if j == 0:
            return 0
        if i == 0:
            if j % arr[0] == 0:
                return j // arr[0]
            else:
                return 1e6
        if dp[i][j] is not None:
            return dp[i][j]
        left = 1e6
        if arr[i] <= j:
            left = 1 + solve(arr, i, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = min(left, right)
        return dp[i][j]

    def min_coins(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        ans = solve(arr, n - 1, target, dp)
        if ans != 1e6:
            return ans
        return -1

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
        Time complexity is O(n*k) and space complexity is O(nk).
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
                if arr[i] <= j:
                    left = 1 + dp[i][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = min(left, right)

        ans = dp[n - 1][target]
        if ans != 1e6:
            return ans
        return -1

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