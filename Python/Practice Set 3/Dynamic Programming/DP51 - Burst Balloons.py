# Problem link - https://www.naukri.com/code360/problems/mining-diamonds_4244494?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=Yz4LlDSlkns&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=52


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


def memoized():
    """
        Time complexity is O(n^3) and space complexity is O(n^2 + recursion).
    """
    def solve(arr, i, j, dp):
        if i > j:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        max_coins_collected = 0
        for index in range(i, j + 1):
            coins = arr[i - 1] * arr[index] * arr[j + 1] + solve(arr, i, index - 1, dp) + solve(arr, index + 1, j, dp)
            max_coins_collected = max(max_coins_collected, coins)
        dp[i][j] = max_coins_collected
        return dp[i][j]

    def burst_balloons(arr):
        n = len(arr)
        balloons = [1] + arr + [1]
        dp = {i: {j: None for j in range(n + 1)} for i in range(n + 1)}
        return solve(balloons, 1, n, dp)

    print(burst_balloons([3, 1, 5, 8]))
    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))
    print(burst_balloons([5, 10]))
    print(burst_balloons([1, 5]))


def tabulation():
    """
        Time complexity is O(n^3) and space complexity is O(n^2).
    """
    def burst_balloons(arr):
        n = len(arr)
        arr = [1] + arr + [1]
        dp = {i: {j: 0 for j in range(n + 2)} for i in range(n + 2)}
        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                if i > j:
                    continue
                max_coins_collected = 0
                for index in range(i, j + 1):
                    coins = arr[i - 1] * arr[index] * arr[j + 1] + dp[i][index - 1] + dp[index + 1][j]
                    max_coins_collected = max(max_coins_collected, coins)
                dp[i][j] = max_coins_collected
        return dp[1][n]

    print(burst_balloons([3, 1, 5, 8]))
    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))
    print(burst_balloons([5, 10]))
    print(burst_balloons([1, 5]))


recursive()
print()
memoized()
print()
tabulation()
