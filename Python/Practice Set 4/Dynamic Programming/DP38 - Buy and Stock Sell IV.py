def recursive():
    def buy_sell(arr, k):
        n = len(arr)
        return solve(arr, 0, True, n, k)

    def solve(arr, i, j, n, k):
        if k == 0:
            return 0
        if i >= n:
            return 0
        if j:
            return max(
                -arr[i] + solve(arr, i + 1, not j, n, k),
                solve(arr, i + 1, j, n, k)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, not j, n, k - 1),
                solve(arr, i + 1, j, n, k)
            )

    print(buy_sell([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(buy_sell([1, 3, 1, 2, 4, 8], 2))
    print(buy_sell([5, 4, 3, 2, 1], 2))
    print(buy_sell([1, 2, 3, 4, 5], 2))
    print(buy_sell([7, 1, 5, 3, 6, 4], 2))


recursive()