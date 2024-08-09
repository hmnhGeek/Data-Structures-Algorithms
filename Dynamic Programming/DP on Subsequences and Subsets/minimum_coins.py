# Problem link - https://www.naukri.com/code360/problems/minimum-elements_3843091?leftPanelTab=1%3Fsource%3Dyoutube&campaign=striver_dpseries
# Solution - https://www.youtube.com/watch?v=myPeWb3Y68A&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=22

def recursive():
    def solve(denominations, index, target_amount):
        # Time complexity is >= O(2^n) and space is >= O(n) because we might stand at the same
        # index in multiple calls.

        # if target amount becomes 0, no need to check further. we don't need any coins now.
        if target_amount == 0:
            return 0

        # if you're at index 0, and the denomination at index 0 can divide the target amount,
        # then that many coins of denomination[0] will be needed, else return infinite so that
        # in the min() function, we get correct answer.
        if index == 0:
            if target_amount % denominations[0] == 0:
                return target_amount // denominations[0]
            return float('inf')

        # assuming that we cannot take the coin at this index, store take case as infinite.
        # if the coin at index is less than or equal to the target amount, we can take this
        # coin. Increase the answer by 1 and solve on same index by reducing the target, because
        # same coin can be picked up multiple times.
        take = float('inf')
        if denominations[index] <= target_amount:
            take = 1 + solve(denominations, index, target_amount - denominations[index])

        # if you're not taking this coin, it is straight-forward, simply move to lower index
        # with same target amount.
        not_take = solve(denominations, index - 1, target_amount)

        # return the minimum of take and not-take case.
        return min(take, not_take)

    def min_coins(denominations, target_amount):
        n = len(denominations)
        return solve(denominations, n - 1, target_amount)

    print(
        min_coins([1, 2, 3], 7)
    )

    print(
        min_coins([1, 0], 0)
    )

    print(
        min_coins([12, 1, 3], 4)
    )

    print(
        min_coins([2, 1], 11)
    )


def memoized():
    def solve(denominations, index, target_amount, dp):
        # Time complexity is >= O(n * target_amount) and space is >= O(n + n * target_amount)
        # because we might stand at the same index in multiple calls.

        # if target amount becomes 0, no need to check further. we don't need any coins now.
        if target_amount == 0:
            return 0

        # if you're at index 0, and the denomination at index 0 can divide the target amount,
        # then that many coins of denomination[0] will be needed, else return infinite so that
        # in the min() function, we get correct answer.
        if index == 0:
            if target_amount % denominations[0] == 0:
                return target_amount // denominations[0]
            return float('inf')

        if dp[index][target_amount] is not None:
            return dp[index][target_amount]

        # assuming that we cannot take the coin at this index, store take case as infinite.
        # if the coin at index is less than or equal to the target amount, we can take this
        # coin. Increase the answer by 1 and solve on same index by reducing the target, because
        # same coin can be picked up multiple times.
        take = float('inf')
        if denominations[index] <= target_amount:
            take = 1 + solve(denominations, index, target_amount - denominations[index], dp)

        # if you're not taking this coin, it is straight-forward, simply move to lower index
        # with same target amount.
        not_take = solve(denominations, index - 1, target_amount, dp)

        # return the minimum of take and not-take case.
        dp[index][target_amount] = min(take, not_take)
        return dp[index][target_amount]

    def min_coins(denominations, target_amount):
        n = len(denominations)
        dp = {i: {j: None for j in range(target_amount + 1)} for i in range(n)}
        return solve(denominations, n - 1, target_amount, dp)

    print(
        min_coins([1, 2, 3], 7)
    )

    print(
        min_coins([1, 0], 0)
    )

    print(
        min_coins([12, 1, 3], 4)
    )

    print(
        min_coins([2, 1], 11)
    )


def tabulation():
    def min_coins(denominations, target_amount):
        # Time is >= O(n * target_amount) and space is >= O(n * target_amount)
        n = len(denominations)
        dp = {i: {j: float('inf') for j in range(target_amount + 1)} for i in range(n)}

        # for all the indices, wherever target is 0, set the value of dp[index][0] to 0.
        for index in dp:
            dp[index][0] = 0

        # for all the target values at 0 index, if the target is divisible by 0th denomination, modify dp[0][target]
        # else leave it as infinite.
        for target in dp[0]:
            if target % denominations[0] == 0:
                dp[0][target] = target // denominations[0]

        # 0th index has been formed, start from index = 1
        for index in range(1, n):
            for target in range(target_amount + 1):
                # assuming that we cannot take the coin at this index, store take case as infinite.
                # if the coin at index is less than or equal to the target amount, we can take this
                # coin. Increase the answer by 1 and solve on same index by reducing the target, because
                # same coin can be picked up multiple times.
                take = float('inf')
                if denominations[index] <= target:
                    take = 1 + dp[index][target - denominations[index]]

                # if you're not taking this coin, it is straight-forward, simply move to lower index
                # with same target amount.
                not_take = dp[index - 1][target]

                # return the minimum of take and not-take case.
                dp[index][target] = min(take, not_take)

        return dp[n - 1][target_amount]

    print(
        min_coins([1, 2, 3], 7)
    )

    print(
        min_coins([1, 0], 0)
    )

    print(
        min_coins([12, 1, 3], 4)
    )

    print(
        min_coins([2, 1], 11)
    )


def space_optimized():
    def min_coins(denominations, target_amount):
        # Time is >= O(n * target_amount) and space is >= O(target_amount)
        n = len(denominations)
        prev = {j: float('inf') for j in range(target_amount + 1)}

        # for all the target values at 0 index, if the target is divisible by 0th denomination, modify dp[0][target]
        # else leave it as infinite.
        for target in prev:
            if target % denominations[0] == 0:
                prev[target] = target // denominations[0]

        # 0th index has been formed, start from index = 1
        for index in range(1, n):
            curr = {j: float('inf') for j in range(target_amount + 1)}
            for target in range(target_amount + 1):
                # assuming that we cannot take the coin at this index, store take case as infinite.
                # if the coin at index is less than or equal to the target amount, we can take this
                # coin. Increase the answer by 1 and solve on same index by reducing the target, because
                # same coin can be picked up multiple times.
                take = float('inf')
                if denominations[index] <= target:
                    take = 1 + curr[target - denominations[index]]

                # if you're not taking this coin, it is straight-forward, simply move to lower index
                # with same target amount.
                not_take = prev[target]

                # return the minimum of take and not-take case.
                curr[target] = min(take, not_take)
            prev = curr

        return prev[target_amount]

    print(
        min_coins([1, 2, 3], 7)
    )

    print(
        min_coins([1, 0], 0)
    )

    print(
        min_coins([12, 1, 3], 4)
    )

    print(
        min_coins([2, 1], 11)
    )


print("Recursive Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()