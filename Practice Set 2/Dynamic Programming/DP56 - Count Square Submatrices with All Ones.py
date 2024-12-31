class Solution:
    @staticmethod
    def count_squares(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][0] = mtx[i][0]
        for j in range(1, m):
            dp[0][j] = mtx[0][j]
        for i in range(1, n):
            for j in range(1, m):
                if mtx[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        for i in range(n):
            for j in range(m):
                count += dp[i][j]
        return count


print(
    Solution.count_squares(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(
    Solution.count_squares(
        [
            [1, 0],
            [0, 1]
        ]
    )
)

print(
    Solution.count_squares(
        [
            [0, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 1, 0]
        ]
    )
)
