def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, i, can_buy, fee, n):
        if i == n:
            return 0
        if can_buy:
            return max(
                -arr[i] + solve(arr, i + 1, False, fee, n),
                solve(arr, i + 1, True, fee, n)
            )
        else:
            return max(
                arr[i] - fee + solve(arr, i + 1, True, fee, n),
                solve(arr, i + 1, False, fee, n)
            )

    def buy_and_sell(arr, fee):
        n = len(arr)
        return solve(arr, 0, True, fee, n)

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


recursive()
