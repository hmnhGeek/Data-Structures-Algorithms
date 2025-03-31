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
    """
        Let us assume that there are two subsets with sums s1 and s2. Let the sum of whole array
        be s. We have these two equations now:

        s1 + s2 = s
        |s1 - s2| = d

        We have to minimize the value of `d`. Let's assume that s1 > s2. In that case, the 2nd equation
        becomes s1 - s2 = d.

        Using both the equations, we have d = 2*s1 - s.
        For s1 > s2, our search space will be [s//2, s). Even if you want to take the search space as
        (0, s//2], then s2 > s1. But that doesn't matter because both the search spaces will yield the same
        result.

        Now assuming the search space to be [s//2, s), the first target that is found in this space will give
        us the answer. Why first such target? Because as you move to the right in the search space, s1 starts
        to increase, but at the same time, s2 starts to decrease. Therefore, `d` or the gap between s1 and s2
        starts to increase. We don't want this to happen. The best result would come when s1 and s2 are near
        to s//2.

        Similarly, if your search space had been (0, s//2], then the loop should start in reverse so that you
        can detect the nearest target to s//2.

        Once we get the desired target, d_min = |2*s1 - s|.
        Return this d_min value.
    """

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