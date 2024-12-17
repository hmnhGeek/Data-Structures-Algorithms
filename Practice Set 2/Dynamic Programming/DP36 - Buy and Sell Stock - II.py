def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, can_buy, n):
        if i == n:
            return 0

        if can_buy:
            return max(
                -arr[i] + solve(arr, i + 1, False, n),
                solve(arr, i + 1, True, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, True, n),
                solve(arr, i + 1, False, n)
            )

    def max_profit(arr):
        n = len(arr)
        return solve(arr, 0, True, n)

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


recursive()
