def recursive():
    def solve_for_lcs(s1, s2, i, j):
        # at any point, if indices become negative, then it means
        # that either of the two strings or both have become empty,
        # in this case, there is no common substring, and even if both
        # are "", then also, the length is 0, so return 0.
        if i < 0 or j < 0:
            return 0

        # if the ith and jth indices match, we have found one matching character in
        # the substring, so add 1 to the answer (which represents the length of the lcs).
        # Decrement both the indices and recurse on them to find solution for sub problems.
        if s1[i] == s2[j]:
            return 1 + solve_for_lcs(s1, s2, i - 1, j - 1)

        # if there was no match, add 0 to answer and solve for these two cases:
        # Case 1: Solve for f(i - 1, j)
        # Case 2: Solve for f(i, j - 1)
        # From both, find out the maximum value and return that, meaning max length lcs.
        return 0 + max(solve_for_lcs(s1, s2, i - 1, j), solve_for_lcs(s1, s2, i, j - 1))

    def lcs(s1, s2):
        n = len(s1)
        m = len(s2)
        return solve_for_lcs(s1, s2, n - 1, m - 1)

    print(lcs("abcdgh", "aedfhr"))
    print(lcs("abc", "ac"))
    print(lcs("xyzw", "xywz"))


def memoized():
    def solve_for_lcs(s1, s2, i, j, dp):
        # at any point, if indices become negative, then it means
        # that either of the two strings or both have become empty,
        # in this case, there is no common substring, and even if both
        # are "", then also, the length is 0, so return 0.
        if i < 0 or j < 0:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        # if the ith and jth indices match, we have found one matching character in
        # the substring, so add 1 to the answer (which represents the length of the lcs).
        # Decrement both the indices and recurse on them to find solution for sub problems.
        if s1[i] == s2[j]:
            dp[i][j] = 1 + solve_for_lcs(s1, s2, i - 1, j - 1, dp)
            return dp[i][j]

        # if there was no match, add 0 to answer and solve for these two cases:
        # Case 1: Solve for f(i - 1, j)
        # Case 2: Solve for f(i, j - 1)
        # From both, find out the maximum value and return that, meaning max length lcs.
        dp[i][j] = 0 + max(solve_for_lcs(s1, s2, i - 1, j, dp), solve_for_lcs(s1, s2, i, j - 1, dp))
        return dp[i][j]

    def lcs(s1, s2):
        n = len(s1)
        m = len(s2)

        # please take a note that columns in dp represent s2 and rows in dp represent s1.
        dp = [[None for _ in range(m)] for _ in range(n)]
        return solve_for_lcs(s1, s2, n - 1, m - 1, dp)

    print(lcs("abcdgh", "aedfhr"))
    print(lcs("abc", "ac"))
    print(lcs("xyzw", "xywz"))


def tabulation():
    def lcs(s1, s2):
        n = len(s1)
        m = len(s2)

        # please take a note that columns in dp represent s2 and rows in dp represent s1.
        dp = [[None for _ in range(m)] for _ in range(n)]

        # This base condition shall be handled in the for loop
        # if i < 0 or j < 0:
        #     return 0

        for i in range(n):
            for j in range(m):
                # in matrix kind of tabulation solution, always handle dp[0][0] explicitly
                if i == 0 and j == 0:
                    dp[0][0] = 1 if s1[i] == s2[j] else 0
                else:
                    # i > 0 and j > 0; Handling negative indices
                    if s1[i] == s2[j] and i > 0 and j > 0:
                        prev = dp[i - 1][j - 1]
                        dp[i][j] = 1 + (prev if prev else 0)
                    else:
                        left = dp[i - 1][j] if i > 0 else 0
                        right = dp[i][j - 1] if j > 0 else 0
                        dp[i][j] = 0 + max(left, right)

        # answer always lies on the last cell of dp matrix.
        return dp[n - 1][m - 1]

    print(lcs("abcdgh", "aedfhr"))
    print(lcs("abc", "ac"))
    print(lcs("xyzw", "xywz"))


def space_optimized():
    def lcs(s1, s2):
        n = len(s1)
        m = len(s2)

        # store previous row
        prev = [0 for _ in range(m)]

        # This base condition shall be handled in the for loop
        # if i < 0 or j < 0:
        #     return 0

        for i in range(n):
            curr = [0 for _ in range(m)]
            for j in range(m):
                # in matrix kind of tabulation solution, always handle dp[0][0] explicitly
                if i == 0 and j == 0:
                    curr[0] = 1 if s1[i] == s2[j] else 0
                else:
                    # i > 0 and j > 0; Handling negative indices
                    if s1[i] == s2[j] and i > 0 and j > 0:
                        temp = prev[j - 1]
                        curr[j] = 1 + (temp if temp else 0)
                    else:
                        left = prev[j] if i > 0 else 0
                        right = curr[j - 1] if j > 0 else 0
                        curr[j] = 0 + max(left, right)

            prev = curr

        # answer always lies on the last index of previous row.
        return prev[m - 1]

    print(lcs("abcdgh", "aedfhr"))
    print(lcs("abc", "ac"))
    print(lcs("xyzw", "xywz"))


print("Recursive Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()
