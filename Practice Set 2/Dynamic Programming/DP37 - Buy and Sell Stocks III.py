def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, i, can_buy, tx, n):
        if tx == 2:
            return 0
        if i == n:
            return 0
        if can_buy:
            return max(
                -arr[i] + solve(arr, i + 1, False, tx, n),
                solve(arr, i + 1, True, tx, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, True, tx + 1, n),
                solve(arr, i + 1, False, tx, n)
            )

    def buy_sell(arr):
        n = len(arr)
        return solve(arr, 0, True, 0, n)

    print(buy_sell([3, 3, 5, 0, 0, 3, 1, 4]))
    print(buy_sell([1, 3, 1, 2, 4, 8]))
    print(buy_sell([5, 4, 3, 2, 1]))
    print(buy_sell([1, 2, 3, 4, 5]))
    print(buy_sell([7, 1, 5, 3, 6, 4]))


recursive()
