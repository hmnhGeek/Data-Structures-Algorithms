def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, can_buy, n):
        if i >= n:
            return 0
        if can_buy:
            return max(
                -arr[i] + solve(arr, i + 1, False, n),
                solve(arr, i + 1, True, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 2, True, n),
                solve(arr, i + 1, False, n)
            )

    def buy_sell_cooldown(arr):
        n = len(arr)
        return solve(arr, 0, True, n)

    print(buy_sell_cooldown([4, 9, 0, 4, 10]))
    print(buy_sell_cooldown([1, 2, 3, 4]))
    print(buy_sell_cooldown([5, 4, 3]))
    print(buy_sell_cooldown([1, 2, 3, 0, 2]))
    print(buy_sell_cooldown([1]))
    print(buy_sell_cooldown([3, 1, 6, 1, 2, 4]))


recursive()
