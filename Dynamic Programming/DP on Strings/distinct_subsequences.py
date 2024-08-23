def recursive():
    def solve_num_distinct_subsequences(string, i, lookup, j):
        """
            Time complexity is exponential (2^n apx)
            Space complexity is O(n) where n is the length of string.
        """

        # if `j` became negative, this means we have looked for everything in lookup, and so we can
        # say that we have found an occurrence of lookup in string, return 1, irrespective of what
        # `i` is right now.
        if j < 0:
            return 1

        # if at any point there is nothing to left in string to compare (and j > 0), return 0.
        if i < 0:
            return 0

        # again, if the characters in both the strings match, then you've two options at this juncture:
        # 1. reduce indices of both and consider getting a match.
        # 2. reduce only `i` and stay at `j`, basically not considering `i` even though it's a match with `j`.
        if string[i] == lookup[j]:
            left = solve_num_distinct_subsequences(string, i - 1, lookup, j - 1)
            right = solve_num_distinct_subsequences(string, i - 1, lookup, j)
            # return the sum of distinct subsequences so obtained.
            return left + right

        # if there is not a match, you have no option but to stay at same `j` but move lower on `i`.
        return solve_num_distinct_subsequences(string, i - 1, lookup, j)

    def get_distinct_subsequences(string, lookup):
        n = len(string)
        m = len(lookup)
        return solve_num_distinct_subsequences(string, n - 1, lookup, m - 1)

    print(get_distinct_subsequences("brootgroot", "brt"))
    print(get_distinct_subsequences("dingdingdingding", "ing"))
    print(get_distinct_subsequences("aaaaa", "a"))


def memoized():
    def solve_num_distinct_subsequences(string, i, lookup, j, dp):
        """
            Time complexity is O(m*n)
            Space complexity is O(n + m*n) where n is the length of string and m is the length of lookup.
        """

        # if `j` became negative, this means we have looked for everything in lookup, and so we can
        # say that we have found an occurrence of lookup in string, return 1, irrespective of what
        # `i` is right now.
        if j < 0:
            return 1

        # if at any point there is nothing to left in string to compare (and j > 0), return 0.
        if i < 0:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        # again, if the characters in both the strings match, then you've two options at this juncture:
        # 1. reduce indices of both and consider getting a match.
        # 2. reduce only `i` and stay at `j`, basically not considering `i` even though it's a match with `j`.
        if string[i] == lookup[j]:
            left = solve_num_distinct_subsequences(string, i - 1, lookup, j - 1, dp)
            right = solve_num_distinct_subsequences(string, i - 1, lookup, j, dp)
            # return the sum of distinct subsequences so obtained.
            dp[i][j] = left + right
        # if there is not a match, you have no option but to stay at same `j` but move lower on `i`.
        else:
            dp[i][j] = solve_num_distinct_subsequences(string, i - 1, lookup, j, dp)
        return dp[i][j]

    def get_distinct_subsequences(string, lookup):
        n = len(string)
        m = len(lookup)
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve_num_distinct_subsequences(string, n - 1, lookup, m - 1, dp)

    print(get_distinct_subsequences("brootgroot", "brt"))
    print(get_distinct_subsequences("dingdingdingding", "ing"))
    print(get_distinct_subsequences("aaaaa", "a"))

