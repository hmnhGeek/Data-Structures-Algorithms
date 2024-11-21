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


recursive()