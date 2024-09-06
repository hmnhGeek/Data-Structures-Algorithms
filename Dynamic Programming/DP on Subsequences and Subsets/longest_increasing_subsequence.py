def recursive():
    def solve(arr, index, length, max_val):
        # Time complexity is O(2^n) and space complexity is O(n).

        # if the index 0 is reached
        if index == 0:
            # check if the 0th element is less than the max value stored till now, if yes,
            # then return length + 1 because 0th element will also be included. Note that
            # we are doing `<` and not `<=` because we will be taking only strictly increasing
            # subsequence.
            if arr[0] < max_val:
                return length + 1

            # otherwise simply return length
            return length

        # now assume that the left recursion is not possible.
        left = float('-inf')

        # check if the value at current index is less than the max value. If yes, then
        # this index value can be taken into consideration.
        if arr[index] < max_val:
            # take this index value and increase the length. Also, update the max value
            # with the current index value.
            left = solve(arr, index - 1, length + 1, arr[index])

        # if we don't pick the current index in the sequence, then go to next index, with
        # same length and same max value.
        right = solve(arr, index - 1, length, max_val)
        return max(left, right)

    def get_length_of_longest_increasing_subsequence(arr):
        # Time complexity is O(2^n) and space complexity is O(n).

        n = len(arr)
        # assuming that you've got current max value as infinite start with last index
        # with the longest increasing subsequence length of 0.
        return solve(arr, n - 1, 0, float('inf'))

    print(get_length_of_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_length_of_longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(get_length_of_longest_increasing_subsequence([1, 2, 2]))
    print(get_length_of_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))
    print(get_length_of_longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))


def get_value(arr, index):
    # function to handle edge case of prev_index in below solution.
    if index is None:
        return float('inf')
    if index >= len(arr):
        return float('inf')
    return arr[index]


def recursive1():
    def solve(arr, index, prev_index):
        # Time complexity is O(2^n) and space complexity is O(n).

        # if the index 0 is reached
        if index == 0:
            # check if the 0th element is less than the max value stored till now, if yes,
            # then return 1 because 0th element will also be included. Note that we are
            # doing `<` and not `<=` because we will be taking only strictly increasing
            # subsequence.
            if arr[0] < get_value(arr, prev_index):
                return 1

            # otherwise simply return 0
            return 0

        # now assume that the left recursion is not possible.
        left = float('-inf')

        # check if the value at current index is less than the max value. If yes, then
        # this index value can be taken into consideration.
        if arr[index] < get_value(arr, prev_index):
            # take this index value and increase the length. Also, update the max value
            # with the current index value.
            left = 1 + solve(arr, index - 1, index)

        # if we don't pick the current index in the sequence, then go to next index, with
        # same length and same max value.
        right = solve(arr, index - 1, prev_index)
        return max(left, right)

    def get_length_of_longest_increasing_subsequence(arr):
        # Time complexity is O(2^n) and space complexity is O(n).

        n = len(arr)
        # assuming that you've got current max value as infinite start with last index
        # with the longest increasing subsequence length of 0.
        return solve(arr, n - 1, None)

    print(get_length_of_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_length_of_longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(get_length_of_longest_increasing_subsequence([1, 2, 2]))
    print(get_length_of_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))
    print(get_length_of_longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))


def memoized():
    def solve(arr, index, prev_index, dp):
        # Time complexity is O(n^2) and space complexity is O(n + n^2).

        # if the index 0 is reached
        if index == 0:
            # check if the 0th element is less than the max value stored till now, if yes,
            # then return 1 because 0th element will also be included. Note that we are
            # doing `<` and not `<=` because we will be taking only strictly increasing
            # subsequence.
            if arr[0] < get_value(arr, prev_index):
                return 1

            # otherwise simply return 0
            return 0

        if dp[index][prev_index] is not None:
            return dp[index][prev_index]

        # now assume that the left recursion is not possible.
        left = float('-inf')

        # check if the value at current index is less than the max value. If yes, then
        # this index value can be taken into consideration.
        if arr[index] < get_value(arr, prev_index):
            # take this index value and increase the length. Also, update the max value
            # with the current index value.
            left = 1 + solve(arr, index - 1, index, dp)

        # if we don't pick the current index in the sequence, then go to next index, with
        # same length and same max value.
        right = solve(arr, index - 1, prev_index, dp)
        dp[index][prev_index] = max(left, right)
        return dp[index][prev_index]

    def get_length_of_longest_increasing_subsequence(arr):
        # Time complexity is O(n^2) and space complexity is O(n + n^2).

        n = len(arr)

        # create a DP array
        dp = {i: {j: None for j in range(n)} for i in range(n)}
        # introduce a None key for each index.
        for i in dp:
            dp[i][None] = None

        # assuming that you've got current max value as infinite start with last index
        # with the longest increasing subsequence length of 0.
        return solve(arr, n - 1, None, dp)

    print(get_length_of_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_length_of_longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(get_length_of_longest_increasing_subsequence([1, 2, 2]))
    print(get_length_of_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))
    print(get_length_of_longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))


def tabulation():
    def get_length_of_longest_increasing_subsequence(arr):
        # Time complexity is O(n^2) and space complexity is O(n^2).

        n = len(arr)

        # create a DP array
        dp = {i: {j: 0 for j in range(n)} for i in range(n)}
        # introduce a None key for each index.
        for i in dp:
            dp[i][None] = 0

        for j in dp[0]:
            dp[0][j] = 1 if arr[0] < get_value(arr, j) else 0

        for index in range(1, n):
            # For every index, specifically do a `None` prev_index code run

            # now assume that the left recursion is not possible.
            left = float('-inf')

            # check if the value at current index is less than the max value. If yes, then
            # this index value can be taken into consideration.
            if arr[index] < get_value(arr, None):
                # take this index value and increase the length. Also, update the max value
                # with the current index value.
                left = 1 + dp[index - 1][index]

            # if we don't pick the current index in the sequence, then go to next index, with
            # same length and same max value.
            right = dp[index - 1][None]
            dp[index][None] = max(left, right)

            # since prev_index = None is done, now populate for j = 0 to n - 1.
            for prev_index in range(n):
                # now assume that the left recursion is not possible.
                left = float('-inf')

                # check if the value at current index is less than the max value. If yes, then
                # this index value can be taken into consideration.
                if arr[index] < get_value(arr, prev_index):
                    # take this index value and increase the length. Also, update the max value
                    # with the current index value.
                    left = 1 + dp[index - 1][index]

                # if we don't pick the current index in the sequence, then go to next index, with
                # same length and same max value.
                right = dp[index - 1][prev_index]
                dp[index][prev_index] = max(left, right)

        # assuming that you've got current max value as infinite start with last index
        # with the longest increasing subsequence length of 0.
        return dp[n - 1][None]

    print(get_length_of_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_length_of_longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(get_length_of_longest_increasing_subsequence([1, 2, 2]))
    print(get_length_of_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))
    print(get_length_of_longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))


recursive()
print()
recursive1()
print()
memoized()
print()
tabulation()