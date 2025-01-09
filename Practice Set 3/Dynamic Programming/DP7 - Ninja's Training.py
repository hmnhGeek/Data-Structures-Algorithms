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
        Time complexity is O(nk) and space complexity is O(n + nk).
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


recursive()
print()
memoized()
print()
