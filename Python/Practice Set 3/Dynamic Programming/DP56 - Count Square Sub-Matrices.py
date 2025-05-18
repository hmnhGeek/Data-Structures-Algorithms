# Problem link - https://www.naukri.com/code360/problems/count-square-submatrices-with-all-ones_3751502?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=auS1fynpnjo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=57


class Solution:
    @staticmethod
    def count_squares(mtx):
        """
            Time complexity is O(nm) and space complexity O(mn).
        """
        n, m = len(mtx), len(mtx[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            dp[0][j] = mtx[0][j]
        for i in range(1, n):
            dp[i][0] = mtx[i][0]
        for i in range(1, n):
            for j in range(1, m):
                if mtx[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i - 1][j - 1],
                        dp[i][j - 1]
                    )
        result = 0
        for i in range(n):
            for j in range(m):
                result += dp[i][j]
        return result


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