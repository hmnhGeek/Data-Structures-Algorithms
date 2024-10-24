# Problem link - https://www.naukri.com/code360/problems/target-sum_4127362?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=b3GD8263-PQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=22


def recursive():
    def solve(arr, index, target):
        if target == 0:
            return 1

        if index == 0:
            return 1 if arr[0] == target else 0

        left = 0
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index])
        right = solve(arr, index - 1, target)
        return left + right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(subset_sum([2, 1, 3, 1], 5))
    print(subset_sum([1, 2, 3, 3], 6))
    print(subset_sum([1, 1, 1, 1], 1))


def memoized():
    def solve(arr, index, target, dp):
        if target == 0:
            return 1

        if index == 0:
            return 1 if arr[0] == target else 0

        if dp[index][target] is not None:
            return dp[index][target]

        left = 0
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index], dp)
        right = solve(arr, index - 1, target, dp)
        dp[index][target] = left + right
        return dp[index][target]

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([2, 1, 3, 1], 5))
    print(subset_sum([1, 2, 3, 3], 6))
    print(subset_sum([1, 1, 1, 1], 1))


def tabulation():
    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: 0 for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 1
        for j in dp[0]:
            if j == arr[0]:
                dp[0][j] = 1

        for index in range(1, n):
            for tgt in range(1, target + 1):
                left = 0
                if arr[index] <= tgt:
                    left = dp[index - 1][tgt - arr[index]]
                right = dp[index - 1][tgt]
                dp[index][tgt] = left + right
        return dp[n - 1][target]

    print(subset_sum([2, 1, 3, 1], 5))
    print(subset_sum([1, 2, 3, 3], 6))
    print(subset_sum([1, 1, 1, 1], 1))


def subset_sum(arr, target):
    """
        Time complexity is O(n*target) and space complexity is O(target).
    """
    n = len(arr)
    prev = {j: 0 for j in range(target + 1)}
    prev[0] = 1
    for j in prev:
        if j == arr[0]:
            prev[j] = 1

    for index in range(1, n):
        curr = {j: 0 for j in range(target + 1)}
        curr[0] = 1
        for tgt in range(1, target + 1):
            left = 0
            if arr[index] <= tgt:
                left = prev[tgt - arr[index]]
            right = prev[tgt]
            curr[tgt] = left + right
        prev = curr
    return prev[target]


def target_sum(arr, k):
    s = sum(arr)
    s1 = (s + k)//2
    return subset_sum(arr, s1)


print(target_sum([1, 1, 1, 1, 1], 3))
print(target_sum([1, 2, 3, 1], 3))
print(target_sum([1, 2, 3], 2))
print(target_sum([1, 1], 0))