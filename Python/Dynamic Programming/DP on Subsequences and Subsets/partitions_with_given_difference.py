# Problem link - https://www.naukri.com/code360/problems/partitions-with-given-difference_3751628?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=zoilQD1kYSg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=19

# This problem is same as the one solved in subset_sum_equals_k.py. The difference here is that we
# have to figure out the target ourselves this time.

def recursive():
    def f(arr, index, target):
        if index < 0:
            return 0
        if target < 0:
            return 0
        if target == 0:
            return 1
        if index == 0:
            return 1 if arr[0] == target else 0

        return f(arr, index - 1, target - arr[index]) + f(arr, index - 1, target)

    def get_count_with_subset_sum(arr, target):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1 if arr[0] == target else 0

        return f(arr, len(arr) - 1, target)

    def get_partitions_with_diff(arr, diff):
        # Given that s1 - s2 = diff >= 0 and s1 + s2 = sigma, we can say that we have to find
        # those subsets from the array where s1 = (sigma + diff)/2. Also, sigma + diff needs to be
        # divisible by 2 so that we can find such a subset. Apart from this, the whole problem
        # is same as the subset sum equals k problem. For time and space complexity analysis, refer
        # to that problem.
        sigma = sum(arr)
        if (sigma + diff) % 2 != 0:
            return 0

        target = (sigma + diff) // 2
        return get_count_with_subset_sum(arr, target)

    print(
        get_partitions_with_diff(
            [5, 2, 5, 1],
            3
        )
    )

    print(
        get_partitions_with_diff(
            [5, 2, 6, 4],
            3
        )
    )

    print(
        get_partitions_with_diff(
            [1, 1, 1, 1],
            0
        )
    )

    print(
        get_partitions_with_diff(
            [4, 6, 3],
            1
        )
    )

    print(
        get_partitions_with_diff(
            [3, 1, 1, 2, 1],
            0
        )
    )

    print(
        get_partitions_with_diff(
            [3, 2, 2, 5, 1],
            1
        )
    )


def memoized():
    def f(arr, index, target, dp):
        if index < 0:
            return 0
        if target < 0:
            return 0
        if target == 0:
            return 1
        if index == 0:
            return 1 if arr[0] == target else 0

        if target in dp[index] and dp[index][target] is not None:
            return dp[index][target]

        dp[index][target] = f(arr, index - 1, target - arr[index], dp) + f(arr, index - 1, target, dp)
        return dp[index][target]

    def get_count_with_subset_sum(arr, target):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1 if arr[0] == target else 0

        dp = {i: {tgt: None for tgt in range(target + 1)} for i in range(len(arr))}
        return f(arr, len(arr) - 1, target, dp)

    def get_partitions_with_diff(arr, diff):
        # Given that s1 - s2 = diff >= 0 and s1 + s2 = sigma, we can say that we have to find
        # those subsets from the array where s1 = (sigma + diff)/2. Also, sigma + diff needs to be
        # divisible by 2 so that we can find such a subset. Apart from this, the whole problem
        # is same as the subset sum equals k problem. For time and space complexity analysis, refer
        # to that problem.
        sigma = sum(arr)
        if (sigma + diff) % 2 != 0:
            return 0

        target = (sigma + diff) // 2
        return get_count_with_subset_sum(arr, target)

    print(
        get_partitions_with_diff(
            [5, 2, 5, 1],
            3
        )
    )

    print(
        get_partitions_with_diff(
            [5, 2, 6, 4],
            3
        )
    )

    print(
        get_partitions_with_diff(
            [1, 1, 1, 1],
            0
        )
    )

    print(
        get_partitions_with_diff(
            [4, 6, 3],
            1
        )
    )

    print(
        get_partitions_with_diff(
            [3, 1, 1, 2, 1],
            0
        )
    )

    print(
        get_partitions_with_diff(
            [3, 2, 2, 5, 1],
            1
        )
    )


def tabulation():
    def get_count_with_subset_sum(arr, target):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1 if arr[0] == target else 0

        dp = {i: {tgt: 0 for tgt in range(target + 1)} for i in range(len(arr))}
        for index in dp:
            dp[index][0] = 1

        dp[0][arr[0]] = 1

        for index in range(1, len(arr)):
            for tgt in range(target + 1):
                left, right = 0, 0

                if tgt - arr[index] in dp[index - 1]:
                    left = dp[index - 1][tgt - arr[index]]
                if tgt in dp[index - 1]:
                    right = dp[index - 1][tgt]

                dp[index][tgt] = left + right

        return dp[len(arr) - 1][target]

    def get_partitions_with_diff(arr, diff):
        # Given that s1 - s2 = diff >= 0 and s1 + s2 = sigma, we can say that we have to find
        # those subsets from the array where s1 = (sigma + diff)/2. Also, sigma + diff needs to be
        # divisible by 2 so that we can find such a subset. Apart from this, the whole problem
        # is same as the subset sum equals k problem. For time and space complexity analysis, refer
        # to that problem.
        sigma = sum(arr)
        if (sigma + diff) % 2 != 0:
            return 0

        target = (sigma + diff) // 2
        return get_count_with_subset_sum(arr, target)

    print(
        get_partitions_with_diff(
            [5, 2, 5, 1],
            3
        )
    )

    print(
        get_partitions_with_diff(
            [5, 2, 6, 4],
            3
        )
    )

    print(
        get_partitions_with_diff(
            [1, 1, 1, 1],
            0
        )
    )

    print(
        get_partitions_with_diff(
            [4, 6, 3],
            1
        )
    )

    print(
        get_partitions_with_diff(
            [3, 1, 1, 2, 1],
            0
        )
    )

    print(
        get_partitions_with_diff(
            [3, 2, 2, 5, 1],
            1
        )
    )


def space_optimized():
    def get_count_with_subset_sum(arr, target):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1 if arr[0] == target else 0

        prev = {tgt: 0 for tgt in range(target + 1)}
        prev[0] = 1
        prev[arr[0]] = 1

        for index in range(1, len(arr)):
            curr = {tgt: 0 for tgt in range(target + 1)}
            curr[0] = 1

            for tgt in range(target + 1):
                left, right = 0, 0

                if tgt - arr[index] in prev:
                    left = prev[tgt - arr[index]]
                if tgt in prev:
                    right = prev[tgt]

                curr[tgt] = left + right

            prev = curr

        return prev[target]

    def get_partitions_with_diff(arr, diff):
        # Given that s1 - s2 = diff >= 0 and s1 + s2 = sigma, we can say that we have to find
        # those subsets from the array where s1 = (sigma + diff)/2. Also, sigma + diff needs to be
        # divisible by 2 so that we can find such a subset. Apart from this, the whole problem
        # is same as the subset sum equals k problem. For time and space complexity analysis, refer
        # to that problem.
        sigma = sum(arr)
        if (sigma + diff) % 2 != 0:
            return 0

        target = (sigma + diff) // 2
        return get_count_with_subset_sum(arr, target)

    print(
        get_partitions_with_diff(
            [5, 2, 5, 1],
            3
        )
    )

    print(
        get_partitions_with_diff(
            [5, 2, 6, 4],
            3
        )
    )

    print(
        get_partitions_with_diff(
            [1, 1, 1, 1],
            0
        )
    )

    print(
        get_partitions_with_diff(
            [4, 6, 3],
            1
        )
    )

    print(
        get_partitions_with_diff(
            [3, 1, 1, 2, 1],
            0
        )
    )

    print(
        get_partitions_with_diff(
            [3, 2, 2, 5, 1],
            1
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