def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(i):
        if i < 0:
            return 0
        if i == 0:
            return 1

        left = solve(i - 1)
        right = solve(i - 2)
        return left + right

    def climbing_stairs(n):
        return solve(n)

    print(climbing_stairs(3))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))
    print(climbing_stairs(2))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """
    def solve(i, dp):
        if i < 0:
            return 0
        if i == 0:
            return 1
        if dp[i] is not None:
            return dp[i]
        left = solve(i - 1, dp)
        right = solve(i - 2, dp)
        dp[i] = left + right
        return dp[i]

    def climbing_stairs(n):
        dp = {i: None for i in range(n + 1)}
        return solve(n, dp)

    print(climbing_stairs(3))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))
    print(climbing_stairs(2))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def climbing_stairs(n):
        dp = {i: 0 for i in range(n + 1)}
        dp[0] = 1
        for i in range(1, n + 1):
            left = dp[i - 1]
            right = dp[i - 2] if i > 1 else 0
            dp[i] = left + right
        return dp[n]

    print(climbing_stairs(3))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))
    print(climbing_stairs(2))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def climbing_stairs(n):
        dp = {i: 0 for i in range(n + 1)}
        prev1 = 1
        prev2 = 0
        for i in range(1, n + 1):
            left = prev1
            right = prev2
            curr = left + right
            prev2 = prev1
            prev1 = curr
        return prev1

    print(climbing_stairs(3))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))
    print(climbing_stairs(2))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()