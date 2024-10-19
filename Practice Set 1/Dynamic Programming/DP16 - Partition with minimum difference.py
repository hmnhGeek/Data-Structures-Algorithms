# Problem link - https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494
# Solution - https://www.youtube.com/watch?v=GS_OqZb2CWc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=17

def recursive():
    def solve(arr, index, target):
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target

        left = False
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index])
        right = solve(arr, index - 1, target)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)


def memoized():
    def solve(arr, index, target, dp):
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target

        if dp[index][target] is not None:
            return dp[index][target]

        left = False
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index], dp)
        right = solve(arr, index - 1, target, dp)
        dp[index][target] = left or right
        return dp[index][target]

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([1, 6, 11, 5], 15))


def tabulation():
    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: False for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = True
        dp[0][arr[0]] = True

        for index in range(1, n):
            for tgt in range(target + 1):
                left = False
                if arr[index] <= tgt:
                    left = dp[index - 1][tgt - arr[index]]
                right = dp[index - 1][tgt]
                dp[index][tgt] = left or right
        return dp[n - 1][target]

    print(subset_sum([1, 6, 11, 5], 12))


def subset_sum(arr, target):
    """
        Time complexity is O(n*target) and space complexity is O(target).
    """
    n = len(arr)
    prev = {j: False for j in range(target + 1)}
    prev[0] = True
    prev[arr[0]] = True

    for index in range(1, n):
        curr = {j: False for j in range(target + 1)}
        curr[0] = True
        for tgt in range(target + 1):
            left = False
            if arr[index] <= tgt:
                left = prev[tgt - arr[index]]
            right = prev[tgt]
            curr[tgt] = left or right
        prev = curr
    return prev[target]


def min_partition(arr):
    sigma = sum(arr)
    for target in range(sigma//2, sigma):
        if subset_sum(arr, target):
            break
    return abs(2*target - sigma)


print(min_partition([1, 2, 3, 4]))
print(min_partition([8, 6, 5]))
print(min_partition([1, 6, 11, 5]))
print(min_partition([1, 5, 11, 5]))
print(min_partition([3, 1, 5, 2, 8]))