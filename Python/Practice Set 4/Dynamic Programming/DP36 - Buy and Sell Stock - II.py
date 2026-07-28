def recursive():
    def max_profit(arr):
        n = len(arr)
        return solve(arr, 0, True, n)

    def solve(arr, i, j, n):
        if i >= n:
            return 0
        if j:
            return max(
                -arr[i] + solve(arr, i + 1, not j, n),
                solve(arr, i + 1, j, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, not j, n),
                solve(arr, i + 1, j, n)
            )

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


recursive()
print()
