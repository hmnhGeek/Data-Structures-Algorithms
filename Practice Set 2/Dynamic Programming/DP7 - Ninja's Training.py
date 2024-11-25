def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, i, j, m):
        if i == 0:
            return arr[0][j]

        max_pts = 0
        for k in range(m):
            if k != j:
                max_pts = max(max_pts, solve(arr, i - 1, k, m))
        return arr[i][j] + max_pts

    def ninja_training(arr):
        n = len(arr)
        m = len(arr[0])
        max_pts = 0
        for i in range(m):
            max_pts = max(max_pts, solve(arr, n - 1, i, m))
        return max_pts

    print(ninja_training([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(
        ninja_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )
    print(
        ninja_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )

    print(
        ninja_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )


def memoized():
    """
        Time complexity is O(n*m^2) and space complexity is O(n*m).
    """

    def solve(arr, i, j, m, dp):
        if i == 0:
            return arr[0][j]

        if dp[i][j] is not None:
            return dp[i][j]

        max_pts = 0
        for k in range(m):
            if k != j:
                max_pts = max(max_pts, solve(arr, i - 1, k, m, dp))
        dp[i][j] = arr[i][j] + max_pts
        return dp[i][j]

    def ninja_training(arr):
        n = len(arr)
        m = len(arr[0])
        max_pts = 0
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        for i in range(m):
            max_pts = max(max_pts, solve(arr, n - 1, i, m, dp))
        return max_pts

    print(ninja_training([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(
        ninja_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )
    print(
        ninja_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )

    print(
        ninja_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )


recursive()
print()
memoized()
