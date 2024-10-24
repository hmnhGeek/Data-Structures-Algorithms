def recursive():
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

    def coin_change_2(coins, target):
        n = len(coins)
        return solve(coins, n - 1, target)

    print(coin_change_2([3, 1, 2], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))


def memoized():
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

    def coin_change_2(coins, target):
        n = len(coins)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(coins, n - 1, target, dp)

    print(coin_change_2([3, 1, 2], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))


recursive()
print()
memoized()