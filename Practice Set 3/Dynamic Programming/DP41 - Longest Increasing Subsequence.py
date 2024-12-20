# Problem link - https://www.naukri.com/code360/problems/longest-increasing-subsequence_630459?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=ekcwMsSIzVc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=43&t=1270s


def get_val_at(arr, index):
    if index >= len(arr):
        return 1e6
    if index < 0:
        return -1e6
    return arr[index]


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, index, prev):
        if index == 0:
            if get_val_at(arr, 0) < get_val_at(arr, prev):
                return 1
            else:
                return 0
        left = 0
        if get_val_at(arr, index) < get_val_at(arr, prev):
            left = 1 + solve(arr, index - 1, index)
        right = solve(arr, index - 1, prev)
        return max(left, right)

    def get_lis_length(arr):
        n = len(arr)
        return solve(arr, n - 1, n)

    print(get_lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_lis_length([5, 4, 11, 1, 16, 8]))
    print(get_lis_length([1, 2, 2]))
    print(get_lis_length([0, 1, 0, 3, 2, 3]))
    print(get_lis_length([7, 7, 7, 7, 7, 7, 7]))
    print(get_lis_length([3, 10, 2, 1, 20]))
    print(get_lis_length([30, 20, 10]))
    print(get_lis_length([10, 20, 35, 80]))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n + 2n).
    """

    def solve(arr, index, prev, dp):
        if index == 0:
            if get_val_at(arr, 0) < get_val_at(arr, prev):
                return 1
            else:
                return 0
        if dp[index][prev] is not None:
            return dp[index][prev]
        left = 0
        if get_val_at(arr, index) < get_val_at(arr, prev):
            left = 1 + solve(arr, index - 1, index, dp)
        right = solve(arr, index - 1, prev, dp)
        dp[index][prev] = max(left, right)
        return dp[index][prev]

    def get_lis_length(arr):
        n = len(arr)
        dp = {i: {j: None for j in range(n + 1)} for i in range(n)}
        return solve(arr, n - 1, n, dp)

    print(get_lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_lis_length([5, 4, 11, 1, 16, 8]))
    print(get_lis_length([1, 2, 2]))
    print(get_lis_length([0, 1, 0, 3, 2, 3]))
    print(get_lis_length([7, 7, 7, 7, 7, 7, 7]))
    print(get_lis_length([3, 10, 2, 1, 20]))
    print(get_lis_length([30, 20, 10]))
    print(get_lis_length([10, 20, 35, 80]))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(2n).
    """

    def get_lis_length(arr):
        n = len(arr)
        dp = {i: {j: 0 for j in range(n + 1)} for i in range(n)}
        for j in dp[0]:
            if get_val_at(arr, 0) < get_val_at(arr, j):
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        for index in range(1, n):
            for prev in range(index + 1, n + 1):
                left = 0
                if get_val_at(arr, index) < get_val_at(arr, prev):
                    left = 1 + dp[index - 1][index]
                right = dp[index - 1][prev]
                dp[index][prev] = max(left, right)
        return dp[n - 1][n]

    print(get_lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_lis_length([5, 4, 11, 1, 16, 8]))
    print(get_lis_length([1, 2, 2]))
    print(get_lis_length([0, 1, 0, 3, 2, 3]))
    print(get_lis_length([7, 7, 7, 7, 7, 7, 7]))
    print(get_lis_length([3, 10, 2, 1, 20]))
    print(get_lis_length([30, 20, 10]))
    print(get_lis_length([10, 20, 35, 80]))


def space_optimized():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """

    def get_lis_length(arr):
        n = len(arr)
        prev = {j: 0 for j in range(n + 1)}
        for j in prev:
            if get_val_at(arr, 0) < get_val_at(arr, j):
                prev[j] = 1
            else:
                prev[j] = 0
        for index in range(1, n):
            curr = {j: 0 for j in range(n + 1)}
            for j in range(index + 1, n + 1):
                left = 0
                if get_val_at(arr, index) < get_val_at(arr, j):
                    left = 1 + prev[index]
                right = prev[j]
                curr[j] = max(left, right)
            prev = curr
        return prev[n]

    print(get_lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_lis_length([5, 4, 11, 1, 16, 8]))
    print(get_lis_length([1, 2, 2]))
    print(get_lis_length([0, 1, 0, 3, 2, 3]))
    print(get_lis_length([7, 7, 7, 7, 7, 7, 7]))
    print(get_lis_length([3, 10, 2, 1, 20]))
    print(get_lis_length([30, 20, 10]))
    print(get_lis_length([10, 20, 35, 80]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
