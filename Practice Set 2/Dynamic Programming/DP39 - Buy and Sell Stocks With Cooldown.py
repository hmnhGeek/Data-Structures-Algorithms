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


def memoized():
    """
        Time complexity is O(2n) and space complexity is O(n + 2n).
    """
    def solve(arr, i, can_buy, n, dp):
        if i >= n:
            return 0
        if dp[i][can_buy] is not None:
            return dp[i][can_buy]
        if can_buy:
            dp[i][can_buy] = max(
                -arr[i] + solve(arr, i + 1, False, n, dp),
                solve(arr, i + 1, True, n, dp)
            )
        else:
            dp[i][can_buy] = max(
                arr[i] + solve(arr, i + 2, True, n, dp),
                solve(arr, i + 1, False, n, dp)
            )
        return dp[i][can_buy]

    def buy_sell_cooldown(arr):
        n = len(arr)
        dp = {i: {j: None for j in [True, False]} for i in range(n + 2)}
        return solve(arr, 0, True, n, dp)

    print(buy_sell_cooldown([4, 9, 0, 4, 10]))
    print(buy_sell_cooldown([1, 2, 3, 4]))
    print(buy_sell_cooldown([5, 4, 3]))
    print(buy_sell_cooldown([1, 2, 3, 0, 2]))
    print(buy_sell_cooldown([1]))
    print(buy_sell_cooldown([3, 1, 6, 1, 2, 4]))


recursive()
print()
memoized()
