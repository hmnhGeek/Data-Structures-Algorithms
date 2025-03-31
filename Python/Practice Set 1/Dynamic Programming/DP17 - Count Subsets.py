# Problem link - https://www.naukri.com/code360/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=ZHyb-A2Mte4&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=18

def recursive():
    """
        T: 2^{n*target} and S: O(target)
    """

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

    def count_subsets(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(count_subsets([1, 2, 2, 3], 3))
    print(count_subsets([1, 1, 4, 5], 5))
    print(count_subsets([2, 34, 5], 40))


def memoized():
    """
        T: O(n*target) and S: O(target*n + target)
    """

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
        return left + right

    def count_subsets(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(count_subsets([1, 2, 2, 3], 3))
    print(count_subsets([1, 1, 4, 5], 5))
    print(count_subsets([2, 34, 5], 40))


def tabulation():
    """
            T: O(n*target) and S: O(target*n)
    """

    def count_subsets(arr, target):
        n = len(arr)
        dp = {i: {j: 0 for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 1
        dp[0][arr[0]] = 1

        for index in range(1, n):
            for tgt in range(target + 1):
                left = 0
                if arr[index] <= tgt:
                    left = dp[index - 1][tgt - arr[index]]
                right = dp[index - 1][tgt]
                dp[index][tgt] = left + right

        return dp[n - 1][target]

    print(count_subsets([1, 2, 2, 3], 3))
    print(count_subsets([1, 1, 4, 5], 5))
    print(count_subsets([2, 34, 5], 40))


def space_optimized():
    """
            T: O(n*target) and S: O(target)
    """

    def count_subsets(arr, target):
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

    print(count_subsets([1, 2, 2, 3], 3))
    print(count_subsets([1, 1, 4, 5], 5))
    print(count_subsets([2, 34, 5], 40))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()