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


recursive()