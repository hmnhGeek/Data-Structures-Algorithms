# Problem link - https://www.naukri.com/code360/problems/unbounded-knapsack_1215029?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=OgvOZ6OrJoY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=24

def recursive():
    def solve(item_weights, item_values, index, capacity):
        # Time complexity is >= O(2^n) and space is >= O(n) because we can have same index multiple times in the
        # recursion.

        # if you are able to reach index 0, check if you have capacity available.
        # if yes, return the value at index 0 multiplied by the maximum capacity utilization, which
        # is capacity // item_weights[0], else return 0 (the same formula can handle both cases).
        if index == 0:
            return (capacity // item_weights[0]) * item_values[0]

        # if capacity has become 0, you cannot pick further, return 0 value.
        if capacity == 0:
            return 0

        # assume that you cannot take the weight at index. initialize it with -infinite so that
        # in max() function you don't pick it, if it is really not picked by the check just below.
        take = float('-inf')

        # now, let us check if we have the capacity to bear this weight. If yes, add the value of this
        # weight and solve for the same index again by reducing the capacity. Remember, we have unlimited
        # supply of items, so we must remain at the same index if we take this index weight.
        if item_weights[index] <= capacity:
            take = item_values[index] + solve(item_weights, item_values, index, capacity - item_weights[index])

        # if we don't take the weight at this index, move to a lower index with same capacity.
        not_take = solve(item_weights, item_values, index - 1, capacity)

        # return the max value that can be extracted from the two cases.
        return max(take, not_take)

    def unlimited_knapsack(capacity, item_weights, item_values):
        n = len(item_weights)
        return solve(item_weights, item_values, n - 1, capacity)

    print(
        unlimited_knapsack(
            10,
            [2, 4, 6],
            [5, 11, 13]
        )
    )

    print(
        unlimited_knapsack(
            15,
            [5, 10, 20],
            [7, 2, 4]
        )
    )

    print(
        unlimited_knapsack(
            3,
            [4, 17],
            [6, 12]
        )
    )

    print(
        unlimited_knapsack(
            100,
            [1, 50],
            [1, 30]
        )
    )

    print(
        unlimited_knapsack(
            8,
            [1, 3, 4, 5],
            [10, 40, 50, 70]
        )
    )


def memoized():
    def solve(item_weights, item_values, index, capacity, dp):
        # Time complexity is >= O(n * capacity) and space is >= O(n * capacity + n) because we can have
        # same index multiple times in the recursion.

        # if you are able to reach index 0, check if you have capacity available.
        # if yes, return the value at index 0 multiplied by the maximum capacity utilization, which
        # is capacity // item_weights[0], else return 0 (the same formula can handle both cases).
        if index == 0:
            return (capacity // item_weights[0]) * item_values[0]

        # if capacity has become 0, you cannot pick further, return 0 value.
        if capacity == 0:
            return 0

        if dp[index][capacity] is not None:
            return dp[index][capacity]

        # assume that you cannot take the weight at index. initialize it with -infinite so that
        # in max() function you don't pick it, if it is really not picked by the check just below.
        take = float('-inf')

        # now, let us check if we have the capacity to bear this weight. If yes, add the value of this
        # weight and solve for the same index again by reducing the capacity. Remember, we have unlimited
        # supply of items, so we must remain at the same index if we take this index weight.
        if item_weights[index] <= capacity:
            take = item_values[index] + solve(item_weights, item_values, index, capacity - item_weights[index], dp)

        # if we don't take the weight at this index, move to a lower index with same capacity.
        not_take = solve(item_weights, item_values, index - 1, capacity, dp)

        # return the max value that can be extracted from the two cases.
        dp[index][capacity] = max(take, not_take)
        return dp[index][capacity]

    def unlimited_knapsack(capacity, item_weights, item_values):
        n = len(item_weights)
        dp = {i: {j: None for j in range(capacity + 1)} for i in range(n)}
        return solve(item_weights, item_values, n - 1, capacity, dp)

    print(
        unlimited_knapsack(
            10,
            [2, 4, 6],
            [5, 11, 13]
        )
    )

    print(
        unlimited_knapsack(
            15,
            [5, 10, 20],
            [7, 2, 4]
        )
    )

    print(
        unlimited_knapsack(
            3,
            [4, 17],
            [6, 12]
        )
    )

    print(
        unlimited_knapsack(
            100,
            [1, 50],
            [1, 30]
        )
    )

    print(
        unlimited_knapsack(
            8,
            [1, 3, 4, 5],
            [10, 40, 50, 70]
        )
    )


def tabulation():
    def unlimited_knapsack(capacity, item_weights, item_values):
        # Time complexity is O(n * capacity) and space complexity is O(n * capacity) with no recursion space.

        n = len(item_weights)
        dp = {i: {j: float('-inf') for j in range(capacity + 1)} for i in range(n)}

        # initialize the max value that can be obtained at index 0 for all the capacities (0 till `capacity`).
        for cap in dp[0]:
            dp[0][cap] = (cap // item_weights[0]) * item_values[0]

        # in all the indices, wherever capacity is 0, you will get 0 value.
        for index in dp:
            dp[index][0] = 0

        for index in range(1, n):
            for cap in range(capacity + 1):
                # assume that you cannot take the weight at index. initialize it with -infinite so that
                # in max() function you don't pick it, if it is really not picked by the check just below.
                take = float('-inf')

                # now, let us check if we have the capacity to bear this weight. If yes, add the value of this
                # weight and solve for the same index again by reducing the capacity. Remember, we have unlimited
                # supply of items, so we must remain at the same index if we take this index weight.
                if item_weights[index] <= cap:
                    take = item_values[index] + dp[index][cap - item_weights[index]]

                # if we don't take the weight at this index, move to a lower index with same capacity.
                not_take = dp[index - 1][cap]

                # return the max value that can be extracted from the two cases.
                dp[index][cap] = max(take, not_take)

        return dp[n - 1][capacity]

    print(
        unlimited_knapsack(
            10,
            [2, 4, 6],
            [5, 11, 13]
        )
    )

    print(
        unlimited_knapsack(
            15,
            [5, 10, 20],
            [7, 2, 4]
        )
    )

    print(
        unlimited_knapsack(
            3,
            [4, 17],
            [6, 12]
        )
    )

    print(
        unlimited_knapsack(
            100,
            [1, 50],
            [1, 30]
        )
    )

    print(
        unlimited_knapsack(
            8,
            [1, 3, 4, 5],
            [10, 40, 50, 70]
        )
    )


def space_optimized():
    def unlimited_knapsack(capacity, item_weights, item_values):
        # Time complexity is O(n * capacity) and space complexity is O(capacity) with no recursion space.

        n = len(item_weights)

        # initialize a prev row for 0th index.
        prev = {j: float('-inf') for j in range(capacity + 1)}

        # initialize the max value that can be obtained at index 0 for all the capacities (0 till `capacity`).
        for cap in prev:
            prev[cap] = (cap // item_weights[0]) * item_values[0]

        for index in range(1, n):
            curr = {j: float('-inf') for j in range(capacity + 1)}
            for cap in range(capacity + 1):
                # assume that you cannot take the weight at index. initialize it with -infinite so that
                # in max() function you don't pick it, if it is really not picked by the check just below.
                take = float('-inf')

                # now, let us check if we have the capacity to bear this weight. If yes, add the value of this
                # weight and solve for the same index again by reducing the capacity. Remember, we have unlimited
                # supply of items, so we must remain at the same index if we take this index weight.
                if item_weights[index] <= cap:
                    take = item_values[index] + curr[cap - item_weights[index]]

                # if we don't take the weight at this index, move to a lower index with same capacity.
                not_take = prev[cap]

                # return the max value that can be extracted from the two cases.
                curr[cap] = max(take, not_take)
            prev = curr

        return prev[capacity]

    print(
        unlimited_knapsack(
            10,
            [2, 4, 6],
            [5, 11, 13]
        )
    )

    print(
        unlimited_knapsack(
            15,
            [5, 10, 20],
            [7, 2, 4]
        )
    )

    print(
        unlimited_knapsack(
            3,
            [4, 17],
            [6, 12]
        )
    )

    print(
        unlimited_knapsack(
            100,
            [1, 50],
            [1, 30]
        )
    )

    print(
        unlimited_knapsack(
            8,
            [1, 3, 4, 5],
            [10, 40, 50, 70]
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