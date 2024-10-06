def recursive():
    # T: O(2^(nm)) and S: O(n + m)
    def solve(i, j, n, m):
        if i == 0 and j == 0:
            return 1

        left = 0
        if 0 <= i - 1 < n:
            left = solve(i - 1, j, n, m)

        right = 0
        if 0 <= j - 1 < m:
            right = solve(i, j - 1, n, m)

        return left + right

    def gup(n, m):
        return solve(n - 1, m - 1, n, m)

    print(gup(2, 2))
    print(gup(1, 1))
    print(gup(3, 2))
    print(gup(1, 6))
    print(gup(5, 4))


def memoized():
    # T: O(nm) and S: O(n + m + nm)
    def solve(i, j, n, m, dp):
        if i == 0 and j == 0:
            return 1

        if dp[i][j] is not None:
            return dp[i][j]

        left = 0
        if 0 <= i - 1 < n:
            left = solve(i - 1, j, n, m, dp)

        right = 0
        if 0 <= j - 1 < m:
            right = solve(i, j - 1, n, m, dp)

        dp[i][j] = left + right
        return left + right

    def gup(n, m):
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve(n - 1, m - 1, n, m, dp)

    print(gup(2, 2))
    print(gup(1, 1))
    print(gup(3, 2))
    print(gup(1, 6))
    print(gup(5, 4))


def tabulation():
    # T: O(nm) and S: O(nm)
    def gup(n, m):
        dp = {i: {j: 0 for j in range(m)} for i in range(n)}

        for j in dp[0]:
            dp[0][j] = 1
        for i in dp:
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                left = 0
                if 0 <= i - 1 < n:
                    left = dp[i - 1][j]

                right = 0
                if 0 <= j - 1 < m:
                    right = dp[i][j - 1]

                dp[i][j] = left + right

        return dp[n - 1][m - 1]

    print(gup(2, 2))
    print(gup(1, 1))
    print(gup(3, 2))
    print(gup(1, 6))
    print(gup(5, 4))


def space_optimized():
    # T: O(nm) and S: O(m)
    def gup(n, m):
        prev = {j: 1 for j in range(m)}

        for i in range(1, n):
            curr = {j: 0 for j in range(m)}
            curr[0] = 1
            for j in range(1, m):
                left = 0
                if 0 <= i - 1 < n:
                    left = prev[j]

                right = 0
                if 0 <= j - 1 < m:
                    right = curr[j - 1]

                curr[j] = left + right
            prev = curr

        return prev[m - 1]

    print(gup(2, 2))
    print(gup(1, 1))
    print(gup(3, 2))
    print(gup(1, 6))
    print(gup(5, 4))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()