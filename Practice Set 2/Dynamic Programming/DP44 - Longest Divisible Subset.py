def get_at(arr, index):
    if index >= len(arr):
        return 1
    if index < 0:
        return 1
    return arr[index]


def mutual_divisibility(arr, index, prev_index):
    return get_at(arr, prev_index) % get_at(arr, index) == 0 or get_at(arr, index) % get_at(arr, prev_index) == 0


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, index, prev_index):
        if index == 0:
            return 1 if mutual_divisibility(arr, 0, prev_index) else 0
        left = 0
        if mutual_divisibility(arr, index, prev_index):
            left = 1 + solve(arr, index - 1, index)
        right = solve(arr, index - 1, prev_index)
        return max(left, right)

    def lds(arr):
        n = len(arr)
        return solve(arr, n - 1, n)

    print(lds([1, 16, 7, 8, 4]))
    print(lds([1, 2, 5]))
    print(lds([3, 3, 3]))
    print(lds([1, 2, 4, 8]))
    print(lds([1, 2, 3]))
    print(lds([2, 4, 3, 8]))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n^2 + n).
    """
    def solve(arr, index, prev_index, dp):
        if index == 0:
            return 1 if mutual_divisibility(arr, 0, prev_index) else 0
        if dp[index][prev_index] is not None:
            return dp[index][prev_index]
        left = 0
        if mutual_divisibility(arr, index, prev_index):
            left = 1 + solve(arr, index - 1, index, dp)
        right = solve(arr, index - 1, prev_index, dp)
        dp[index][prev_index] = max(left, right)
        return dp[index][prev_index]

    def lds(arr):
        n = len(arr)
        dp = {i: {j: None for j in range(1, n + 1)} for i in range(n)}
        return solve(arr, n - 1, n, dp)

    print(lds([1, 16, 7, 8, 4]))
    print(lds([1, 2, 5]))
    print(lds([3, 3, 3]))
    print(lds([1, 2, 4, 8]))
    print(lds([1, 2, 3]))
    print(lds([2, 4, 3, 8]))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n^2).
    """
    def lds(arr):
        n = len(arr)
        dp = {i: {j: 0 for j in range(1, n + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = 1 if mutual_divisibility(arr, 0, j) else 0
        for index in range(1, n):
            for prev_index in range(index + 1, n + 1):
                left = 0
                if mutual_divisibility(arr, index, prev_index):
                    left = 1 + dp[index - 1][index]
                right = dp[index - 1][prev_index]
                dp[index][prev_index] = max(left, right)
        return dp[n - 1][n]

    print(lds([1, 16, 7, 8, 4]))
    print(lds([1, 2, 5]))
    print(lds([3, 3, 3]))
    print(lds([1, 2, 4, 8]))
    print(lds([1, 2, 3]))
    print(lds([2, 4, 3, 8]))


def space_optimized():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """
    def lds(arr):
        n = len(arr)
        prev = {j: 0 for j in range(1, n + 1)}
        for j in prev:
            prev[j] = 1 if mutual_divisibility(arr, 0, j) else 0
        for index in range(1, n):
            curr = {j: 0 for j in range(1, n + 1)}
            for prev_index in range(index + 1, n + 1):
                left = 0
                if mutual_divisibility(arr, index, prev_index):
                    left = 1 + prev[index]
                right = prev[prev_index]
                curr[prev_index] = max(left, right)
            prev = curr
        return prev[n]

    print(lds([1, 16, 7, 8, 4]))
    print(lds([1, 2, 5]))
    print(lds([3, 3, 3]))
    print(lds([1, 2, 4, 8]))
    print(lds([1, 2, 3]))
    print(lds([2, 4, 3, 8]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
