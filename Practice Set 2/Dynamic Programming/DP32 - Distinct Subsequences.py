def recursive():
    """
        Time complexity is O(2^{n + m}) and space complexity is O(n + m).
    """
    def solve(s1, i, s2, j):
        # if both the strings get exhausted at the same time, return 1 as we have found a match
        if i < 0 and j < 0:
            return 1
        # if s1 is exhausted but s2 still has characters, we have not found a match.
        if i < 0:
            return 0
        # if s2 is exhausted but s1 has characters, we have found a match, return 1.
        if j < 0:
            return 1

        # if ith and jth characters match, then we have two options.
        if s1[i] == s2[j]:
            # option 1: use the match and decrement both indices
            # option 2: don't match with current i character, match with some other lower index in s1.
            # add the results from above two options
            return solve(s1, i - 1, s2, j - 1) + solve(s1, i - 1, s2, j)
        else:
            # if there is no match, use option 2 from above.
            return solve(s1, i - 1, s2, j)

    def distinct_subsequences(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n - 1, s2, m - 1)

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


def memoized():
    """
        Time complexity is O(n * m) and space complexity is O(n + m + nm).
    """
    def solve(s1, i, s2, j, dp):
        # if both the strings get exhausted at the same time, return 1 as we have found a match
        if i == 0 and j == 0:
            return 1
        # if s1 is exhausted but s2 still has characters, we have not found a match.
        if i == 0:
            return 0
        # if s2 is exhausted but s1 has characters, we have found a match, return 1.
        if j == 0:
            return 1

        if dp[i][j] is not None:
            return dp[i][j]

        # if ith and jth characters match, then we have two options.
        if s1[i - 1] == s2[j - 1]:
            # option 1: use the match and decrement both indices
            # option 2: don't match with current i character, match with some other lower index in s1.
            # add the results from above two options
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp) + solve(s1, i - 1, s2, j, dp)
        else:
            # if there is no match, use option 2 from above.
            dp[i][j] = solve(s1, i - 1, s2, j, dp)
        return dp[i][j]

    def distinct_subsequences(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


def tabulation():
    """
        Time complexity is O(n * m) and space complexity is O(n * m).
    """
    def distinct_subsequences(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        for i in dp:
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if ith and jth characters match, then we have two options.
                if s1[i - 1] == s2[j - 1]:
                    # option 1: use the match and decrement both indices
                    # option 2: don't match with current i character, match with some other lower index in s1.
                    # add the results from above two options
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # if there is no match, use option 2 from above.
                    dp[i][j] = dp[i - 1][j]
        return dp[n][m]

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


recursive()
print()
memoized()
print()
tabulation()