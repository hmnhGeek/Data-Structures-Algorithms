def recursive():
    def buy_and_sell(arr, transaction_fee):
        n = len(arr)
        return solve(arr, 0, True, transaction_fee, n)

    def solve(arr, i, j, k, n):
        if i >= n:
            return 0
        if j:
            return max(
                -arr[i] + solve(arr, i + 1, not j, k, n),
                solve(arr, i + 1, j, k, n)
            )
        else:
            return max(
                arr[i] - k + solve(arr, i + 1, not j, k, n),
                solve(arr, i + 1, j, k, n)
            )

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


recursive()
print()