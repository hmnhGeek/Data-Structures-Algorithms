def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(i, j, n, m):
        if i == 0:
            return 1
        left = 0
        if 0 <= i - 1 < n:
            left = solve(i - 1, j, n, m)
        right = 0
        if 0 <= j - 1 < m:
            right = solve(i, j - 1, n, m)
        return left + right

    def grid_unique_paths(n, m):
        return solve(n - 1, m - 1, n, m)

    print(grid_unique_paths(2, 2))
    print(grid_unique_paths(1, 1))
    print(grid_unique_paths(3, 2))
    print(grid_unique_paths(1, 6))
    print(grid_unique_paths(3, 7))


recursive()
print()
