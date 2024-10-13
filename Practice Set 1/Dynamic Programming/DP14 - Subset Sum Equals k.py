def recursive():
    def solve(arr, i, target):
        # Time complexity is O(2^n) and space complexity is O(n)

        if target == 0:
            return True
        if i == 0:
            return arr[0] == target

        left = False
        if target >= arr[i]:
            left = solve(arr, i - 1, target - arr[i])
        right = solve(arr, i - 1, target)
        return left or right

    def subset_sum(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def memoized():
    def solve(arr, i, target, dp):
        # Time complexity is O(n*target) and space complexity is O(n + n*target)

        if target == 0:
            return True
        if i == 0:
            return arr[0] == target

        if dp[i][target] is not None:
            return dp[i][target]

        left = False
        if target >= arr[i]:
            left = solve(arr, i - 1, target - arr[i], dp)
        right = solve(arr, i - 1, target, dp)
        dp[i][target] = left or right
        return left or right

    def subset_sum(arr, k):
        n = len(arr)
        dp = {i: {j: None for j in range(k + 1)} for i in range(n)}
        return solve(arr, n - 1, k, dp)

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def tabulation():
    # T: O(n*target) and space: O(n*target)
    def subset_sum(arr, k):
        n = len(arr)
        dp = {i: {j: False for j in range(k + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = True
        dp[0][arr[0]] = True

        for i in range(1, n):
            for target in range(k + 1):
                left = False
                if target >= arr[i]:
                    left = dp[i - 1][target - arr[i]]
                right = dp[i - 1][target]
                dp[i][target] = left or right

        return dp[n - 1][k]

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def space_optimized():
    # T: O(n*target) and space: O(target)
    def subset_sum(arr, k):
        n = len(arr)
        prev = {j: False for j in range(k + 1)}
        prev[0] = True
        prev[arr[0]] = True

        for i in range(1, n):
            curr = {j: False for j in range(k + 1)}
            for target in range(k + 1):
                left = False
                if target >= arr[i]:
                    left = prev[target - arr[i]]
                right = prev[target]
                curr[target] = left or right
            prev = curr
        return prev[k]

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()