def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, target):
        if target == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == target else 0

        left = 0
        if arr[i] <= target:
            left = solve(arr, i - 1, target - arr[i])
        right = solve(arr, i - 1, target)
        return left + right

    def count(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


def memoized():
    """
        Time complexity is O(nk) and space complexity is O(n + nk).
    """
    def solve(arr, i, target, dp):
        if target == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == target else 0

        if dp[i][target] is not None:
            return dp[i][target]

        left = 0
        if arr[i] <= target:
            left = solve(arr, i - 1, target - arr[i], dp)
        right = solve(arr, i - 1, target, dp)
        dp[i][target] = left + right
        return dp[i][target]

    def count(arr, k):
        n = len(arr)
        dp = {i: {j: None for j in range(k + 1)} for i in range(n)}
        return solve(arr, n - 1, k, dp)

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


def tabulation():
    """
        Time complexity is O(nk) and space complexity is O(nk).
    """
    def count(arr, k):
        n = len(arr)
        dp = {i: {j: 0 for j in range(k + 1)} for i in range(n)}

        for j in dp[0]:
            dp[0][j] = 1 if arr[0] == j else 0
        for i in dp:
            dp[i][0] = 1

        for i in range(1, n):
            for target in range(k + 1):
                left = 0
                if arr[i] <= target:
                    left = dp[i - 1][target - arr[i]]
                right = dp[i - 1][target]
                dp[i][target] = left + right
        return dp[n - 1][k]

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


def space_optimized():
    """
        Time complexity is O(nk) and space complexity is O(k).
    """
    def count(arr, k):
        n = len(arr)
        prev = {j: 0 for j in range(k + 1)}

        for j in prev:
            prev[j] = 1 if arr[0] == j else 0
        prev[0] = 1

        for i in range(1, n):
            curr = {j: 0 for j in range(k + 1)}
            curr[0] = 1
            for target in range(k + 1):
                left = 0
                if arr[i] <= target:
                    left = prev[target - arr[i]]
                right = prev[target]
                curr[target] = left + right
            prev = curr
        return prev[k]

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


class Solution:
    @staticmethod
    def _count_subsets(arr, k):
        n = len(arr)
        prev = {j: 0 for j in range(k + 1)}

        for j in prev:
            prev[j] = 1 if arr[0] == j else 0
        prev[0] = 1

        for i in range(1, n):
            curr = {j: 0 for j in range(k + 1)}
            curr[0] = 1
            for target in range(k + 1):
                left = 0
                if arr[i] <= target:
                    left = prev[target - arr[i]]
                right = prev[target]
                curr[target] = left + right
            prev = curr
        return prev[k]

    @staticmethod
    def count_subsets(arr, d):
        s = sum(arr)
        if (s + d) % 2 != 0:
            return 0
        s1 = (s + d)//2
        s2 = s1 - d
        count = 0
        if s1 >= s2:
            count = Solution._count_subsets(arr, s1)
        return count


print(Solution.count_subsets([5, 2, 6, 4], 3))
print(Solution.count_subsets([1, 1, 1, 1], 0))
print(Solution.count_subsets([4, 6, 3], 1))
print(Solution.count_subsets([3, 1, 1, 2, 1], 0))
print(Solution.count_subsets([3, 2, 2, 5, 1], 1))