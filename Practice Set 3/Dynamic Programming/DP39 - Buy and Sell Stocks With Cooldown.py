def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
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


def memoized():
    """
        Time complexity is O(n) and space complexity is O(3n).
    """
    def solve(arr, index, can_buy, n, dp):
        if index >= n:
            return 0
        if dp[index][can_buy] is not None:
            return dp[index][can_buy]

        if can_buy:
            dp[index][can_buy] = max(
                -arr[index] + solve(arr, index + 1, not can_buy, n, dp),
                solve(arr, index + 1, can_buy, n, dp)
            )
        else:
            dp[index][can_buy] = max(
                arr[index] + solve(arr, index + 2, not can_buy, n, dp),
                solve(arr, index + 1, can_buy, n, dp)
            )
        return dp[index][can_buy]

    def buy_sell(arr):
        n = len(arr)
        dp = {i: {j: None for j in [True, False]} for i in range(n + 2)}
        return solve(arr, 0, True, n, dp)

    print(buy_sell([4, 9, 0, 4, 10]))
    print(buy_sell([1, 2, 3, 4]))
    print(buy_sell([5, 4, 3]))
    print(buy_sell([1, 2, 3, 0, 2]))
    print(buy_sell([1]))
    print(buy_sell([3, 1, 6, 1, 2, 4]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """
    def buy_sell(arr):
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
                        arr[index] + dp[index + 2][not can_buy],
                        dp[index + 1][can_buy]
                    )
        return dp[0][True]

    print(buy_sell([4, 9, 0, 4, 10]))
    print(buy_sell([1, 2, 3, 4]))
    print(buy_sell([5, 4, 3]))
    print(buy_sell([1, 2, 3, 0, 2]))
    print(buy_sell([1]))
    print(buy_sell([3, 1, 6, 1, 2, 4]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def buy_sell(arr):
        n = len(arr)
        nxt = {j: 0 for j in [True, False]}
        nxt2 = {j: 0 for j in [True, False]}
        for index in range(n - 1, -1, -1):
            curr = {j: 0 for j in [True, False]}
            for can_buy in [True, False]:
                if can_buy:
                    curr[can_buy] = max(
                        -arr[index] + nxt[not can_buy],
                        nxt[can_buy]
                    )
                else:
                    curr[can_buy] = max(
                        arr[index] + nxt2[not can_buy],
                        nxt[can_buy]
                    )
            nxt2 = nxt
            nxt = curr
        return nxt[True]

    print(buy_sell([4, 9, 0, 4, 10]))
    print(buy_sell([1, 2, 3, 4]))
    print(buy_sell([5, 4, 3]))
    print(buy_sell([1, 2, 3, 0, 2]))
    print(buy_sell([1]))
    print(buy_sell([3, 1, 6, 1, 2, 4]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()