# Problem link - https://www.naukri.com/code360/problems/partition-equal-subset-sum_892980?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
# Solution - https://www.youtube.com/watch?v=7win3dcgo3k&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=16

# This problem is exactly same as subset_sum_equals_k.py in this folder. Please refer to it for comments.
# The only catch here is that since we want to know if a partition is possible or not such that the sum
# of both subsets is same, we can compute the sum of complete array and divide the sum by 2; this would
# be the target sum which we can feed to the code in subset_sum_equals_k.py. If the sum of the array is
# odd, then partition is not possible because the whole array is made of integers and no partition could
# form an integral sum//2 if sum is odd. Please watch the soltion for more clarity.

def recursive():
    def f(arr, index, target):
        if index < 0:
            return False
        if target < 0:
            return False
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target

        return f(arr, index - 1, target - arr[index]) or f(arr, index - 1, target)

    def is_subset_sum_possible(arr, required_target):
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == required_target

        return f(arr, len(arr) - 1, required_target)

    def is_partition_possible(arr):
        s = sum(arr)
        if s % 2 == 1:
            return False

        required_target = s // 2
        return is_subset_sum_possible(arr, required_target)

    print(
        is_partition_possible(
            [2, 3, 3, 3, 4, 5]
        )
    )

    print(
        is_partition_possible(
            [3, 1, 1, 2, 2, 1]
        )
    )

    print(
        is_partition_possible(
            [5, 6, 5, 11, 6]
        )
    )

    print(
        is_partition_possible(
            [2, 2, 1, 1, 1, 1, 1, 3, 3]
        )
    )

    print(
        is_partition_possible(
            [8, 7, 6, 12, 4, 5]
        )
    )


def memoized():
    def f(arr, index, target, dp):
        if index < 0:
            return False
        if target < 0:
            return False
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target

        if target in dp[index] and dp[index][target] is not None:
            return dp[index][target]

        dp[index][target] = f(arr, index - 1, target - arr[index], dp) or f(arr, index - 1, target, dp)
        return dp[index][target]

    def is_subset_sum_possible(arr, required_target):
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == required_target

        dp = {i: {tgt: None for tgt in range(required_target - max(arr), required_target + 1)} for i in range(len(arr))}
        return f(arr, len(arr) - 1, required_target, dp)

    def is_partition_possible(arr):
        s = sum(arr)
        if s % 2 == 1:
            return False

        required_target = s // 2
        return is_subset_sum_possible(arr, required_target)

    print(
        is_partition_possible(
            [2, 3, 3, 3, 4, 5]
        )
    )

    print(
        is_partition_possible(
            [3, 1, 1, 2, 2, 1]
        )
    )

    print(
        is_partition_possible(
            [5, 6, 5, 11, 6]
        )
    )

    print(
        is_partition_possible(
            [2, 2, 1, 1, 1, 1, 1, 3, 3]
        )
    )

    print(
        is_partition_possible(
            [8, 7, 6, 12, 4, 5]
        )
    )


def tabulation():
    def is_subset_sum_possible(arr, required_target):
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == required_target

        dp = {i: {tgt: False for tgt in range(required_target - max(arr), required_target + 1)} for i in range(len(arr))}
        for index in dp:
            dp[index][0] = True

        dp[0][arr[0]] = True

        for index in range(1, len(arr)):
            for tgt in range(1, required_target + 1):
                left, right = False, False

                if tgt - arr[index] in dp[index - 1]:
                    left = dp[index - 1][tgt - arr[index]]
                if tgt in dp[index - 1]:
                    right = dp[index - 1][tgt]

                dp[index][tgt] = left or right

        return dp[len(arr) - 1][required_target]

    def is_partition_possible(arr):
        s = sum(arr)
        if s % 2 == 1:
            return False

        required_target = s // 2
        return is_subset_sum_possible(arr, required_target)

    print(
        is_partition_possible(
            [2, 3, 3, 3, 4, 5]
        )
    )

    print(
        is_partition_possible(
            [3, 1, 1, 2, 2, 1]
        )
    )

    print(
        is_partition_possible(
            [5, 6, 5, 11, 6]
        )
    )

    print(
        is_partition_possible(
            [2, 2, 1, 1, 1, 1, 1, 3, 3]
        )
    )

    print(
        is_partition_possible(
            [8, 7, 6, 12, 4, 5]
        )
    )


def space_optimized():
    def is_subset_sum_possible(arr, required_target):
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == required_target

        prev = {tgt: False for tgt in range(required_target - max(arr), required_target + 1)}
        prev[0] = True
        prev[arr[0]] = True

        for index in range(1, len(arr)):
            curr = {tgt: False for tgt in range(required_target - max(arr), required_target + 1)}
            curr[0] = True

            for tgt in range(1, required_target + 1):
                left, right = False, False

                if tgt - arr[index] in prev:
                    left = prev[tgt - arr[index]]
                if tgt in prev:
                    right = prev[tgt]

                curr[tgt] = left or right
            prev = curr

        return prev[required_target]

    def is_partition_possible(arr):
        s = sum(arr)
        if s % 2 == 1:
            return False

        required_target = s // 2
        return is_subset_sum_possible(arr, required_target)

    print(
        is_partition_possible(
            [2, 3, 3, 3, 4, 5]
        )
    )

    print(
        is_partition_possible(
            [3, 1, 1, 2, 2, 1]
        )
    )

    print(
        is_partition_possible(
            [5, 6, 5, 11, 6]
        )
    )

    print(
        is_partition_possible(
            [2, 2, 1, 1, 1, 1, 1, 3, 3]
        )
    )

    print(
        is_partition_possible(
            [8, 7, 6, 12, 4, 5]
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