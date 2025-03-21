def is_divisible(arr, index1, index2):
    if index2 >= len(arr) or index1 >= len(arr):
        return True
    return arr[index1] % arr[index2] == 0 or arr[index2] % arr[index1] == 0


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, i, j):
        if i == 0:
            return is_divisible(arr, 0, j)
        left = -1e6
        if is_divisible(arr, i, j):
            left = 1 + solve(arr, i - 1, i)
        right = solve(arr, i - 1, j)
        return max(left, right)
    
    def largest_divisible_subset(arr):
        n = len(arr)
        return solve(arr, n - 1, n)

    print(largest_divisible_subset([1, 16, 7, 8, 4]))
    print(largest_divisible_subset([1, 2, 5]))
    print(largest_divisible_subset([3, 3, 3]))
    print(largest_divisible_subset([1, 2, 4, 8]))
    print(largest_divisible_subset([1, 2, 3]))
    print(largest_divisible_subset([2, 4, 3, 8]))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n + n^2).
    """
    def solve(arr, i, j, dp):
        if i == 0:
            return is_divisible(arr, 0, j)
        if dp[i][j] is not None:
            return dp[i][j]
        left = -1e6
        if is_divisible(arr, i, j):
            left = 1 + solve(arr, i - 1, i, dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = max(left, right)
        return dp[i][j]

    def largest_divisible_subset(arr):
        n = len(arr)
        dp = {i: {j: None for j in range(1, n + 1)} for i in range(n)}
        return solve(arr, n - 1, n, dp)

    print(largest_divisible_subset([1, 16, 7, 8, 4]))
    print(largest_divisible_subset([1, 2, 5]))
    print(largest_divisible_subset([3, 3, 3]))
    print(largest_divisible_subset([1, 2, 4, 8]))
    print(largest_divisible_subset([1, 2, 3]))
    print(largest_divisible_subset([2, 4, 3, 8]))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n^2).
    """
    def largest_divisible_subset(arr):
        n = len(arr)
        dp = {i: {j: -1e6 for j in range(1, n + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = is_divisible(arr, 0, j)
        for i in range(1, n):
            for j in range(1, n + 1):
                left = -1e6
                if is_divisible(arr, i, j):
                    left = 1 + dp[i - 1][i]
                right = dp[i - 1][j]
                dp[i][j] = max(left, right)
        return dp[n - 1][n]

    print(largest_divisible_subset([1, 16, 7, 8, 4]))
    print(largest_divisible_subset([1, 2, 5]))
    print(largest_divisible_subset([3, 3, 3]))
    print(largest_divisible_subset([1, 2, 4, 8]))
    print(largest_divisible_subset([1, 2, 3]))
    print(largest_divisible_subset([2, 4, 3, 8]))


def space_optimized():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """
    def largest_divisible_subset(arr):
        n = len(arr)
        prev = {j: -1e6 for j in range(1, n + 1)}
        for j in prev:
            prev[j] = is_divisible(arr, 0, j)
        for i in range(1, n):
            curr = {j: -1e6 for j in range(1, n + 1)}
            for j in range(1, n + 1):
                left = -1e6
                if is_divisible(arr, i, j):
                    left = 1 + prev[i]
                right = prev[j]
                curr[j] = max(left, right)
            prev = curr
        return prev[n]

    print(largest_divisible_subset([1, 16, 7, 8, 4]))
    print(largest_divisible_subset([1, 2, 5]))
    print(largest_divisible_subset([3, 3, 3]))
    print(largest_divisible_subset([1, 2, 4, 8]))
    print(largest_divisible_subset([1, 2, 3]))
    print(largest_divisible_subset([2, 4, 3, 8]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
