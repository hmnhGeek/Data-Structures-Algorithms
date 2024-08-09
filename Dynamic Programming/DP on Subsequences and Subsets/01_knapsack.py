# Problem link - https://www.naukri.com/code360/problems/0-1-knapsack_920542?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=GqOmJHQZivw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=20

def recursive():
    def solve(item_weights, item_values, index, knapsack_wt):
        # Time complexity is O(2^n) and space complexity O(n).

        # if you've reached index 0, and if the weight of item at index 0 is still less than or
        # equal to the available weight, return the value of that item, else you cannot pick
        # this item and return 0.
        if index == 0:
            return item_values[0] if item_weights[0] <= knapsack_wt else 0

        # assuming that you cannot pick the item at index = `index` because it's weight is
        # still more than available weight (just assuming). We don't want to consider it in
        # the max() function.
        left = float('-inf')

        # if the item's weight at index = `index` is less than the available weight, pick
        # it up by adding its value and solve for one lesser index by reducing the available
        # weight.
        if item_weights[index] <= knapsack_wt:
            left = item_values[index] + solve(item_weights, item_values, index - 1, knapsack_wt - item_weights[index])

        # if you don't pick the item at index = `index`, move to lower index with same
        # available weight.
        right = solve(item_weights, item_values, index - 1, knapsack_wt)

        # return the maximum value that you can obtain from left or right.
        return max(left, right)

    def knapsack(knapsack_wt, item_weights, item_values):
        n = len(item_weights)

        # start from last index and go on till 0th index.
        return solve(item_weights, item_values, n - 1, knapsack_wt)


    print(
        knapsack(
            4,
            [4, 5, 1],
            [1, 2, 3]
        )
    )

    print(
        knapsack(
            3,
            [4, 5, 6],
            [1, 2, 3]
        )
    )

    print(
        knapsack(
            5,
            [1, 2, 4, 5],
            [5, 4, 8, 6]
        )
    )

    print(
        knapsack(
            10,
            [2, 1, 5, 3],
            [300, 200, 400, 500]
        )
    )

    print(
        knapsack(
            8,
            [1, 3, 5, 7],
            [2, 4, 7, 10]
        )
    )


def memoized():
    def solve(item_weights, item_values, index, knapsack_wt, dp):
        # Time complexity is O(n * knapsack_wt) and space complexity O(n + knapsack_wt*n).

        # if you've reached index 0, and if the weight of item at index 0 is still less than or
        # equal to the available weight, return the value of that item, else you cannot pick
        # this item and return 0.
        if index == 0:
            return item_values[0] if item_weights[0] <= knapsack_wt else 0

        if dp[index][knapsack_wt] is not None:
            return dp[index][knapsack_wt]

        # assuming that you cannot pick the item at index = `index` because it's weight is
        # still more than available weight (just assuming). We don't want to consider it in
        # the max() function.
        left = float('-inf')

        # if the item's weight at index = `index` is less than the available weight, pick
        # it up by adding its value and solve for one lesser index by reducing the available
        # weight.
        if item_weights[index] <= knapsack_wt:
            left = item_values[index] + solve(item_weights, item_values, index - 1, knapsack_wt - item_weights[index], dp)

        # if you don't pick the item at index = `index`, move to lower index with same
        # available weight.
        right = solve(item_weights, item_values, index - 1, knapsack_wt, dp)

        # return the maximum value that you can obtain from left or right.
        dp[index][knapsack_wt] = max(left, right)
        return dp[index][knapsack_wt]

    def knapsack(knapsack_wt, item_weights, item_values):
        n = len(item_weights)

        # initialize a 2D DP array with index, knapsack_wt as changing parameters.
        # we also want to include knapsack_wt in the array, so make it till knapsack_wt + 1.
        dp = {i: {j: None for j in range(knapsack_wt + 1)} for i in range(n)}

        # start from last index and go on till 0th index.
        return solve(item_weights, item_values, n - 1, knapsack_wt, dp)


    print(
        knapsack(
            4,
            [4, 5, 1],
            [1, 2, 3]
        )
    )

    print(
        knapsack(
            3,
            [4, 5, 6],
            [1, 2, 3]
        )
    )

    print(
        knapsack(
            5,
            [1, 2, 4, 5],
            [5, 4, 8, 6]
        )
    )

    print(
        knapsack(
            10,
            [2, 1, 5, 3],
            [300, 200, 400, 500]
        )
    )

    print(
        knapsack(
            8,
            [1, 3, 5, 7],
            [2, 4, 7, 10]
        )
    )


def tabulation():
    def knapsack(knapsack_wt, item_weights, item_values):
        # Time complexity is again O(n * knapsack_wt) and space complexity is O(n * knapsack_wt) with recursion stack
        # space being avoided.

        # store the number of items for later use.
        n = len(item_weights)

        # initialize a 2D DP array with index, knapsack_wt as changing parameters.
        # we also want to include knapsack_wt in the array, so make it till knapsack_wt + 1.
        dp = {i: {j: float('-inf') for j in range(knapsack_wt + 1)} for i in range(n)}

        # populate all the values with item_values[0] for index = 0 or 0 depending upon the available capacity at
        # index = 0.
        for available_capacity_at_index_0 in dp[0]:
            dp[0][available_capacity_at_index_0] = item_values[0] if item_weights[0] <= available_capacity_at_index_0 else 0

        # start from index = 1 as index = 0 is already covered in the base case.
        for index in range(1, n):
            for available_capacity in range(knapsack_wt + 1):
                # assuming that you cannot pick the item at index = `index` because it's weight is
                # still more than available weight (just assuming). We don't want to consider it in
                # the max() function.
                left = float('-inf')

                # if the item's weight at index = `index` is less than the available weight, pick
                # it up by adding its value and solve for one lesser index by reducing the available
                # weight.
                if item_weights[index] <= available_capacity:
                    left = item_values[index] + dp[index - 1][available_capacity - item_weights[index]]

                # if you don't pick the item at index = `index`, move to lower index with same
                # available weight.
                right = dp[index - 1][available_capacity]

                # update the maximum value that you can obtain from left or right.
                dp[index][available_capacity] = max(left, right)

        # the final answer always lies in the last index.
        return dp[n - 1][knapsack_wt]

    print(
        knapsack(
            4,
            [4, 5, 1],
            [1, 2, 3]
        )
    )

    print(
        knapsack(
            3,
            [4, 5, 6],
            [1, 2, 3]
        )
    )

    print(
        knapsack(
            5,
            [1, 2, 4, 5],
            [5, 4, 8, 6]
        )
    )

    print(
        knapsack(
            10,
            [2, 1, 5, 3],
            [300, 200, 400, 500]
        )
    )

    print(
        knapsack(
            8,
            [1, 3, 5, 7],
            [2, 4, 7, 10]
        )
    )


def space_optimized():
    def knapsack(knapsack_wt, item_weights, item_values):
        # Time complexity is again O(n * knapsack_wt) and space complexity is O(knapsack_wt) with recursion stack
        # space being avoided and only prev being used.

        # store the number of items for later use.
        n = len(item_weights)

        # initialize a 2D DP array with index, knapsack_wt as changing parameters.
        # we also want to include knapsack_wt in the array, so make it till knapsack_wt + 1.
        prev = {j: float('-inf') for j in range(knapsack_wt + 1)}

        # populate all the values with item_values[0] for index = 0 or 0 depending upon the available capacity at
        # index = 0.
        for available_capacity_at_index_0 in prev:
            prev[available_capacity_at_index_0] = item_values[0] if item_weights[0] <= available_capacity_at_index_0 else 0

        # start from index = 1 as index = 0 is already covered in the base case.
        for index in range(1, n):
            curr = {j: float('-inf') for j in range(knapsack_wt + 1)}
            for available_capacity in range(knapsack_wt + 1):
                # assuming that you cannot pick the item at index = `index` because it's weight is
                # still more than available weight (just assuming). We don't want to consider it in
                # the max() function.
                left = float('-inf')

                # if the item's weight at index = `index` is less than the available weight, pick
                # it up by adding its value and solve for one lesser index by reducing the available
                # weight.
                if item_weights[index] <= available_capacity:
                    left = item_values[index] + prev[available_capacity - item_weights[index]]

                # if you don't pick the item at index = `index`, move to lower index with same
                # available weight.
                right = prev[available_capacity]

                # update the maximum value that you can obtain from left or right.
                curr[available_capacity] = max(left, right)
            prev = curr

        # the final answer always lies in the prev index.
        return prev[knapsack_wt]

    print(
        knapsack(
            4,
            [4, 5, 1],
            [1, 2, 3]
        )
    )

    print(
        knapsack(
            3,
            [4, 5, 6],
            [1, 2, 3]
        )
    )

    print(
        knapsack(
            5,
            [1, 2, 4, 5],
            [5, 4, 8, 6]
        )
    )

    print(
        knapsack(
            10,
            [2, 1, 5, 3],
            [300, 200, 400, 500]
        )
    )

    print(
        knapsack(
            8,
            [1, 3, 5, 7],
            [2, 4, 7, 10]
        )
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