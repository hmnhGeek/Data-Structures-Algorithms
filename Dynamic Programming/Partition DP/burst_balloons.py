# Problem link - https://www.naukri.com/code360/problems/mining-diamonds_4244494?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=Yz4LlDSlkns&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=52


def recursive():
    def solve(balloons, i, j):
        """
            The time complexity is exponential and space complexity is O(n).
        """

        # if there are no more balloons left to be burst, return 0 coins.
        if i > j:
            return 0

        # assume that -inf max coins have been collected.
        max_coins = float('-inf')

        # loop from `i` to `j` (inclusive), assuming each one of them to be the last balloon that was burst.
        for index in range(i, j + 1):
            # the cost of bursting this balloon will be (i - 1)th balloon * this balloon * (j + 1)th balloon, plus the
            # coins obtained by bursting balloons from i to index - 1 and balloons from index + 1 to j.
            coins_collected = (balloons[i - 1] * balloons[index] * balloons[j + 1]) + \
                   solve(balloons, i, index - 1) + solve(balloons, index + 1, j)

            # maximize the max coins obtained
            max_coins = max(max_coins, coins_collected)

        # return the max coins obtained.
        return max_coins

    def burst_balloons(balloons):
        n = len(balloons)
        # append and prepend `1`s to make the multiplication possible for edge balloons.
        balloons = [1] + balloons + [1]
        # apart from the above two virtual balloons, actual balloons now start from index 1 to index n.
        return solve(balloons, 1, n)

    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))


def memoized():
    def solve(balloons, i, j, dp):
        """
            The time complexity is O(n^3) and space complexity is O(n + n^2).
        """

        # if there are no more balloons left to be burst, return 0 coins.
        if i > j:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        # assume that -inf max coins have been collected.
        max_coins = float('-inf')

        # loop from `i` to `j` (inclusive), assuming each one of them to be the last balloon that was burst.
        for index in range(i, j + 1):
            # the cost of bursting this balloon will be (i - 1)th balloon * this balloon * (j + 1)th balloon, plus the
            # coins obtained by bursting balloons from i to index - 1 and balloons from index + 1 to j.
            coins_collected = (balloons[i - 1] * balloons[index] * balloons[j + 1]) + \
                   solve(balloons, i, index - 1, dp) + solve(balloons, index + 1, j, dp)

            # maximize the max coins obtained
            max_coins = max(max_coins, coins_collected)

        # return the max coins obtained.
        dp[i][j] = max_coins
        return max_coins

    def burst_balloons(balloons):
        n = len(balloons)
        # append and prepend `1`s to make the multiplication possible for edge balloons.
        balloons = [1] + balloons + [1]

        dp = {i: {j: None for j in range(n + 2)} for i in range(n + 2)}

        # apart from the above two virtual balloons, actual balloons now start from index 1 to index n.
        return solve(balloons, 1, n, dp)

    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))


recursive()
print()
memoized()