def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i):
        if i < 0:
            return 0
        if i == 0:
            return arr[0]
        left = arr[i] + solve(arr, i - 2)
        right = solve(arr, i - 1)
        return max(left, right)

    def house_robber(arr):
        n = len(arr)
        return solve(arr, n - 1)

    def house_robber2(arr):
        x = house_robber(arr[:-1])
        y = house_robber(arr[1:])
        return max(x, y)

    print(house_robber2([2, 3, 2]))
    print(house_robber2([1, 3, 2, 1]))
    print(house_robber2([1, 5, 1, 2, 6]))
    print(house_robber2([2, 3, 5]))
    print(house_robber2([1, 3, 2, 0]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """
    def solve(arr, i, dp):
        if i < 0:
            return 0
        if i == 0:
            return arr[0]
        if dp[i] is not None:
            return dp[i]
        left = arr[i] + solve(arr, i - 2, dp)
        right = solve(arr, i - 1, dp)
        dp[i] = max(left, right)
        return dp[i]

    def house_robber(arr):
        n = len(arr)
        dp = {i: None for i in range(n)}
        dp[-2] = dp[-1] = None
        return solve(arr, n - 1, dp)

    def house_robber2(arr):
        x = house_robber(arr[:-1])
        y = house_robber(arr[1:])
        return max(x, y)

    print(house_robber2([2, 3, 2]))
    print(house_robber2([1, 3, 2, 1]))
    print(house_robber2([1, 5, 1, 2, 6]))
    print(house_robber2([2, 3, 5]))
    print(house_robber2([1, 3, 2, 0]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def house_robber(arr):
        n = len(arr)
        dp = {i: 0 for i in range(n)}
        dp[-2] = dp[-1] = 0
        for i in range(n):
            left = arr[i] + dp[i - 2]
            right = dp[i - 1]
            dp[i] = max(left, right)
        return dp[n - 1]

    def house_robber2(arr):
        x = house_robber(arr[:-1])
        y = house_robber(arr[1:])
        return max(x, y)

    print(house_robber2([2, 3, 2]))
    print(house_robber2([1, 3, 2, 1]))
    print(house_robber2([1, 5, 1, 2, 6]))
    print(house_robber2([2, 3, 5]))
    print(house_robber2([1, 3, 2, 0]))


recursive()
print()
memoized()
print()
tabulation()