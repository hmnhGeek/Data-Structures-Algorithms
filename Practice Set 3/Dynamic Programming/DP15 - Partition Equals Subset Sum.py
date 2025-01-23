def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, k):
        if k == 0:
            return True
        if i == 0:
            return arr[0] == k
        left = False
        if arr[i] <= k:
            left = solve(arr, i - 1, k - arr[i])
        right = solve(arr, i - 1, k)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """
    def solve(arr, i, k, dp):
        if k == 0:
            return True
        if i == 0:
            return arr[0] == k
        if dp[i][k] is not None:
            return dp[i][k]
        left = False
        if arr[i] <= k:
            left = solve(arr, i - 1, k - arr[i], dp)
        right = solve(arr, i - 1, k, dp)
        dp[i][k] = left or right
        return dp[i][k]

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


recursive()
print()
memoized()