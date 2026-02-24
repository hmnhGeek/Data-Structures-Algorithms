def recursive():
    def rod_cut(prices, rod_length):
        n = len(prices)
        return solve(prices, n - 1, rod_length)

    def solve(arr, i, j):
        if i < 0:
            return 0
        if j == 0:
            return 0
        left = -1e6
        if i + 1 <= j:
            left = arr[i] + solve(arr, i, j - i - 1)
        right = solve(arr, i - 1, j)
        return max(left, right)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


recursive()
print()