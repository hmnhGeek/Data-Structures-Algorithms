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


def memoized():
    """
        Time complexity is O(2n) and space complexity is O(n + 2n).
    """

    def solve(arr, i, can_buy, fee, n, dp):
        if i == n:
            return 0
        if dp[i][can_buy] is not None:
            return dp[i][can_buy]
        if can_buy:
            dp[i][can_buy] = max(
                -arr[i] + solve(arr, i + 1, False, fee, n, dp),
                solve(arr, i + 1, True, fee, n, dp)
            )
        else:
            dp[i][can_buy] = max(
                arr[i] - fee + solve(arr, i + 1, True, fee, n, dp),
                solve(arr, i + 1, False, fee, n, dp)
            )
        return dp[i][can_buy]

    def buy_and_sell(arr, fee):
        n = len(arr)
        dp = {i: {j: None for j in [True, False]} for i in range(n + 1)}
        return solve(arr, 0, True, fee, n, dp)

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


def tabulation():
    """
        Time complexity is O(2n) and space complexity is O(2n).
    """

    def buy_and_sell(arr, fee):
        n = len(arr)
        dp = {i: {j: 0 for j in [True, False]} for i in range(n + 1)}
        for i in range(n - 1, -1, -1):
            for can_buy in [True, False]:
                if can_buy:
                    dp[i][can_buy] = max(
                        -arr[i] + dp[i + 1][False],
                        dp[i + 1][True]
                    )
                else:
                    dp[i][can_buy] = max(
                        arr[i] - fee + dp[i + 1][True],
                        dp[i + 1][False]
                    )
        return dp[0][True]

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


def space_optimized():
    """
        Time complexity is O(2n) and space complexity is O(1).
    """

    def buy_and_sell(arr, fee):
        n = len(arr)
        nxt = {j: 0 for j in [True, False]}
        for i in range(n - 1, -1, -1):
            curr = {j: 0 for j in [True, False]}
            for can_buy in [True, False]:
                if can_buy:
                    curr[can_buy] = max(
                        -arr[i] + nxt[False],
                        nxt[True]
                    )
                else:
                    curr[can_buy] = max(
                        arr[i] - fee + nxt[True],
                        nxt[False]
                    )
            nxt = curr
        return nxt[True]

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
print()
space_optimized()
