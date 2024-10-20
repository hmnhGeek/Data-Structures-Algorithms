# Problem link - https://www.geeksforgeeks.org/count-of-subsets-with-given-difference/
# Solution - https://www.youtube.com/watch?v=zoilQD1kYSg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=19


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

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))


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
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))


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

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))


def subset_sum(arr, target):
    n = len(arr)
    prev = {j: 0 for j in range(target + 1)}
    prev[0] = 1
    prev[arr[0]] = 1
    for index in range(1, n):
        curr = {j: 0 for j in range(target + 1)}
        curr[0] = 1
        for tgt in range(target + 1):
            left = 0
            if arr[index] <= tgt:
                left = prev[tgt - arr[index]]
            right = prev[tgt]
            curr[tgt] = left + right
        prev = curr
    return prev[target]


def count_partitions(arr, diff):
    s = sum(arr)
    count = 0
    for target in range(s // 2, s + 1):
        s1 = target
        if 2 * s1 - s == diff:
            count_subsets = subset_sum(arr, s1)
            count += count_subsets
    return count


print(count_partitions([5, 2, 6, 4], 3))
print(count_partitions([5, 2, 5, 1], 3))
print(count_partitions([1, 1, 1, 1], 0))
print(count_partitions([4, 6, 3], 1))
print(count_partitions([3, 1, 1, 2, 1], 4))
print(count_partitions([3, 2, 2, 5, 1], 1))
print(count_partitions([1, 2, 3, 1, 2], 1))
