# Problem link - https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
# Solution - https://www.youtube.com/watch?v=7SBVnw7GSTk & https://www.youtube.com/watch?v=tZAa_jJ3SwQ


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, index, n):
        if index >= n - 1:
            return 0
        if arr[index] == 0:
            return 1e6

        min_steps = 1e6
        for i in range(1, arr[index] + 1):
            min_steps = min(min_steps, 1 + solve(arr, index + i, n))
        return min_steps

    def min_jumps(arr):
        n = len(arr)
        min_steps_found = solve(arr, 0, n)
        return min_steps_found if min_steps_found < 1e6 else -1

    print(min_jumps([1, 4, 3, 2, 6, 7]))
    print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    print(min_jumps([0, 10, 20]))
    print(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(min_jumps([2, 3, 1, 1, 4]))
    print(min_jumps([2, 3, 0, 1, 4]))


def memoized():
    """
        Time complexity is O(n*max(arr)) and space complexity is O(n + n).
    """

    def solve(arr, index, n, dp):
        if index >= n - 1:
            return 0
        if arr[index] == 0:
            return 1e6

        if dp[index] is not None:
            return dp[index]

        min_steps = 1e6
        for i in range(1, arr[index] + 1):
            min_steps = min(min_steps, 1 + solve(arr, index + i, n, dp))
        dp[index] = min_steps
        return dp[index]

    def min_jumps(arr):
        n = len(arr)
        dp = {i: None for i in range(n)}
        min_steps_found = solve(arr, 0, n, dp)
        return min_steps_found if min_steps_found < 1e6 else -1

    print(min_jumps([1, 4, 3, 2, 6, 7]))
    print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    print(min_jumps([0, 10, 20]))
    print(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(min_jumps([2, 3, 1, 1, 4]))
    print(min_jumps([2, 3, 0, 1, 4]))


def tabulation():
    """
        Time complexity is O(n*max(arr)) and space complexity is O(n).
    """
    def min_jumps(arr):
        n = len(arr)
        dp = {i: 1e6 for i in range(n)}
        for i in dp:
            if arr[i] == 0:
                dp[i] = 0
        dp[n - 1] = 0

        for index in range(n - 2, -1, -1):
            min_steps = 1e6
            for i in range(1, arr[index] + 1):
                if index + i in dp:
                    min_steps = min(min_steps, 1 + dp[index + i])
            dp[index] = min_steps

        min_steps_found = dp[0]
        return min_steps_found if min_steps_found < 1e6 else -1

    print(min_jumps([1, 4, 3, 2, 6, 7]))
    print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    print(min_jumps([0, 10, 20]))
    print(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(min_jumps([2, 3, 1, 1, 4]))
    print(min_jumps([2, 3, 0, 1, 4]))


def is_end_reachable(arr):
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    max_index_reachable = 0
    n = len(arr)
    for i in range(n):
        # if the current index is within max reachable index, then continue. It can become otherwise,
        # if there's a 0 in between. Then we must return a False.
        if i <= max_index_reachable:
            # if the next maximum jump can increase max reachable index, then update it.
            if arr[i] + i > max_index_reachable:
                max_index_reachable = arr[i] + i
        else:
            return False
    # return answer.
    return max_index_reachable >= n - 1


def min_jumps(arr):
    """
        Time complexity is O(n) and space complexity is O(1).
    """

    # if end is not reachable, return -1.
    if not is_end_reachable(arr):
        return -1

    # initialize jumps to 0.
    jumps = 0
    # initialize a window.
    left, right = 0, 0
    n = len(arr)

    # while the whole array is not traversed.
    while right < n - 1:
        # set the farthest point to 0.
        farthest = 0
        # loop for all the indices from left to right. And update the farthest index that can be reached while staying
        # at index `index`.
        for index in range(left, right + 1):
            farthest = max(farthest, index + arr[index])

        # switch to the next window.
        left = right + 1
        right = farthest

        # and update the number of jumps
        jumps += 1
    return jumps


recursive()
print()
memoized()
print()
tabulation()

print()
print()
print(min_jumps([1, 2, 3, 1, 1, 0, 2, 5]))
print(min_jumps([1, 2, 4, 1, 1, 0, 2, 5]))
print(min_jumps([1, 4, 3, 2, 6, 7]))
print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(min_jumps([0, 10, 20]))
print(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(min_jumps([2, 3, 1, 1, 4]))
print(min_jumps([2, 3, 0, 1, 4]))
