# Problem link - https://www.geeksforgeeks.org/coin-change-dp-7/
# Solution - https://www.youtube.com/watch?v=HgyouUi11zk&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=23


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def coin_change_2(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    def solve(arr, i, j):
        if j == 0:
            return 1
        if i == 0:
            if j % arr[0] == 0:
                return 1
            return 0
        left = 0
        if arr[i] <= j:
            left = solve(arr, i, j - arr[i])
        right = solve(arr, i - 1, j)
        return left + right

    print(coin_change_2([1, 2, 3], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


def memoized():
    """
        Time complexity is O(nk) and space complexity is O(n + nk).
    """
    def coin_change_2(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    def solve(arr, i, j, dp):
        if j == 0:
            return 1
        if i == 0:
            if j % arr[0] == 0:
                return 1
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if arr[i] <= j:
            left = solve(arr, i, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left + right
        return dp[i][j]

    print(coin_change_2([1, 2, 3], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


def tabulation():
    """
        Time complexity is O(nk) and space complexity is O(nk).
    """
    def coin_change_2(arr, target):
        n = len(arr)
        dp = {i: {j: 0 for j in range(target + 1)} for i in range(n)}
        for i in range(n):
            dp[i][0] = 1
        for j in range(target + 1):
            if j % arr[0] == 0:
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(target + 1):
                left = 0
                if arr[i] <= j:
                    left = dp[i][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left + right
        return dp[n - 1][target]

    print(coin_change_2([1, 2, 3], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


def space_optimized():
    """
        Time complexity is O(nk) and space complexity is O(k).
    """
    def coin_change_2(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        for j in range(target + 1):
            if j % arr[0] == 0:
                prev[j] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for j in range(target + 1):
                left = 0
                if arr[i] <= j:
                    left = curr[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    print(coin_change_2([1, 2, 3], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
