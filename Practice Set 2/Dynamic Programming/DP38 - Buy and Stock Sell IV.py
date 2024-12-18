def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, can_buy, tx, k, n):
        if tx == k:
            return 0
        if i == n:
            return 0
        if can_buy:
            return max(
                -arr[i] + solve(arr, i + 1, False, tx, k, n),
                solve(arr, i + 1, True, tx, k, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, True, tx + 1, k, n),
                solve(arr, i + 1, False, tx, k, n)
            )

    def buy_and_sell(arr, k):
        n = len(arr)
        return solve(arr, 0, True, 0, k, n)

    print(buy_and_sell([3, 2, 6, 5, 0, 3], 2))
    print(buy_and_sell([8, 5, 1, 3, 10], 2))
    print(buy_and_sell([10, 8, 6, 2], 2))
    print(buy_and_sell([2, 6, 5, 2], 0))
    print(buy_and_sell([1, 2, 3, 5], 2))
    print(buy_and_sell([2, 4, 1], 2))
    print(buy_and_sell([10, 22, 5, 75, 65, 80], 2))
    print(buy_and_sell([12, 14, 17, 10, 14, 13, 12, 15], 3))
    print(buy_and_sell([100, 30, 15, 10, 8, 25, 80], 3))
    print(buy_and_sell([90, 80, 70, 60, 50], 1))


recursive()