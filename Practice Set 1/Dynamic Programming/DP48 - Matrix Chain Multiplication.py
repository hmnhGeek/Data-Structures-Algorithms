# Problem link - https://www.naukri.com/code360/problems/matrix-chain-multiplication_975344?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=pDCXsbAw5Cg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=50


def recursive():
    """
        Time complexity is exponential
    """

    def solve(arr, i, j):
        if i == j:
            return 0

        min_val = 1e6
        for k in range(i, j):
            steps = (arr[i - 1] * arr[k] * arr[j]) + solve(arr, i, k) + solve(arr, k + 1, j)
            min_val = min(min_val, steps)
        return min_val

    def matrix_chain_multiplication(arr):
        n = len(arr)
        return solve(arr, 1, n - 1)

    print(matrix_chain_multiplication([10, 20, 30, 40, 50]))
    print(matrix_chain_multiplication([4, 5, 3, 2]))
    print(matrix_chain_multiplication([10, 15, 20, 25]))
    print(matrix_chain_multiplication([1, 4, 3, 2]))


def memoized():
    """
        Time complexity is O(n^3) and space complexity is (n^2 + n).
    """

    def solve(arr, i, j, dp):
        if i == j:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        min_val = 1e6
        for k in range(i, j):
            steps = (arr[i - 1] * arr[k] * arr[j]) + solve(arr, i, k, dp) + solve(arr, k + 1, j, dp)
            min_val = min(min_val, steps)
        dp[i][j] = min_val
        return min_val

    def matrix_chain_multiplication(arr):
        n = len(arr)
        dp = {i: {j: None for j in range(n)} for i in range(n)}
        return solve(arr, 1, n - 1, dp)

    print(matrix_chain_multiplication([10, 20, 30, 40, 50]))
    print(matrix_chain_multiplication([4, 5, 3, 2]))
    print(matrix_chain_multiplication([10, 15, 20, 25]))
    print(matrix_chain_multiplication([1, 4, 3, 2]))


def tabulation():
    """
        Time complexity is O(n^3) and space complexity is (n^2).
    """
    def matrix_chain_multiplication(arr):
        n = len(arr)
        dp = {i: {j: 1e6 for j in range(n)} for i in range(n)}
        for i in dp:
            dp[i][i] = 0

        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n):
                min_val = 1e6
                for k in range(i, j):
                    steps = (arr[i - 1] * arr[k] * arr[j]) + dp[i][k] + dp[k + 1][j]
                    min_val = min(min_val, steps)
                dp[i][j] = min_val

        return dp[1][n - 1]

    print(matrix_chain_multiplication([10, 20, 30, 40, 50]))
    print(matrix_chain_multiplication([4, 5, 3, 2]))
    print(matrix_chain_multiplication([10, 15, 20, 25]))
    print(matrix_chain_multiplication([1, 4, 3, 2]))


recursive()
print()
memoized()
print()
tabulation()