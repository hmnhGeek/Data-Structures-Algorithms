def recursive():
    """
        Time complexity is O(2 ^ {m + n}) and space complexity is O(n + m).
    """

    def get_paths(n, m):
        return solve(n - 1, m - 1)

    def solve(i, j):
        if i < 0 or j < 0:
            return 0
        if i == 0 and j == 0:
            return 1
        up = solve(i - 1, j)
        down = solve(i, j - 1)
        return up + down

    print(get_paths(3, 7))
    print(get_paths(3, 2))
    print(get_paths(2, 2))
    print(get_paths(2, 3))


recursive()
