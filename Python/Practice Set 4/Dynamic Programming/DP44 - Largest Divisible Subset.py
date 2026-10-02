# Problem link - https://www.naukri.com/code360/problems/divisible-set_3754960?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=gDuZwBW9VvM&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=45


def is_divisible(arr, i, j):
    if j == len(arr):
        return True
    return arr[i] % arr[j] == 0 or arr[j] % arr[i] == 0


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def get_lds_length(arr):
        n = len(arr)
        return solve(arr, n - 1, n)

    def solve(arr, i, j):
        if i == 0:
            return 1 if is_divisible(arr, i, j) else 0
        if is_divisible(arr, i, j):
            return max(1 + solve(arr, i - 1, i), solve(arr, i - 1, j))
        else:
            return solve(arr, i - 1, j)

    print(get_lds_length([1, 16, 7, 8, 4]))
    print(get_lds_length([1, 2, 5]))
    print(get_lds_length([3, 3, 3]))
    print(get_lds_length([1, 2, 4, 8]))
    print(get_lds_length([1, 2, 3]))
    print(get_lds_length([2, 4, 3, 8]))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n + n^2).
    """
    def get_lds_length(arr):
        n = len(arr)
        dp = {i: {j: None for j in range(1, n + 1)} for i in range(n)}
        return solve(arr, n - 1, n, dp)

    def solve(arr, i, j, dp):
        if i == 0:
            return 1 if is_divisible(arr, i, j) else 0
        if dp[i][j] is not None:
            return dp[i][j]
        if is_divisible(arr, i, j):
            dp[i][j] = max(1 + solve(arr, i - 1, i, dp), solve(arr, i - 1, j, dp))
        else:
            dp[i][j] = solve(arr, i - 1, j, dp)
        return dp[i][j]

    print(get_lds_length([1, 16, 7, 8, 4]))
    print(get_lds_length([1, 2, 5]))
    print(get_lds_length([3, 3, 3]))
    print(get_lds_length([1, 2, 4, 8]))
    print(get_lds_length([1, 2, 3]))
    print(get_lds_length([2, 4, 3, 8]))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n^2).
    """
    def get_lds_length(arr):
        n = len(arr)
        dp = {i: {j: 0 for j in range(1, n + 1)} for i in range(n)}
        for j in range(1, n + 1):
            if is_divisible(arr, 0, j):
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, n + 1):
                if is_divisible(arr, i, j):
                    dp[i][j] = max(1 + dp[i - 1][i], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][n]

    print(get_lds_length([1, 16, 7, 8, 4]))
    print(get_lds_length([1, 2, 5]))
    print(get_lds_length([3, 3, 3]))
    print(get_lds_length([1, 2, 4, 8]))
    print(get_lds_length([1, 2, 3]))
    print(get_lds_length([2, 4, 3, 8]))


def space_optimized():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """
    def get_lds_length(arr):
        n = len(arr)
        prev = {j: 0 for j in range(1, n + 1)}
        for j in range(1, n + 1):
            if is_divisible(arr, 0, j):
                prev[j] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(1, n + 1)}
            for j in range(1, n + 1):
                if is_divisible(arr, i, j):
                    curr[j] = max(1 + prev[i], prev[j])
                else:
                    curr[j] = prev[j]
            prev = curr
        return prev[n]

    print(get_lds_length([1, 16, 7, 8, 4]))
    print(get_lds_length([1, 2, 5]))
    print(get_lds_length([3, 3, 3]))
    print(get_lds_length([1, 2, 4, 8]))
    print(get_lds_length([1, 2, 3]))
    print(get_lds_length([2, 4, 3, 8]))


class Solution:
    @staticmethod
    def print_lds(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """
        n = len(arr)
        dp = {i: 1 for i in range(n)}
        parent = {i: i for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if is_divisible(arr, i, j) and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    parent[i] = j
        lds_length = max(dp, key=dp.get)
        lds = []
        start_index = lds_length
        while start_index != parent[start_index]:
            lds.append(arr[start_index])
            start_index = parent[start_index]
        lds.append(arr[start_index])
        return lds


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
print("Printing LDS")
print(Solution.print_lds([1, 16, 7, 8, 4]))
print(Solution.print_lds([1, 2, 5]))
print(Solution.print_lds([3, 3, 3]))
print(Solution.print_lds([1, 2, 4, 8]))
print(Solution.print_lds([1, 2, 3]))
print(Solution.print_lds([2, 4, 3, 8]))
