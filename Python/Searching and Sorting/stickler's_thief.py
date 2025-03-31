# Problem link - https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/


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
        dp = {i: None for i in range(n)}
        return solve(arr, n - 1, dp)

    print(stickler([6, 5, 5, 7, 4]))
    print(stickler([1, 5, 3]))
    print(stickler([4, 4, 4, 4]))
    print(stickler([6, 7, 1, 3, 8, 2, 4]))
    print(stickler([5, 3, 4, 11, 2]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def stickler(arr):
        n = len(arr)
        dp = {i: 0 for i in range(n)}
        dp[-1] = dp[-2] = 0
        for index in range(n):
            # if thief wants to steal from `index`, skip the immediate next index.
            left = arr[index] + dp[index - 2]
            # if the thief does not steal from current index, move to the next index.
            right = dp[index - 1]
            # return the max loot.
            dp[index] = max(left, right)
        return dp[n - 1]

    print(stickler([6, 5, 5, 7, 4]))
    print(stickler([1, 5, 3]))
    print(stickler([4, 4, 4, 4]))
    print(stickler([6, 7, 1, 3, 8, 2, 4]))
    print(stickler([5, 3, 4, 11, 2]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def stickler(arr):
        n = len(arr)
        prev1 = 0
        prev2 = 0
        for index in range(n):
            # if thief wants to steal from `index`, skip the immediate next index.
            left = arr[index] + prev2
            # if the thief does not steal from current index, move to the next index.
            right = prev1
            # return the max loot.
            curr = max(left, right)
            prev2 = prev1
            prev1 = curr
        return prev1

    print(stickler([6, 5, 5, 7, 4]))
    print(stickler([1, 5, 3]))
    print(stickler([4, 4, 4, 4]))
    print(stickler([6, 7, 1, 3, 8, 2, 4]))
    print(stickler([5, 3, 4, 11, 2]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
