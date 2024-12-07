# Problem link - https://www.geeksforgeeks.org/coin-change-dp-7/
# Solution - https://www.youtube.com/watch?v=HgyouUi11zk&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=23


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
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1,2,5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


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
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


def tabulation():
    """
        T: O(nk) and S: O(nk)
    """
    def coin_change_2(arr, k):
        n = len(arr)
        dp = {i: {j: 0 for j in range(k + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = 1 if j % arr[0] == 0 else 0
        for i in dp:
            dp[i][0] = 1
        for index in range(1, n):
            for target in range(k + 1):
                left = 0
                if arr[index] <= target:
                    left = dp[index][target - arr[index]]
                right = dp[index - 1][target]
                dp[index][target] = left + right
        return dp[n - 1][k]

    print(coin_change_2([1, 2, 3], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


def space_optimized():
    """
        T: O(nk) and S: O(k)
    """
    def coin_change_2(arr, k):
        n = len(arr)
        prev = {j: 0 for j in range(k + 1)}
        for j in prev:
            prev[j] = 1 if j % arr[0] == 0 else 0
        prev[0] = 1
        for index in range(1, n):
            curr = {j: 0 for j in range(k + 1)}
            curr[0] = 1
            for target in range(k + 1):
                left = 0
                if arr[index] <= target:
                    left = curr[target - arr[index]]
                right = prev[target]
                curr[target] = left + right
            prev = curr
        return prev[k]

    print(coin_change_2([1, 2, 3], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
