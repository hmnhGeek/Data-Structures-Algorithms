# Problem link - https://www.naukri.com/code360/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=AE39gJYuRog&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=8


def get_next_activities_indices(j, k):
    result = []
    for i in range(k):
        if i != j:
            result.append(i)
    return result


def recursive():
    """
        Time complexity is O(k^n) and space complexity is O(n).
    """

    def solve(mtx, i, j, k):
        if i == 0:
            return mtx[0][j]
        ans = -1e6
        next_indices = get_next_activities_indices(j, k)
        for index in next_indices:
            ans = max(ans, mtx[i][j] + solve(mtx, i - 1, index, k))
        return ans

    def ninjas_training(mtx):
        n, k = len(mtx), len(mtx[0])
        ans = -1e6
        for j in range(k):
            ans = max(ans, solve(mtx, n - 1, j, k))
        return ans

    print(
        ninjas_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )


def memoized():
    """
        Time complexity is O(nk^3) and space complexity is O(n + nk).
    """

    def solve(mtx, i, j, k, dp):
        if i == 0:
            return mtx[0][j]
        if dp[i][j] is not None:
            return dp[i][j]
        ans = -1e6
        next_indices = get_next_activities_indices(j, k)
        for index in next_indices:
            ans = max(ans, mtx[i][j] + solve(mtx, i - 1, index, k, dp))
        dp[i][j] = ans
        return dp[i][j]

    def ninjas_training(mtx):
        n, k = len(mtx), len(mtx[0])
        ans = -1e6
        dp = {i: {j: None for j in range(k)} for i in range(n)}
        for j in range(k):
            ans = max(ans, solve(mtx, n - 1, j, k, dp))
        return ans

    print(
        ninjas_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )


def tabulation():
    """
        Time complexity is O(nk^3) and space complexity is O(nk).
    """
    def ninjas_training(mtx):
        n, k = len(mtx), len(mtx[0])
        ans = -1e6
        for j in range(k):
            dp = {i: {j: -1e6 for j in range(k)} for i in range(n)}
            for q in dp[0]:
                dp[0][q] = mtx[0][q]
            for i in range(1, n):
                for j0 in range(k):
                    res = -1e6
                    next_indices = get_next_activities_indices(j0, k)
                    for index in next_indices:
                        res = max(res, mtx[i][j0] + dp[i - 1][index])
                    dp[i][j0] = res
            ans = max(ans, dp[n - 1][j])
        return ans

    print(
        ninjas_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )


def space_optimized():
    """
        Time complexity is O(nk^3) and space complexity is O(k).
    """
    def ninjas_training(mtx):
        n, k = len(mtx), len(mtx[0])
        ans = -1e6
        for j in range(k):
            prev = {j: -1e6 for j in range(k)}
            for q in prev:
                prev[q] = mtx[0][q]
            for i in range(1, n):
                curr = {j: -1e6 for j in range(k)}
                for j0 in range(k):
                    res = -1e6
                    next_indices = get_next_activities_indices(j0, k)
                    for index in next_indices:
                        res = max(res, mtx[i][j0] + prev[index])
                    curr[j0] = res
                prev = curr
            ans = max(ans, prev[j])
        return ans

    print(
        ninjas_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
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
