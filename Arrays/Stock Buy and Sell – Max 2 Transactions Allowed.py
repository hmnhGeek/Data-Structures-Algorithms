def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, index, can_buy, k, n):
        if k == 0:
            return 0
        if index == n:
            return 0
        if can_buy:
            return max(
                -arr[index] + solve(arr, index + 1, False, k, n),
                solve(arr, index + 1, True, k, n)
            )
        else:
            return max(
                arr[index] + solve(arr, index + 1, True, k - 1, n),
                solve(arr, index + 1, False, k, n)
            )

    def buy_sell(arr):
        n = len(arr)
        return solve(arr, 0, True, 2, n)

    print(buy_sell([10, 22, 5, 75, 65, 80]))
    print(buy_sell([100, 30, 15, 10, 8, 25, 80]))
    print(buy_sell([90, 80, 70, 60, 50]))
    print(buy_sell([10, 30, 50, 60]))
    print(buy_sell([2, 30, 15, 10, 8, 25, 80]))
    print(buy_sell([3, 3, 5, 0, 0, 3, 1, 4]))
    print(buy_sell([1, 2, 3, 4, 5]))


recursive()
