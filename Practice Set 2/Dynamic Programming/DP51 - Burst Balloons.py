def recursive():
    """
        Time complexity is exponential and space complexity is polynomial.
    """
    def solve(arr, i, j):
        if i > j:
            return 0
        max_coins = 0
        for index in range(i, j + 1):
            coins = arr[i - 1] * arr[index] * arr[j + 1] + solve(arr, i, index - 1) + solve(arr, index + 1, j)
            max_coins = max(max_coins, coins)
        return max_coins

    def burst(arr):
        n = len(arr)
        balloons = [1, ] + arr + [1, ]
        return solve(balloons, 1, n)

    print(burst([3, 1, 5, 8]))
    print(burst([7, 1, 8]))
    print(burst([9, 1]))
    print(burst([1, 2, 3, 4, 5]))
    print(burst([1, 5, 2, 8]))
    print(burst([5, 10]))
    print(burst([1, 5]))


recursive()