# Problem - https://www.naukri.com/code360/problems/target-sum_4127362?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=b3GD8263-PQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=22

# The approach used here is different. However, we can use subset sum also to calculate the answer.
# We want to assign signs in such a way that s1 - s2 = D. We also know that s1 + s2 = sum. Hence,
# s1 = (D + sum)/2. This will be the target for the subset sum problem, and we will be able to find
# the count of such subsets, which will match with the results here.

def recursive():
    def solve(arr, target, index, value):
        # Time complexity is O(2^n) and space is O(n)

        # if you are at index = 0, that means you must've a value in which you
        # have summed up all the elements. Check if this value is equal to target
        # or not. If it is, return 1 else return 0.
        if index == 0:
            return 1 if value == target else 0

        # solve the left recursion by moving to a lower index and consider the value at
        # that lower index to be positive.
        left = solve(arr, target, index - 1, value + arr[index - 1])

        # solve the right recursion by moving to a lower index and consider the value at
        # that lower index to be negative.
        right = solve(arr, target, index - 1, value - arr[index - 1])

        # return the count obtained by summing both up.
        return left + right

    def target_sum_with_signs(arr, target):
        # store the length of the array to be used for indexing later.
        n = len(arr)

        # start from last index and the counts obtained in these two cases
        # Case 1: When the value at last index is considered as positive.
        # Case 2: When the value at last index is considered as negative.
        return solve(arr, target, n - 1, arr[n - 1]) + solve(arr, target, n - 1, -arr[n - 1])

    print(target_sum_with_signs([1, 2, 3, 1], 3))
    print(target_sum_with_signs([1, 1, 1, 1, 1], 3))
    print(target_sum_with_signs([1, 2, 3], 2))
    print(target_sum_with_signs([1, 1], 0))
    print(target_sum_with_signs([1], 1))


def memoized():
    def solve(arr, target, index, value, dp):
        # Time complexity is O(n * value * 2) and space is O(n + {n * value * 2})

        # if you are at index = 0, that means you must've a value in which you
        # have summed up all the elements. Check if this value is equal to target
        # or not. If it is, return 1 else return 0.
        if index == 0:
            return 1 if value == target else 0

        if dp[index][value] is not None:
            return dp[index][value]

        # solve the left recursion by moving to a lower index and consider the value at
        # that lower index to be positive.
        left = solve(arr, target, index - 1, value + arr[index - 1], dp)

        # solve the right recursion by moving to a lower index and consider the value at
        # that lower index to be negative.
        right = solve(arr, target, index - 1, value - arr[index - 1], dp)

        # return the count obtained by summing both up.
        dp[index][value] = left + right
        return dp[index][value]

    def target_sum_with_signs(arr, target):
        # store the length of the array to be used for indexing later.
        n = len(arr)

        dp = {i: {j: None for j in range(-sum(arr), sum(arr) + 1)} for i in range(n)}

        # start from last index and the counts obtained in these two cases
        # Case 1: When the value at last index is considered as positive.
        # Case 2: When the value at last index is considered as negative.
        return solve(arr, target, n - 1, arr[n - 1], dp) + solve(arr, target, n - 1, -arr[n - 1], dp)

    print(target_sum_with_signs([1, 2, 3, 1], 3))
    print(target_sum_with_signs([1, 1, 1, 1, 1], 3))
    print(target_sum_with_signs([1, 2, 3], 2))
    print(target_sum_with_signs([1, 1], 0))
    print(target_sum_with_signs([1], 1))


def tabulation():
    def target_sum_with_signs(arr, target):
        # Time complexity is O(n * target) and space is O(n * target)

        # store the length of the array to be used for indexing later.
        n = len(arr)

        # initialize a 2D DP array with all the counts as 0. The range for values can be from -sum(arr) to
        # sum(arr) (inclusive) do a dry run and observe the maximum values the recursion can reach on both
        # ends, and you will find this range only.
        dp = {i: {j: 0 for j in range(-sum(arr), sum(arr) + 1)} for i in range(n)}

        for index in range(n):
            for value in range(-sum(arr), sum(arr) + 1):
                # if index is 0 and the value is equal to target, then we must increase the count to 1.
                if index == 0:
                    dp[0][value] = 1 if value == target else 0
                else:
                    left, right = 0, 0
                    # solve the left recursion by moving to a lower index and consider the value at
                    # that lower index to be positive.
                    if value + arr[index - 1] in dp[index - 1]:
                        left = dp[index - 1][value + arr[index - 1]]

                    # solve the right recursion by moving to a lower index and consider the value at
                    # that lower index to be negative.
                    if value - arr[index - 1] in dp[index - 1]:
                        right = dp[index - 1][value - arr[index - 1]]

                    # return the count obtained by summing both up.
                    dp[index][value] = left + right

        # start from last index and the counts obtained in these two cases
        # Case 1: When the value at last index is considered as positive.
        # Case 2: When the value at last index is considered as negative.
        return dp[n - 1][arr[n - 1]] + dp[n - 1][-arr[n - 1]]

    print(target_sum_with_signs([1, 2, 3, 1], 3))
    print(target_sum_with_signs([1, 1, 1, 1, 1], 3))
    print(target_sum_with_signs([1, 2, 3], 2))
    print(target_sum_with_signs([1, 1], 0))
    print(target_sum_with_signs([1], 1))


def space_optimized():
    def target_sum_with_signs(arr, target):
        # Time complexity is O(n * target) and space is O(target)

        # store the length of the array to be used for indexing later.
        n = len(arr)

        # initialize a 2D DP array with all the counts as 0.
        prev = {j: 0 for j in range(-sum(arr), sum(arr) + 1)}
        prev[target] = 1

        for index in range(1, n):
            curr = {j: 0 for j in range(-sum(arr), sum(arr) + 1)}
            for value in range(-sum(arr), sum(arr) + 1):
                left, right = 0, 0
                # solve the left recursion by moving to a lower index and consider the value at
                # that lower index to be positive.
                if value + arr[index - 1] in prev:
                    left = prev[value + arr[index - 1]]

                # solve the right recursion by moving to a lower index and consider the value at
                # that lower index to be negative.
                if value - arr[index - 1] in prev:
                    right = prev[value - arr[index - 1]]

                # return the count obtained by summing both up.
                curr[value] = left + right
            prev = curr

        # start from last index and the counts obtained in these two cases
        # Case 1: When the value at last index is considered as positive.
        # Case 2: When the value at last index is considered as negative.
        return prev[arr[n - 1]] + prev[-arr[n - 1]]

    print(target_sum_with_signs([1, 2, 3, 1], 3))
    print(target_sum_with_signs([1, 1, 1, 1, 1], 3))
    print(target_sum_with_signs([1, 2, 3], 2))
    print(target_sum_with_signs([1, 1], 0))
    print(target_sum_with_signs([1], 1))


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