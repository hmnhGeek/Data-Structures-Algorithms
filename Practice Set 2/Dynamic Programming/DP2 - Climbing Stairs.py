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


recursive()
print()
memoized()