# Problem link - https://www.geeksforgeeks.org/word-wrap-problem-dp-19/
# Solution - https://www.youtube.com/watch?v=1oKMVPryX18&t=655s


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def word_wrap(arr, k):
        return solve(1, arr[0], arr, k)

    def solve(i, consumed_spaces, arr, k):
        if i == len(arr):
            return 0

        # staying on the same line
        stays_on_same_line = 1e6
        new_consumed_spaces = consumed_spaces + 1 + arr[i]
        if new_consumed_spaces <= k:
            stays_on_same_line = solve(i + 1, new_consumed_spaces, arr, k)

        # moving to the next line
        moving_to_next_line = (k - consumed_spaces)**2 + solve(i + 1, arr[i], arr, k)
        return min(stays_on_same_line, moving_to_next_line)

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


def memoized():
    """
        Time complexity is O(nk) and space complexity is O(n + nk).
    """
    def word_wrap(arr, k):
        dp = {i: {j: None for j in range(k + 1)} for i in range(len(arr))}
        return solve(1, arr[0], arr, k, dp)

    def solve(i, consumed_spaces, arr, k, dp):
        if i == len(arr):
            return 0

        if dp[i][consumed_spaces] is not None:
            return dp[i][consumed_spaces]

        # staying on the same line
        stays_on_same_line = 1e6
        new_consumed_spaces = consumed_spaces + 1 + arr[i]
        if new_consumed_spaces <= k:
            stays_on_same_line = solve(i + 1, new_consumed_spaces, arr, k, dp)

        # moving to the next line
        moving_to_next_line = (k - consumed_spaces)**2 + solve(i + 1, arr[i], arr, k, dp)
        dp[i][consumed_spaces] = min(stays_on_same_line, moving_to_next_line)
        return dp[i][consumed_spaces]

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


def tabulation():
    """
        Time complexity is O(nk) and space complexity is O(k).
    """
    def word_wrap(arr, k):
        dp = {i: {j: 1e6 for j in range(k + 1)} for i in range(len(arr) + 1)}
        for j in range(k + 1):
            dp[len(arr)][j] = 0

        for i in range(len(arr) - 1, -1, -1):
            for j in range(k + 1):
                # staying on the same line
                stays_on_same_line = 1e6
                new_consumed_spaces = j + 1 + arr[i]
                if new_consumed_spaces <= k:
                    stays_on_same_line = dp[i + 1][new_consumed_spaces]

                # moving to the next line
                moving_to_next_line = (k - j) ** 2 + dp[i + 1][arr[i]]
                dp[i][j] = min(stays_on_same_line, moving_to_next_line)
        return dp[1][arr[0]]

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


def space_optimized():
    """
        Time complexity is O(nk) and space complexity is O(nk).
    """
    def word_wrap(arr, k):
        nxt = {j: 0 for j in range(k + 1)}
        for i in range(len(arr) - 1, 0, -1):
            curr = {j: 1e6 for j in range(k + 1)}
            for j in range(k + 1):
                # staying on the same line
                stays_on_same_line = 1e6
                new_consumed_spaces = j + 1 + arr[i]
                if new_consumed_spaces <= k:
                    stays_on_same_line = nxt[new_consumed_spaces]

                # moving to the next line
                moving_to_next_line = (k - j) ** 2 + nxt[arr[i]]
                curr[j] = min(stays_on_same_line, moving_to_next_line)
            nxt = curr
        return nxt[arr[0]]

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
