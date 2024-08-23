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


def tabulation():
    def get_distinct_subsequences(string, lookup):
        # Time complexity is O(n*m) and space is also O(n*m) with no recursion.

        n = len(string)
        m = len(lookup)
        dp = {i: {j: 0 for j in range(m)} for i in range(n)}

        # fill out first col, i.e., lookup[0] column. No need to fill row 0, i.e. string[0] row because for columns
        # j = 1 to m - 1, lookup[j] would basically mean that you're at index 0 of string but still lookup string has
        # at least one character left to compare, so all will be 0 in that case. However, the lookup[0] case will not
        # be so. In tabulation, we build from bottom to up.
        # set dp[0][0] meaning string[0] and lookup[0] to 1 if both of them are equal, meaning that we have 1
        # subsequence found. Now, we must add 1 to (dp[i - 1][j - 1] + dp[i - 1][j]), but j = 0. Hence, dp[i - 1][j - 1]
        # will always return 0. Hence, we have to add a 1 or a 0 only to dp[i - 1][j].
        # we will use recursion code above to write the base case.
        dp[0][0] = 1 if string[0] == lookup[0] else 0
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + (1 if string[i] == lookup[0] else 0)

        for i in range(1, n):
            for j in range(1, m):
                # again, if the characters in both the strings match, then you've two options at this juncture:
                # 1. reduce indices of both and consider getting a match.
                # 2. reduce only `i` and stay at `j`, basically not considering `i` even though it's a match with `j`.
                if string[i] == lookup[j]:
                    left = dp[i - 1][j - 1]
                    right = dp[i - 1][j]
                    # return the sum of distinct subsequences so obtained.
                    dp[i][j] = left + right
                # if there is not a match, you have no option but to stay at same `j` but move lower on `i`.
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][m - 1]

    print(get_distinct_subsequences("brootgroot", "brt"))
    print(get_distinct_subsequences("dingdingdingding", "ing"))
    print(get_distinct_subsequences("aaaaa", "a"))


def space_optimized():
    def get_distinct_subsequences(string, lookup):
        # Time complexity is O(n*m) and space is also O(m) with no recursion.

        n = len(string)
        m = len(lookup)

        # initialize prev representing the 0th index of string.
        prev = {j: 0 for j in range(m)}

        # fill out first col, i.e., lookup[0] column. No need to fill row 0, i.e. string[0] row because for columns
        # j = 1 to m - 1, lookup[j] would basically mean that you're at index 0 of string but still lookup string has
        # at least one character left to compare, so all will be 0 in that case. However, the lookup[0] case will not
        # be so. In tabulation, we build from bottom to up.
        # set prev[0] meaning string[0] and lookup[0] to 1 if both of them are equal, meaning that we have 1
        # subsequence found. Now, we must add 1 to (prev[j - 1] + prev[j]), but j = 0. Hence, prev[j - 1]
        # will always return 0. Hence, we have to add a 1 or a 0 only to prev[j].
        # we will use recursion code above to write the base case.
        prev[0] = 1 if string[0] == lookup[0] else 0

        for i in range(1, n):
            curr = {j: 0 for j in range(m)}
            curr[0] = prev[0] + (1 if string[i] == lookup[0] else 0)
            for j in range(1, m):
                # again, if the characters in both the strings match, then you've two options at this juncture:
                # 1. reduce indices of both and consider getting a match.
                # 2. reduce only `i` and stay at `j`, basically not considering `i` even though it's a match with `j`.
                if string[i] == lookup[j]:
                    left = prev[j - 1]
                    right = prev[j]
                    # return the sum of distinct subsequences so obtained.
                    curr[j] = left + right
                # if there is not a match, you have no option but to stay at same `j` but move lower on `i`.
                else:
                    curr[j] = prev[j]
            prev = curr

        return prev[m - 1]

    print(get_distinct_subsequences("brootgroot", "brt"))
    print(get_distinct_subsequences("dingdingdingding", "ing"))
    print(get_distinct_subsequences("aaaaa", "a"))
    print(get_distinct_subsequences("abc", "abc"))
    print(get_distinct_subsequences("rabbbit", "rabbit"))
    print(get_distinct_subsequences("geeksforgeeks", "ge"))
    print(get_distinct_subsequences("babgbag", "bag"))


memoized()
print()
space_optimized()