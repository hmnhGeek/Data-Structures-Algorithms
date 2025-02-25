# Problem link - https://www.naukri.com/code360/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=AE39gJYuRog&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=8


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
        Time complexity is O(n*m^2) and space complexity is O(n + n*m).
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
        for i in range(m):
            dp = {i: {j: None for j in range(m)} for i in range(n)}
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


def tabulation():
    """
        Time complexity is O(n*m^2) and space complexity is O(n*m).
    """
    def ninja_training(arr):
        n = len(arr)
        m = len(arr[0])
        max_pts = 0

        for i in range(m):
            # recursion is starting from here, thus dp is defined here.
            dp = {i: {j: 0 for j in range(m)} for i in range(n)}
            for j in dp[0]:
                dp[0][j] = arr[0][j]

            for index in range(1, n):
                for j in range(m):
                    sub_max_pts = 0
                    for k in range(m):
                        if k != j:
                            sub_max_pts = max(sub_max_pts, dp[index - 1][k])
                    dp[index][j] = arr[index][j] + sub_max_pts
            max_pts = max(max_pts, dp[n - 1][i])
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


def space_optimized():
    """
        Time complexity is O(n*m^2) and space complexity is O(m).
    """
    def ninja_training(arr):
        n = len(arr)
        m = len(arr[0])
        max_pts = 0

        for i in range(m):
            # recursion is starting from here, thus previous is defined here.
            prev = {j: arr[0][j] for j in range(m)}
            for index in range(1, n):
                curr = {j: 0 for j in range(m)}
                for j in range(m):
                    sub_max_pts = 0
                    for k in range(m):
                        if k != j:
                            sub_max_pts = max(sub_max_pts, prev[k])
                    curr[j] = arr[index][j] + sub_max_pts
                prev = curr
            max_pts = max(max_pts, prev[i])
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
print()
tabulation()
print()
space_optimized()
