def recursive():
    """
        T: O(2^n) and S: O(n)
    """
    def solve(arr, index, target):
        if target == 0:
            return 1
        if index == 0:
            return 1 if target % arr[0] == 0 else 0
        left = 0
        if arr[index] <= target:
            left = solve(arr, index, target - arr[index])
        right = solve(arr, index - 1, target)
        return left + right

    def coin_change_2(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(coin_change_2([1, 2, 3], 4))


def memoized():
    """
        T: O(nk) and S: O(n + nk)
    """
    def solve(arr, index, target, dp):
        if target == 0:
            return 1
        if index == 0:
            return 1 if target % arr[0] == 0 else 0
        if dp[index][target] is not None:
            return dp[index][target]
        left = 0
        if arr[index] <= target:
            left = solve(arr, index, target - arr[index], dp)
        right = solve(arr, index - 1, target, dp)
        dp[index][target] = left + right
        return dp[index][target]

    def coin_change_2(arr, k):
        n = len(arr)
        dp = {i: {j: None for j in range(k + 1)} for i in range(n)}
        return solve(arr, n - 1, k, dp)

    print(coin_change_2([1, 2, 3], 4))


recursive()
print()
memoized()