def recursive():
    """
        Time complexity is exponential and space complexity is polynomial.
    """
    def solve(arr, i, j):
        if i > j:
            return 0
        max_coins_collected = 0
        for index in range(i, j + 1):
            coins = arr[i - 1] * arr[index] * arr[j + 1] + solve(arr, i, index - 1) + solve(arr, index + 1, j)
            max_coins_collected = max(max_coins_collected, coins)
        return max_coins_collected

    def burst_balloons(arr):
        n = len(arr)
        balloons = [1] + arr + [1]
        return solve(balloons, 1, n)

    print(burst_balloons([3, 1, 5, 8]))
    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))
    print(burst_balloons([5, 10]))
    print(burst_balloons([1, 5]))


recursive()