# Problem link - https://www.naukri.com/code360/problems/mining-diamonds_4244494?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=Yz4LlDSlkns&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=52


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(points, i, j):
        if i > j:
            return 0

        maxi = 0
        for k in range(i, j + 1):
            earnings = points[i - 1] * points[k] * points[j + 1] + solve(points, i, k - 1) + solve(points, k + 1, j)
            maxi = max(maxi, earnings)
        return maxi

    def burst_balloons(arr):
        points = [1] + arr + [1]
        return solve(points, 1, len(arr))

    print(burst_balloons([3, 1, 5, 8]))
    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))


def memoized():
    """
        Time complexity is O(n^3) and space complexity is O(n + n^2).
    """

    def solve(points, i, j, dp):
        if i > j:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        maxi = 0
        for k in range(i, j + 1):
            earnings = points[i - 1] * points[k] * points[j + 1] + solve(points, i, k - 1, dp) + solve(points, k + 1, j, dp)
            maxi = max(maxi, earnings)
        dp[i][j] = maxi
        return maxi

    def burst_balloons(arr):
        n = len(arr)
        points = [1] + arr + [1]
        dp = {i: {j: None for j in range(n + 1)} for i in range(n + 1)}
        return solve(points, 1, len(arr), dp)

    print(burst_balloons([3, 1, 5, 8]))
    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))


def tabulation():
    """
        Time complexity is O(n^3) and space complexity is O(n^2).
    """
    def burst_balloons(arr):
        n = len(arr)
        points = [1] + arr + [1]
        dp = {i: {j: 0 for j in range(n + 2)} for i in range(n + 2)}
        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                maxi = 0
                for k in range(i, j + 1):
                    earnings = points[i - 1] * points[k] * points[j + 1] + dp[i][k - 1] + dp[k + 1][j]
                    maxi = max(maxi, earnings)
                dp[i][j] = maxi

        return dp[1][n]

    print(burst_balloons([3, 1, 5, 8]))
    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))


recursive()
print()
memoized()
print()
tabulation()
