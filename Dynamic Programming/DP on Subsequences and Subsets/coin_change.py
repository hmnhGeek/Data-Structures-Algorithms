# Problem link - https://www.naukri.com/code360/problems/ways-to-make-coin-change_630471?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=HgyouUi11zk&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=24

def recursive():
    def solve(coins, index, target_amount):
        # Time complexity is >= O(2^n) and space complexity is >= O(n) because same coin can be used multiple times.

        # if you've reached index 0, check if the 1st coin can make the target amount or not by
        # using the modulus operator. If yes, we have found one way to make the amount through
        # the recursion tree. Else return 0.
        if index == 0:
            return 1 if target_amount % coins[0] == 0 else 0

        # if at any point, target becomes 0, you must return 1, because it means that even before
        # reaching the index 0, you were able to make the full amount by using coins from the array.
        if target_amount == 0:
            return 1

        # assume that we cannot take the coin at index = `index`
        take = 0

        # now check if the index coin is less than or equal to the target amount or not. If it is,
        # then it means that we can use this coin to arrive at the target amount. Update the `take`
        # scenario and remain on the same index, because we have infinite supply of coins. Who knows
        # that in the next recursion on the same index, we can again use this coin to reduce the
        # amount.
        if coins[index] <= target_amount:
            take = solve(coins, index, target_amount - coins[index])

        # in not_take scenario it is simple. Simply move to the next lower index with same target amount.
        not_take = solve(coins, index - 1, target_amount)

        # finally, return total possibilities of using this coin at index = `index` to arrive at
        # the target amount.
        return take + not_take

    def coin_change(coins, target_amount):
        n = len(coins)
        return solve(coins, n - 1, target_amount)

    print(coin_change([1, 2, 3], 4))
    print(coin_change([1, 2, 5], 5))
    print(coin_change([5, 3, 2], 1))
    print(coin_change([2], 3))
    print(coin_change([8, 3, 1, 2], 3))
    print(coin_change([2, 5, 3, 6], 10))


def memoized():
    def solve(coins, index, target_amount, dp):
        # Time complexity is >= O(n * target_amount) and space complexity is >= O(n * target_amount + n) because same
        # coin can be used multiple times.

        # if you've reached index 0, check if the 1st coin can make the target amount or not by
        # using the modulus operator. If yes, we have found one way to make the amount through
        # the recursion tree. Else return 0.
        if index == 0:
            return 1 if target_amount % coins[0] == 0 else 0

        # if at any point, target becomes 0, you must return 1, because it means that even before
        # reaching the index 0, you were able to make the full amount by using coins from the array.
        if target_amount == 0:
            return 1

        if dp[index][target_amount] is not None:
            return dp[index][target_amount]

        # assume that we cannot take the coin at index = `index`
        take = 0

        # now check if the index coin is less than or equal to the target amount or not. If it is,
        # then it means that we can use this coin to arrive at the target amount. Update the `take`
        # scenario and remain on the same index, because we have infinite supply of coins. Who knows
        # that in the next recursion on the same index, we can again use this coin to reduce the
        # amount.
        if coins[index] <= target_amount:
            take = solve(coins, index, target_amount - coins[index], dp)

        # in not_take scenario it is simple. Simply move to the next lower index with same target amount.
        not_take = solve(coins, index - 1, target_amount, dp)

        # finally, return total possibilities of using this coin at index = `index` to arrive at
        # the target amount.
        dp[index][target_amount] = take + not_take
        return dp[index][target_amount]

    def coin_change(coins, target_amount):
        n = len(coins)
        dp = {i: {j: None for j in range(target_amount + 1)} for i in range(n)}
        return solve(coins, n - 1, target_amount, dp)

    print(coin_change([1, 2, 3], 4))
    print(coin_change([1, 2, 5], 5))
    print(coin_change([5, 3, 2], 1))
    print(coin_change([2], 3))
    print(coin_change([8, 3, 1, 2], 3))
    print(coin_change([2, 5, 3, 6], 10))


def tabulation():
    def coin_change(coins, target_amount):
        # Time complexity will be >= O(n * target_amount) and space complexity would also be >= O(n * target_amount)

        n = len(coins)
        dp = {i: {j: 0 for j in range(target_amount + 1)} for i in range(n)}

        # ensure that at 0th coin can be used to make target amount or not.
        for tgt in dp[0]:
            dp[0][tgt] = 1 if tgt % coins[0] == 0 else 0

        # at any index, if target amount becomes zero, there is one way to form the original target amount.
        for index in dp:
            dp[index][0] = 1

        for index in range(1, n):
            for target in range(target_amount + 1):
                # assume that we cannot take the coin at index = `index`
                take = 0

                # now check if the index coin is less than or equal to the target amount or not. If it is,
                # then it means that we can use this coin to arrive at the target amount. Update the `take`
                # scenario and remain on the same index, because we have infinite supply of coins. Who knows
                # that in the next recursion on the same index, we can again use this coin to reduce the
                # amount.
                if coins[index] <= target:
                    take = dp[index][target - coins[index]]

                # in not_take scenario it is simple. Simply move to the next lower index with same target amount.
                not_take = dp[index - 1][target]

                # finally, return total possibilities of using this coin at index = `index` to arrive at
                # the target amount.
                dp[index][target] = take + not_take

        return dp[n - 1][target_amount]

    print(coin_change([1, 2, 3], 4))
    print(coin_change([1, 2, 5], 5))
    print(coin_change([5, 3, 2], 1))
    print(coin_change([2], 3))
    print(coin_change([8, 3, 1, 2], 3))
    print(coin_change([2, 5, 3, 6], 10))


def space_optimized():
    def coin_change(coins, target_amount):
        # Time complexity will be >= O(n * target_amount) and space complexity would also be >= O(target_amount)

        n = len(coins)

        # initialize a prev row to represent the 0th coin.
        prev = {j: 0 for j in range(target_amount + 1)}

        # ensure that at 0th coin can be used to make target amount or not.
        for tgt in prev:
            prev[tgt] = 1 if tgt % coins[0] == 0 else 0

        # since index = 0 has been already defined in prev, start from index = 1.
        for index in range(1, n):
            curr = {j: 0 for j in range(target_amount + 1)}
            for target in range(target_amount + 1):
                # assume that we cannot take the coin at index = `index`
                take = 0

                # now check if the index coin is less than or equal to the target amount or not. If it is,
                # then it means that we can use this coin to arrive at the target amount. Update the `take`
                # scenario and remain on the same index, because we have infinite supply of coins. Who knows
                # that in the next recursion on the same index, we can again use this coin to reduce the
                # amount.
                if coins[index] <= target:
                    take = curr[target - coins[index]]

                # in not_take scenario it is simple. Simply move to the next lower index with same target amount.
                not_take = prev[target]

                # finally, return total possibilities of using this coin at index = `index` to arrive at
                # the target amount.
                curr[target] = take + not_take
            prev = curr

        return prev[target_amount]

    print(coin_change([1, 2, 3], 4))
    print(coin_change([1, 2, 5], 5))
    print(coin_change([5, 3, 2], 1))
    print(coin_change([2], 3))
    print(coin_change([8, 3, 1, 2], 3))
    print(coin_change([2, 5, 3, 6], 10))


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