def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(n):
        if n == 0:
            return 1
        left = 0
        if 0 <= n - 1:
            left = solve(n - 1)
        right = 0
        if 0 <= n - 2:
            right = solve(n - 2)
        return left + right

    def climbing_stairs(n):
        return solve(n)

    print(climbing_stairs(3))
    print(climbing_stairs(2))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """

    def solve(n, dp):
        if n == 0:
            return 1
        if dp[n] is not None:
            return dp[n]
        left = 0
        if 0 <= n - 1:
            left = solve(n - 1, dp)
        right = 0
        if 0 <= n - 2:
            right = solve(n - 2, dp)
        dp[n] = left + right
        return dp[n]

    def climbing_stairs(n):
        dp = {i: None for i in range(n + 1)}
        return solve(n, dp)

    print(climbing_stairs(3))
    print(climbing_stairs(2))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def climbing_stairs(n):
        dp = {i: 0 for i in range(n + 1)}
        dp[0] = 1
        for i in range(1, n + 1):
            left = 0
            if 0 <= i - 1:
                left = dp[i - 1]
            right = 0
            if 0 <= i - 2:
                right = dp[i - 2]
            dp[i] = left + right
        return dp[n]

    print(climbing_stairs(3))
    print(climbing_stairs(2))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))


recursive()
print()
memoized()
print()
tabulation()
