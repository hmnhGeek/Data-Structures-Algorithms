def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(prices, index, length):
        if length == 0:
            return 0

        if index == 1:
            return length * prices[0]

        left = 0
        if index <= length:
            left = prices[index - 1] + solve(prices, index, length - index)
        right = solve(prices, index - 1, length)
        return max(left, right)

    def rod_cut(prices, length):
        n = len(prices)
        return solve(prices, n, length)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))


def memoized():
    """
        Time complexity is O(n*length) and space complexity is O(n + n*length).
    """
    def solve(prices, index, length, dp):
        if length == 0:
            return 0

        if index == 1:
            return length * prices[0]

        if dp[index][length] is not None:
            return dp[index][length]

        left = 0
        if index <= length:
            left = prices[index - 1] + solve(prices, index, length - index, dp)
        right = solve(prices, index - 1, length, dp)
        dp[index][length] = max(left, right)
        return dp[index][length]

    def rod_cut(prices, length):
        n = len(prices)
        dp = {i: {j: None for j in range(length + 1)} for i in range(1, n + 1)}
        return solve(prices, n, length, dp)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))


def tabulation():
    """
        Time complexity is O(n*length) and space complexity is O(n*length).
    """
    def rod_cut(prices, length):
        n = len(prices)
        dp = {i: {j: 0 for j in range(length + 1)} for i in range(1, n + 1)}
        for j in dp[1]:
            dp[1][j] = j*prices[0]
        for i in dp:
            dp[i][0] = 0

        for index in range(2, n + 1):
            for l in range(length + 1):
                left = 0
                if index <= l:
                    left = prices[index - 1] + dp[index][l - index]
                right = dp[index - 1][l]
                dp[index][l] = max(left, right)
        return dp[n][length]

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))


recursive()
print()
memoized()
print()
tabulation()