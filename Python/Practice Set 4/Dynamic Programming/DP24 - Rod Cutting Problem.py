# Problem link - https://www.naukri.com/code360/problems/rod-cutting-problem_800284?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=mO8XpGoJwuo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=25



def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def rod_cut(prices, rod_length):
        n = len(prices)
        return solve(prices, n - 1, rod_length)

    def solve(arr, i, j):
        if i < 0:
            return 0
        if j == 0:
            return 0
        left = -1e6
        if i + 1 <= j:
            left = arr[i] + solve(arr, i, j - i - 1)
        right = solve(arr, i - 1, j)
        return max(left, right)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def memoized():
    """
        Time complexity is O(rod_length * n) and space complexity is O(n + rod_length * n).
    """
    def rod_cut(prices, rod_length):
        n = len(prices)
        dp = {i: {j: None for j in range(rod_length + 1)} for i in range(-1, n)}
        return solve(prices, n - 1, rod_length, dp)

    def solve(arr, i, j, dp):
        if i < 0:
            return 0
        if j == 0:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = -1e6
        if i + 1 <= j:
            left = arr[i] + solve(arr, i, j - i - 1, dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = max(left, right)
        return dp[i][j]

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def tabulation():
    """
        Time complexity is O(rod_length * n) and space complexity is O(rod_length * n).
    """
    def rod_cut(prices, rod_length):
        n = len(prices)
        dp = {i: {j: -1e6 for j in range(rod_length + 1)} for i in range(-1, n)}
        for j in range(rod_length + 1):
            dp[-1][j] = 0
        for i in range(-1, n):
            dp[i][0] = 0
        for i in range(n):
            for j in range(rod_length + 1):
                left = -1e6
                if i + 1 <= j:
                    left = prices[i] + dp[i][j - i - 1]
                right = dp[i - 1][j]
                dp[i][j] = max(left, right)
        return dp[n - 1][rod_length]

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def space_optimized():
    """
        Time complexity is O(rod_length * n) and space complexity is O(rod_length).
    """
    def rod_cut(prices, rod_length):
        n = len(prices)
        prev = {j: -1e6 for j in range(rod_length + 1)}
        for j in range(rod_length + 1):
            prev[j] = 0
        prev[0] = 0
        for i in range(n):
            curr = {j: -1e6 for j in range(rod_length + 1)}
            curr[0] = 0
            for j in range(rod_length + 1):
                left = -1e6
                if i + 1 <= j:
                    left = prices[i] + curr[j - i - 1]
                right = prev[j]
                curr[j] = max(left, right)
            prev = curr
        return prev[rod_length]

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
