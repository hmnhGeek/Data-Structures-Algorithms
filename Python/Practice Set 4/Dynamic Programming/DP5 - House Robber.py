def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, i):
        if i < 0:
            return 0
        left = arr[i] + solve(arr, i - 2)
        right = solve(arr, i - 1)
        return max(left, right)

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
    def solve(arr, i, dp):
        if i < 0:
            return 0
        if dp[i] is not None:
            return dp[i]
        left = arr[i] + solve(arr, i - 2, dp)
        right = solve(arr, i - 1, dp)
        dp[i] = max(left, right)
        return dp[i]

    def house_robber(arr):
        n = len(arr)
        dp = {i: None for i in range(n)}
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