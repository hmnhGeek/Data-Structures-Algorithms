# Problem link - https://www.naukri.com/code360/problems/longest-increasing-subsequence_630459?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=ekcwMsSIzVc


def recursive():
    def solve(arr, index, prev):
        if index < 0:
            return 0

        left = 0
        if arr[index] < prev:
            left = 1 + solve(arr, index - 1, arr[index])
        right = solve(arr, index - 1, prev)
        return max(left, right)

    def longest_increasing_subsequence(arr):
        n = len(arr)
        return solve(arr, n - 1, 1e6)

    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(longest_increasing_subsequence([1, 2, 2]))


def memoized():
    def solve(arr, index, prev, dp):
        if index == 0:
            return 0

        if dp[index][prev] is not None:
            return dp[index][prev]

        left = 0
        if arr[index - 1] < prev:
            left = 1 + solve(arr, index - 1, arr[index - 1], dp)
        right = solve(arr, index - 1, prev, dp)
        dp[index][prev] = max(left, right)
        return dp[index][prev]

    def longest_increasing_subsequence(arr):
        n = len(arr)
        maxval = max(arr)
        dp = {i: {j: None for j in arr} for i in range(n + 1)}
        for i in dp:
            dp[i][maxval + 1] = None

        return solve(arr, n, maxval + 1, dp)

    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(longest_increasing_subsequence([1, 2, 2]))


def tabulation():
    def longest_increasing_subsequence(arr):
        n = len(arr)
        maxval = max(arr)
        dp = {i: {j: 0 for j in arr} for i in range(n + 1)}
        for i in dp:
            dp[i][maxval + 1] = 0

        for index in range(1, n + 1):
            for prev in dp[index]:
                left = 0
                if arr[index - 1] < prev:
                    left = 1 + dp[index - 1][arr[index - 1]]
                right = dp[index - 1][prev]
                dp[index][prev] = max(left, right)

        return dp[n][maxval + 1]

    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(longest_increasing_subsequence([1, 2, 2]))


def space_optimized():
    """
        Time complexity: O(n^2)
        Space complexity is O(n)
    """
    def longest_increasing_subsequence(arr):
        n = len(arr)
        maxval = max(arr)
        prev1 = {j: 0 for j in arr}
        prev1[maxval + 1] = 0

        for index in range(1, n + 1):
            curr = {j: 0 for j in arr}
            curr[maxval + 1] = 0
            for prev in curr:
                left = 0
                if arr[index - 1] < prev:
                    left = 1 + prev1[arr[index - 1]]
                right = prev1[prev]
                curr[prev] = max(left, right)
            prev1 = curr

        return prev1[maxval + 1]

    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(longest_increasing_subsequence([1, 2, 2]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()