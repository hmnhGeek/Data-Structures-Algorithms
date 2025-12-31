def recursive():
    def target_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    def solve(arr, i, j):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        left = 0
        if j >= arr[i]:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left + right

    print(target_sum([1, 2, 3, 1], 3))


def memoized():
    def target_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    def solve(arr, i, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if j >= arr[i]:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left + right
        return dp[i][j]

    print(target_sum([1, 2, 3, 1], 3))


def tabulation():
    def target_sum(arr, target):
        n = len(arr)
        dp = {i: {j: 0 for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 1
        dp[0][arr[0]] = 1
        for i in range(1, n):
            for j in range(target + 1):
                left = 0
                if j >= arr[i]:
                    left = dp[i - 1][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left + right
        return dp[n - 1][target]

    print(target_sum([1, 2, 3, 1], 3))


def space_optimized():
    def target_sum(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        prev[arr[0]] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for j in range(target + 1):
                left = 0
                if j >= arr[i]:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    print(target_sum([1, 2, 3, 1], 3))


class Solution:
    @staticmethod
    def target_sum(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        prev[arr[0]] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for j in range(target + 1):
                left = 0
                if j >= arr[i]:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    @staticmethod
    def get_target_sum(arr, target):
        s = sum(arr)
        if (s + target) % 2 != 0:
            return
        actual_target = (s + target) // 2
        return Solution.target_sum(arr, actual_target)


print(Solution.get_target_sum([1, 1, 1, 1, 1], 3))
print(Solution.get_target_sum([1, 2, 3, 1], 3))
print(Solution.get_target_sum([1, 2, 3], 2))
print(Solution.get_target_sum([1, 1], 0))
print(Solution.get_target_sum([1], 1))