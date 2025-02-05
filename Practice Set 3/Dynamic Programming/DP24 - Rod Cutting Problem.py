def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, i, j):
        if j == 0:
            return 0
        if i == 0:
            return j * arr[0]
        left = -1e6
        if i + 1 <= j:
            left = arr[i] + solve(arr, i, j - i - 1)
        right = solve(arr, i - 1, j)
        return max(left, right)

    def rod_cut(costs, rod_length):
        n = len(costs)
        return solve(costs, n - 1, rod_length)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


recursive()
print()