def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, index, can_buy, fee, n):
        if index >= n:
            return 0
        if can_buy:
            return max(
                -arr[index] + solve(arr, index + 1, not can_buy, fee, n),
                solve(arr, index + 1, can_buy, fee, n)
            )
        else:
            return max(
                arr[index] - fee + solve(arr, index + 1, not can_buy, fee, n),
                solve(arr, index + 1, can_buy, fee, n)
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


def memoized():
    """
        Time complexity is O(n) and space complexity is O(3n).
    """
    def solve(arr, index, can_buy, fee, n, dp):
        if index >= n:
            return 0
        if dp[index][can_buy] is not None:
            return dp[index][can_buy]
        if can_buy:
            dp[index][can_buy] = max(
                -arr[index] + solve(arr, index + 1, not can_buy, fee, n, dp),
                solve(arr, index + 1, can_buy, fee, n, dp)
            )
        else:
            dp[index][can_buy] = max(
                arr[index] - fee + solve(arr, index + 1, not can_buy, fee, n, dp),
                solve(arr, index + 1, can_buy, fee, n, dp)
            )
        return dp[index][can_buy]

    def buy_and_sell(arr, fee):
        n = len(arr)
        dp = {i: {j: None for j in [True, False]} for i in range(n + 2)}
        return solve(arr, 0, True, fee, n, dp)

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(3n).
    """
    def buy_and_sell(arr, fee):
        n = len(arr)
        dp = {i: {j: 0 for j in [True, False]} for i in range(n + 2)}
        for index in range(n - 1, -1, -1):
            for can_buy in [True, False]:
                if can_buy:
                    dp[index][can_buy] = max(
                        -arr[index] + dp[index + 1][not can_buy],
                        dp[index + 1][can_buy]
                    )
                else:
                    dp[index][can_buy] = max(
                        arr[index] - fee + dp[index + 1][not can_buy],
                        dp[index + 1][can_buy]
                    )
        return dp[0][True]

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


recursive()
print()
memoized()
print()
tabulation()
