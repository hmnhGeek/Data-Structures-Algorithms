# Problem link - https://www.naukri.com/code360/problems/ways-to-make-coin-change_630471?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=HgyouUi11zk&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=23


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


def tabulation():
    def coin_change_2(coins, target):
        n = len(coins)
        dp = {i: {j: 0 for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 1
        for j in dp[0]:
            if j % coins[0] == 0:
                dp[0][j] = 1

        for index in range(1, n):
            for tgt in range(1, target + 1):
                left = 0
                if coins[index] <= tgt:
                    left = dp[index][tgt - coins[index]]
                right = dp[index - 1][tgt]
                dp[index][tgt] = left + right
        return dp[n - 1][target]

    print(coin_change_2([3, 1, 2], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))


def space_optimized():
    def coin_change_2(coins, target):
        n = len(coins)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        for j in prev:
            if j % coins[0] == 0:
                prev[j] = 1

        for index in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for tgt in range(1, target + 1):
                left = 0
                if coins[index] <= tgt:
                    left = curr[tgt - coins[index]]
                right = prev[tgt]
                curr[tgt] = left + right
            prev = curr
        return prev[target]

    print(coin_change_2([3, 1, 2], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()