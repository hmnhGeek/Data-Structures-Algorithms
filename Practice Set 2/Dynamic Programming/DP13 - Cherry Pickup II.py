def recursive():
    """
        Time complexity is exponential and space complexity is O(m + n)
    """

    def solve(mtx, a, b, i, n, m):
        if i == 0:
            chocolates = 0
            if a == 0:
                chocolates += mtx[0][0]
            if b == m - 1:
                chocolates += mtx[0][m - 1]
            return chocolates

        max_chocolates = 0
        deltas = [-1, 0, 1]
        for da in deltas:
            for db in deltas:
                if a == b:
                    if 0 <= a + da < m and 0 <= b + db < m and 0 <= i - 1 < n:
                        max_chocolates = max(
                            max_chocolates,
                            mtx[i][a] + solve(mtx, a + da, b + db, i - 1, n, m)
                        )
                else:
                    if 0 <= a + da < m and 0 <= b + db < m and 0 <= i - 1 < n:
                        max_chocolates = max(
                            max_chocolates,
                            mtx[i][a] + mtx[i][b] + solve(mtx, a + da, b + db, i - 1, n, m)
                        )
        return max_chocolates

    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        max_chocolates = 0
        for alice in range(m):
            for bob in range(m):
                max_chocolates = max(max_chocolates, solve(mtx, alice, bob, n - 1, n, m))
        return max_chocolates

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(cherry_pickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(
        cherry_pickup(
            [
                [4, 1, 2],
                [3, 6, 1],
                [1, 6, 6],
                [3, 1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [2, 0, 0, 0, 0, 0, 2],
                [2, 1, 0, 0, 0, 4, 0],
                [2, 0, 10, 0, 1, 0, 0],
                [0, 3, 0, 6, 5, 0, 0],
                [1, 0, 3, 4, 0, 0, 6]
            ]
        )
    )


def memoized():
    """
        Time complexity is O(m^4 * n) and space complexity is O(m + n + m^2 * n)
    """

    def solve(mtx, a, b, i, n, m, dp):
        if i == 0:
            chocolates = 0
            if a == 0:
                chocolates += mtx[0][0]
            if b == m - 1:
                chocolates += mtx[0][m - 1]
            return chocolates

        if dp[i][a][b] is not None:
            return dp[i][a][b]

        max_chocolates = 0
        deltas = [-1, 0, 1]
        for da in deltas:
            for db in deltas:
                if a == b:
                    if 0 <= a + da < m and 0 <= b + db < m and 0 <= i - 1 < n:
                        max_chocolates = max(
                            max_chocolates,
                            mtx[i][a] + solve(mtx, a + da, b + db, i - 1, n, m, dp)
                        )
                else:
                    if 0 <= a + da < m and 0 <= b + db < m and 0 <= i - 1 < n:
                        max_chocolates = max(
                            max_chocolates,
                            mtx[i][a] + mtx[i][b] + solve(mtx, a + da, b + db, i - 1, n, m, dp)
                        )
        dp[i][a][b] = max_chocolates
        return dp[i][a][b]

    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        max_chocolates = 0
        for alice in range(m):
            for bob in range(m):
                dp = {i: {a: {b: None for b in range(m)} for a in range(m)} for i in range(n)}
                max_chocolates = max(max_chocolates, solve(mtx, alice, bob, n - 1, n, m, dp))
        return max_chocolates

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(cherry_pickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(
        cherry_pickup(
            [
                [4, 1, 2],
                [3, 6, 1],
                [1, 6, 6],
                [3, 1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [2, 0, 0, 0, 0, 0, 2],
                [2, 1, 0, 0, 0, 4, 0],
                [2, 0, 10, 0, 1, 0, 0],
                [0, 3, 0, 6, 5, 0, 0],
                [1, 0, 3, 4, 0, 0, 6]
            ]
        )
    )


def tabulation():
    """
        Time complexity is O(m^4 * n) and space complexity is O(m^2 * n)
    """
    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        max_chocolates = 0

        # O(m^2)
        for alice in range(m):
            for bob in range(m):
                dp = {i: {a: {b: 0 for b in range(m)} for a in range(m)} for i in range(n)}

                # O(m^2)
                for a in dp[0]:
                    for b in dp[0][a]:
                        chocolates = 0
                        if a == 0:
                            chocolates += mtx[0][0]
                        if b == m - 1:
                            chocolates += mtx[0][m - 1]
                        dp[0][a][b] = chocolates

                # O(n * m^2)
                for i in range(1, n):
                    for a in range(m):
                        for b in range(m):
                            sub_max_chocolates = 0
                            deltas = [-1, 0, 1]
                            for da in deltas:
                                for db in deltas:
                                    if a == b:
                                        if 0 <= a + da < m and 0 <= b + db < m and 0 <= i - 1 < n:
                                            sub_max_chocolates = max(
                                                sub_max_chocolates,
                                                mtx[i][a] + dp[i - 1][a + da][b + db]
                                            )
                                    else:
                                        if 0 <= a + da < m and 0 <= b + db < m and 0 <= i - 1 < n:
                                            sub_max_chocolates = max(
                                                sub_max_chocolates,
                                                mtx[i][a] + mtx[i][b] + dp[i - 1][a + da][b + db]
                                            )
                            dp[i][a][b] = sub_max_chocolates
                max_chocolates = max(max_chocolates, dp[n - 1][alice][bob])
        return max_chocolates

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(cherry_pickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(
        cherry_pickup(
            [
                [4, 1, 2],
                [3, 6, 1],
                [1, 6, 6],
                [3, 1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [2, 0, 0, 0, 0, 0, 2],
                [2, 1, 0, 0, 0, 4, 0],
                [2, 0, 10, 0, 1, 0, 0],
                [0, 3, 0, 6, 5, 0, 0],
                [1, 0, 3, 4, 0, 0, 6]
            ]
        )
    )


def space_optimized():
    """
        Time complexity is O(m^4 * n) and space complexity is O(m^2)
    """
    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        max_chocolates = 0

        # O(m^2)
        for alice in range(m):
            for bob in range(m):
                prev = {a: {b: 0 for b in range(m)} for a in range(m)}

                # O(m^2)
                for a in prev:
                    for b in prev[a]:
                        chocolates = 0
                        if a == 0:
                            chocolates += mtx[0][0]
                        if b == m - 1:
                            chocolates += mtx[0][m - 1]
                        prev[a][b] = chocolates

                # O(n * m^2)
                for i in range(1, n):
                    curr = {a: {b: 0 for b in range(m)} for a in range(m)}
                    for a in range(m):
                        for b in range(m):
                            sub_max_chocolates = 0
                            deltas = [-1, 0, 1]
                            for da in deltas:
                                for db in deltas:
                                    if a == b:
                                        if 0 <= a + da < m and 0 <= b + db < m and 0 <= i - 1 < n:
                                            sub_max_chocolates = max(
                                                sub_max_chocolates,
                                                mtx[i][a] + prev[a + da][b + db]
                                            )
                                    else:
                                        if 0 <= a + da < m and 0 <= b + db < m and 0 <= i - 1 < n:
                                            sub_max_chocolates = max(
                                                sub_max_chocolates,
                                                mtx[i][a] + mtx[i][b] + prev[a + da][b + db]
                                            )
                            curr[a][b] = sub_max_chocolates
                    prev = curr
                max_chocolates = max(max_chocolates, prev[alice][bob])
        return max_chocolates

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(cherry_pickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(
        cherry_pickup(
            [
                [4, 1, 2],
                [3, 6, 1],
                [1, 6, 6],
                [3, 1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [2, 0, 0, 0, 0, 0, 2],
                [2, 1, 0, 0, 0, 4, 0],
                [2, 0, 10, 0, 1, 0, 0],
                [0, 3, 0, 6, 5, 0, 0],
                [1, 0, 3, 4, 0, 0, 6]
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
