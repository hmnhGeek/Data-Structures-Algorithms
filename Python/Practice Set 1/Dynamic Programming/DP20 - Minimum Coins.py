# Problem link - https://www.naukri.com/code360/problems/minimum-elements_3843091?leftPanelTab=1%3Fsource%3Dyoutube&campaign=striver_dpseries
# Solution - https://www.youtube.com/watch?v=myPeWb3Y68A&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=21


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, index, target):
        if target == 0:
            return 0

        if index == 0:
            return target // arr[0] if target % arr[0] == 0 else 1e6

        left = 1e6
        if target >= arr[index]:
            left = 1 + solve(arr, index, target - arr[index])
        right = solve(arr, index - 1, target)
        return min(left, right)

    def minimum_coins(denominations, amount):
        num_denominations = len(denominations)
        num_coins = solve(denominations, num_denominations - 1, amount)
        return num_coins if num_coins != 1e6 else -1

    print(minimum_coins([1, 2, 3], 7))
    print(minimum_coins([12, 1, 3], 4))
    print(minimum_coins([1, 2], 11))
    print(minimum_coins([25, 10, 5], 30))
    print(minimum_coins([9, 6, 5, 1], 19))
    print(minimum_coins([5, 1], 0))
    print(minimum_coins([4, 6, 2], 5))


def memoized():
    """
        Time complexity is O(n*amount) and space complexity is O(n + n*amount).
    """
    def solve(arr, index, target, dp):
        if target == 0:
            return 0

        if index == 0:
            return target // arr[0] if target % arr[0] == 0 else 1e6

        if dp[index][target] is not None:
            return dp[index][target]

        left = 1e6
        if target >= arr[index]:
            left = 1 + solve(arr, index, target - arr[index], dp)
        right = solve(arr, index - 1, target, dp)
        dp[index][target] = min(left, right)
        return dp[index][target]

    def minimum_coins(denominations, amount):
        num_denominations = len(denominations)
        dp = {i: {j: None for j in range(amount + 1)} for i in range(num_denominations)}
        num_coins = solve(denominations, num_denominations - 1, amount, dp)
        return num_coins if num_coins != 1e6 else -1

    print(minimum_coins([1, 2, 3], 7))
    print(minimum_coins([12, 1, 3], 4))
    print(minimum_coins([1, 2], 11))
    print(minimum_coins([25, 10, 5], 30))
    print(minimum_coins([9, 6, 5, 1], 19))
    print(minimum_coins([5, 1], 0))
    print(minimum_coins([4, 6, 2], 5))


def tabulation():
    """
        Time complexity is O(n*amount) and space complexity is O(n*amount).
    """
    def minimum_coins(denominations, amount):
        num_denominations = len(denominations)
        dp = {i: {j: 1e6 for j in range(amount + 1)} for i in range(num_denominations)}
        for i in dp:
            dp[i][0] = 0
        for j in dp[0]:
            if j % denominations[0] == 0:
                dp[0][j] = j // denominations[0]

        for index in range(1, num_denominations):
            for target in range(1, amount + 1):
                left = 1e6
                if target >= denominations[index]:
                    left = 1 + dp[index][target - denominations[index]]
                right = dp[index - 1][target]
                dp[index][target] = min(left, right)

        num_coins = dp[num_denominations - 1][amount]
        return num_coins if num_coins != 1e6 else -1

    print(minimum_coins([1, 2, 3], 7))
    print(minimum_coins([12, 1, 3], 4))
    print(minimum_coins([1, 2], 11))
    print(minimum_coins([25, 10, 5], 30))
    print(minimum_coins([9, 6, 5, 1], 19))
    print(minimum_coins([5, 1], 0))
    print(minimum_coins([4, 6, 2], 5))


def space_optimized():
    """
        Time complexity is O(n*amount) and space complexity is O(amount).
    """
    def minimum_coins(denominations, amount):
        num_denominations = len(denominations)
        prev = {j: 1e6 for j in range(amount + 1)}
        prev[0] = 0
        for j in prev:
            if j % denominations[0] == 0:
                prev[j] = j // denominations[0]

        for index in range(1, num_denominations):
            curr = {j: 1e6 for j in range(amount + 1)}
            curr[0] = 0
            for target in range(1, amount + 1):
                left = 1e6
                if target >= denominations[index]:
                    left = 1 + curr[target - denominations[index]]
                right = prev[target]
                curr[target] = min(left, right)
            prev = curr

        num_coins = prev[amount]
        return num_coins if num_coins != 1e6 else -1

    print(minimum_coins([1, 2, 3], 7))
    print(minimum_coins([12, 1, 3], 4))
    print(minimum_coins([1, 2], 11))
    print(minimum_coins([25, 10, 5], 30))
    print(minimum_coins([9, 6, 5, 1], 19))
    print(minimum_coins([5, 1], 0))
    print(minimum_coins([4, 6, 2], 5))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()