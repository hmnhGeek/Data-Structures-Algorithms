def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(words, i, prev_consumed_space, k):
        if i == len(words):
            return 0

        # if we stay on the same line with words[i] word
        cost_for_being_on_same_line = 1e6
        consumed_spaces = prev_consumed_space + 1 + words[i]
        if consumed_spaces <= k:
            cost_for_being_on_same_line = solve(words, i + 1, consumed_spaces, k)

        # if we move to the next line with words[i] word, then compute the cost by using previous consumed space and
        # place the current word in the next line.
        cost_for_switching_lines = (k - prev_consumed_space)**2 + solve(words, i + 1, words[i], k)

        # get the minimum cost out of both.
        return min(cost_for_being_on_same_line, cost_for_switching_lines)

    def word_wrap(words, k):
        n = len(words)
        # start with 1st word and place 0th word in the first line.
        return solve(words, 1, words[0], k)

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """
    def solve(words, i, prev_consumed_space, k, dp):
        if i == len(words):
            return 0

        if dp[i][prev_consumed_space] is not None:
            return dp[i][prev_consumed_space]

        # if we stay on the same line with words[i] word
        cost_for_being_on_same_line = 1e6
        consumed_spaces = prev_consumed_space + 1 + words[i]
        if consumed_spaces <= k:
            cost_for_being_on_same_line = solve(words, i + 1, consumed_spaces, k, dp)

        # if we move to the next line with words[i] word, then compute the cost by using previous consumed space and
        # place the current word in the next line.
        cost_for_switching_lines = (k - prev_consumed_space)**2 + solve(words, i + 1, words[i], k, dp)

        # get the minimum cost out of both.
        dp[i][prev_consumed_space] = min(cost_for_being_on_same_line, cost_for_switching_lines)
        return dp[i][prev_consumed_space]

    def word_wrap(words, k):
        n = len(words)
        # j will take `k` ordered values because previous consumed space cannot exceed k.
        dp = {i: {j: None for j in range(k + 1)} for i in range(n)}
        # start with 1st word and place 0th word in the first line.
        return solve(words, 1, words[0], k, dp)

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


def tabulation():
    """
        Time complexity is O(n*k) and space complexity is O(nk).
    """
    def word_wrap(words, k):
        n = len(words)
        # j will take `k` ordered values because previous consumed space cannot exceed k.
        dp = {i: {j: 1e6 for j in range(k + 1)} for i in range(n + 1)}
        for j in dp[n]:
            dp[n][j] = 0

        for i in range(n - 1, -1, -1):
            for prev_consumed_space in range(k + 1):
                # if we stay on the same line with words[i] word
                cost_for_being_on_same_line = 1e6
                consumed_spaces = prev_consumed_space + 1 + words[i]
                if consumed_spaces <= k:
                    cost_for_being_on_same_line = dp[i + 1][consumed_spaces]

                # if we move to the next line with words[i] word, then compute the cost by using previous consumed
                # space and place the current word in the next line.
                cost_for_switching_lines = (k - prev_consumed_space) ** 2 + dp[i + 1][words[i]]

                # get the minimum cost out of both.
                dp[i][prev_consumed_space] = min(cost_for_being_on_same_line, cost_for_switching_lines)
        # start with 1st word and place 0th word in the first line.
        return dp[1][words[0]]

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


def space_optimized():
    """
        Time complexity is O(n*k) and space complexity is O(k).
    """
    def word_wrap(words, k):
        n = len(words)
        # j will take `k` ordered values because previous consumed space cannot exceed k. The `nxt` denotes i == n base case.
        nxt = {j: 0 for j in range(k + 1)}

        # in space optimized code, go only till 0 and not -1. Why? Because nxt denotes next i value. In the result,
        # we want dp[1] which will come only when we stop at 0.
        for i in range(n - 1, 0, -1):
            curr = {j: 1e6 for j in range(k + 1)}
            for prev_consumed_space in range(k + 1):
                # if we stay on the same line with words[i] word
                cost_for_being_on_same_line = 1e6
                consumed_spaces = prev_consumed_space + 1 + words[i]
                if consumed_spaces <= k:
                    cost_for_being_on_same_line = nxt[consumed_spaces]

                # if we move to the next line with words[i] word, then compute the cost by using previous consumed
                # space and place the current word in the next line.
                cost_for_switching_lines = (k - prev_consumed_space) ** 2 + nxt[words[i]]

                # get the minimum cost out of both.
                curr[prev_consumed_space] = min(cost_for_being_on_same_line, cost_for_switching_lines)
            nxt = curr
        # start with 1st word and place 0th word in the first line.
        return nxt[words[0]]

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()