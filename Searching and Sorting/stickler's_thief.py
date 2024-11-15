def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, index):
        if index < 0:
            return 0
        # if thief wants to steal from `index`, skip the immediate next index.
        left = arr[index] + solve(arr, index - 2)
        # if the thief does not steal from current index, move to the next index.
        right = solve(arr, index - 1)
        # return the max loot.
        return max(left, right)

    def stickler(arr):
        n = len(arr)
        return solve(arr, n - 1)

    print(stickler([6, 5, 5, 7, 4]))
    print(stickler([1, 5, 3]))
    print(stickler([4, 4, 4, 4]))
    print(stickler([6, 7, 1, 3, 8, 2, 4]))
    print(stickler([5, 3, 4, 11, 2]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(n + n).
    """

    def solve(arr, index, dp):
        if index < 0:
            return 0

        if dp[index] is not None:
            return dp[index]

        # if thief wants to steal from `index`, skip the immediate next index.
        left = arr[index] + solve(arr, index - 2, dp)
        # if the thief does not steal from current index, move to the next index.
        right = solve(arr, index - 1, dp)
        # return the max loot.
        dp[index] = max(left, right)
        return dp[index]

    def stickler(arr):
        n = len(arr)
        dp = {i: None for i in range(n + 1)}
        return solve(arr, n - 1, dp)

    print(stickler([6, 5, 5, 7, 4]))
    print(stickler([1, 5, 3]))
    print(stickler([4, 4, 4, 4]))
    print(stickler([6, 7, 1, 3, 8, 2, 4]))
    print(stickler([5, 3, 4, 11, 2]))


recursive()
print()
memoized()