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


recursive()