def recursive():
    def solve(arr, index, can_buy, n):
        if index >= n:
            return 0
        if can_buy:
            return max(
                -arr[index] + solve(arr, index + 1, not can_buy, n),
                solve(arr, index + 1, can_buy, n)
            )
        else:
            return max(
                arr[index] + solve(arr, index + 2, not can_buy, n),
                solve(arr, index + 1, can_buy, n)
            )

    def buy_sell(arr):
        n = len(arr)
        return solve(arr, 0, True, n)

    print(buy_sell([4, 9, 0, 4, 10]))
    print(buy_sell([1, 2, 3, 4]))
    print(buy_sell([5, 4, 3]))
    print(buy_sell([1, 2, 3, 0, 2]))
    print(buy_sell([1]))
    print(buy_sell([3, 1, 6, 1, 2, 4]))


recursive()