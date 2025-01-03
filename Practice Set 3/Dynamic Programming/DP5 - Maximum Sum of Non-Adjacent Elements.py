def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, index):
        if index < 0:
            return 0
        take = arr[index] + solve(arr, index - 2)
        not_take = solve(arr, index - 1)
        return max(take, not_take)

    def house_robber(arr):
        n = len(arr)
        return solve(arr, n - 1)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """

    def solve(arr, index, dp):
        if index < 0:
            return 0
        if dp[index] is not None:
            return dp[index]
        take = arr[index] + solve(arr, index - 2, dp)
        not_take = solve(arr, index - 1, dp)
        dp[index] = max(take, not_take)
        return dp[index]

    def house_robber(arr):
        n = len(arr)
        dp = {i: None for i in range(-2, n)}
        return solve(arr, n - 1, dp)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


recursive()
print()
memoized()