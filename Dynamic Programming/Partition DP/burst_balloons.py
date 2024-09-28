def recursive():
    def solve(balloons, i, j):
        if i > j:
            return 0
        max_coins = float('-inf')
        for index in range(i, j + 1):
            cost = (balloons[i - 1] * balloons[index] * balloons[j + 1]) + \
                   solve(balloons, i, index - 1) + solve(balloons, index + 1, j)
            max_coins = max(max_coins, cost)
        return max_coins

    def burst_balloons(balloons):
        n = len(balloons)
        balloons = [1] + balloons + [1]
        return solve(balloons, 1, n)

    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))


recursive()