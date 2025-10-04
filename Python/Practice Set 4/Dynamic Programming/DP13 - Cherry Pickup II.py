def recursive():
    def cherry_pickup(mtx):
        """
            Time complexity is exponential and space complexity is O(m + n)
        """
        n, m = len(mtx), len(mtx[0])
        max_chocolates = 0
        for last_alice_index in range(m):
            for last_bob_index in range(m):
                max_chocolates = max(max_chocolates, solve(mtx, n - 1, last_alice_index, last_bob_index, n, m))
        return max_chocolates

    def solve(mtx, i, a, b, n, m):
        if i == 0:
            if a == 0 and b == m - 1:
                return mtx[0][0] + mtx[0][m - 1]
            return 0
        chocolates = 0
        for da in range(-1, 2):
            for db in range(-1, 2):
                if 0 <= a < m and 0 <= b < m:
                    if a == b:
                        chocolates = max(chocolates, mtx[i][a] + solve(mtx, i - 1, a + da, b + db, n, m))
                    else:
                        chocolates = max(chocolates, mtx[i][a] + mtx[i][b] + solve(mtx, i - 1, a + da, b + db, n, m))
        return chocolates

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
    def cherry_pickup(mtx):
        """
            Time complexity is O(m^4 * n) and space complexity is O(m + n + m^2 * n)
        """
        n, m = len(mtx), len(mtx[0])
        max_chocolates = 0
        for last_alice_index in range(m):
            for last_bob_index in range(m):
                dp = {i: {a: {b: None for b in range(-1, m + 1)} for a in range(-1, m + 1)} for i in range(n)}
                max_chocolates = max(max_chocolates, solve(mtx, n - 1, last_alice_index, last_bob_index, n, m, dp))
        return max_chocolates

    def solve(mtx, i, a, b, n, m, dp):
        if i == 0:
            if a == 0 and b == m - 1:
                return mtx[0][0] + mtx[0][m - 1]
            return 0
        if dp[i][a][b] is not None:
            return dp[i][a][b]
        chocolates = 0
        for da in range(-1, 2):
            for db in range(-1, 2):
                if 0 <= a < m and 0 <= b < m:
                    if a == b:
                        chocolates = max(chocolates, mtx[i][a] + solve(mtx, i - 1, a + da, b + db, n, m, dp))
                    else:
                        chocolates = max(chocolates, mtx[i][a] + mtx[i][b] + solve(mtx, i - 1, a + da, b + db, n, m, dp))
        dp[i][a][b] = chocolates
        return dp[i][a][b]

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
    def cherry_pickup(mtx):
        """
            Time complexity is O(m^4 * n) and space complexity is O(m + n + m^2 * n)
        """
        n, m = len(mtx), len(mtx[0])
        max_chocolates = 0
        for last_alice_index in range(m):
            for last_bob_index in range(m):
                dp = {i: {a: {b: 0 for b in range(m)} for a in range(m)} for i in range(n)}
                dp[0][0][m - 1] = mtx[0][0] + mtx[0][m - 1]

                for i in range(1, n):
                    for a in range(m):
                        for b in range(m):
                            chocolates = 0
                            for da in range(-1, 2):
                                for db in range(-1, 2):
                                    if 0 <= a + da < m and 0 <= b + db < m:
                                        if a == b:
                                            chocolates = max(chocolates, mtx[i][a] + dp[i - 1][a + da][b + db])
                                        else:
                                            chocolates = max(chocolates, mtx[i][a] + mtx[i][b] + dp[i - 1][a + da][b + db])
                            dp[i][a][b] = chocolates

                max_chocolates = max(max_chocolates, dp[n - 1][last_alice_index][last_bob_index])
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
