# Problem link - https://www.naukri.com/code360/problems/rod-cutting-problem_800284?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=mO8XpGoJwuo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=25


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(prices, index, length):
        if length == 0:
            return 0
        if index == 0:
            return length * prices[0]
        left = 0
        if index + 1 <= length:
            left = prices[index] + solve(prices, index, length - index - 1)
        right = solve(prices, index - 1, length)
        return max(left, right)

    def rod_cut(prices, rod_length):
        n = len(prices)
        return solve(prices, n - 1, rod_length)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def memoized():
    """
        Time complexity is O(n * rod_length) and space complexity is O(n + n * rod_length).
    """

    def solve(prices, index, length, dp):
        if length == 0:
            return 0
        if index == 0:
            return length * prices[0]
        if dp[index][length] is not None:
            return dp[index][length]
        left = 0
        if index + 1 <= length:
            left = prices[index] + solve(prices, index, length - index - 1, dp)
        right = solve(prices, index - 1, length, dp)
        dp[index][length] = max(left, right)
        return dp[index][length]

    def rod_cut(prices, rod_length):
        n = len(prices)
        dp = {i: {j: None for j in range(rod_length + 1)} for i in range(n)}
        return solve(prices, n - 1, rod_length, dp)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def tabulation():
    """
        Time complexity is O(n * rod_length) and space complexity is O(n * rod_length).
    """
    def rod_cut(prices, rod_length):
        n = len(prices)
        dp = {i: {j: 0 for j in range(rod_length + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = j * prices[0]
        for i in dp:
            dp[i][0] = 0
        for index in range(1, n):
            for length in range(rod_length + 1):
                left = 0
                if index + 1 <= length:
                    left = prices[index] + dp[index][length - index - 1]
                right = dp[index - 1][length]
                dp[index][length] = max(left, right)
        return dp[n - 1][rod_length]

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def space_optimized():
    """
        Time complexity is O(n * rod_length) and space complexity is O(rod_length).
    """
    def rod_cut(prices, rod_length):
        n = len(prices)
        prev = {j: 0 for j in range(rod_length + 1)}
        for j in prev:
            prev[j] = j * prices[0]
        prev[0] = 0
        for index in range(1, n):
            curr = {j: 0 for j in range(rod_length + 1)}
            for length in range(rod_length + 1):
                left = 0
                if index + 1 <= length:
                    left = prices[index] + curr[length - index - 1]
                right = prev[length]
                curr[length] = max(left, right)
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
