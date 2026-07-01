def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def house_robber(arr):
        n = len(arr)
        return solve(arr, n - 1)

    def solve(arr, i):
        if i == -2 or i == -1:
            return 0
        take = arr[i] + solve(arr, i - 2)
        not_take = solve(arr, i - 1)
        return max(take, not_take)

    print(house_robber([6, 5, 5, 7, 4]))
    print(house_robber([1, 5, 3]))
    print(house_robber([4, 4, 4, 4]))
    print(house_robber([6, 7, 1, 3, 8, 2, 4]))
    print(house_robber([5, 3, 4, 11, 2]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """
    def house_robber(arr):
        n = len(arr)
        dp = {i: None for i in range(-2, n)}
        return solve(arr, n - 1, dp)

    def solve(arr, i, dp):
        if i == -2 or i == -1:
            return 0
        if dp[i] is not None:
            return dp[i]
        take = arr[i] + solve(arr, i - 2, dp)
        not_take = solve(arr, i - 1, dp)
        dp[i] = max(take, not_take)
        return dp[i]

    print(house_robber([6, 5, 5, 7, 4]))
    print(house_robber([1, 5, 3]))
    print(house_robber([4, 4, 4, 4]))
    print(house_robber([6, 7, 1, 3, 8, 2, 4]))
    print(house_robber([5, 3, 4, 11, 2]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def house_robber(arr):
        n = len(arr)
        dp = {i: 0 for i in range(-2, n)}
        for i in range(n):
            take = arr[i] + dp[i - 2]
            not_take = dp[i - 1]
            dp[i] = max(take, not_take)
        return dp[n - 1]

    print(house_robber([6, 5, 5, 7, 4]))
    print(house_robber([1, 5, 3]))
    print(house_robber([4, 4, 4, 4]))
    print(house_robber([6, 7, 1, 3, 8, 2, 4]))
    print(house_robber([5, 3, 4, 11, 2]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def house_robber(arr):
        n = len(arr)
        prev2 = prev = 0
        for i in range(n):
            take = arr[i] + prev2
            not_take = prev
            curr = max(take, not_take)
            prev2 = prev
            prev = curr
        return prev

    print(house_robber([6, 5, 5, 7, 4]))
    print(house_robber([1, 5, 3]))
    print(house_robber([4, 4, 4, 4]))
    print(house_robber([6, 7, 1, 3, 8, 2, 4]))
    print(house_robber([5, 3, 4, 11, 2]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
