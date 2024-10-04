def recursive():
    def solve(arr, index, prev_index):
        if index == 0:
            return abs(arr[prev_index] - arr[0])

        right = float('inf')
        if index - 2 >= 0:
            right = solve(arr, index - 2, index)
        left = solve(arr, index - 1, index)
        return min(left, right) + abs(arr[prev_index] - arr[index])

    def frog_jump(arr):
        n = len(arr)
        if n == 2:
            return abs(arr[1] - arr[0])
        if n == 1:
            return 0

        return min(solve(arr, n - 3, n - 1), solve(arr, n - 2, n - 1))

    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))


def memoized():
    # T: O(n^2) and S: O(n + n^2)
    def solve(arr, index, prev_index, dp):
        if index == 0:
            return abs(arr[prev_index] - arr[0])

        if dp[index][prev_index] is not None:
            return dp[index][prev_index]

        right = float('inf')
        if index - 2 >= 0:
            right = solve(arr, index - 2, index, dp)
        left = solve(arr, index - 1, index, dp)
        dp[index][prev_index] = min(left, right) + abs(arr[prev_index] - arr[index])
        return dp[index][prev_index]

    def frog_jump(arr):
        n = len(arr)
        if n == 2:
            return abs(arr[1] - arr[0])
        if n == 1:
            return 0

        dp = {i: {j: None for j in range(n)} for i in range(n)}
        return min(solve(arr, n - 3, n - 1, dp), solve(arr, n - 2, n - 1, dp))

    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))


def tabulation():
    # T: O(n^2) and S: O(n^2)
    def frog_jump(arr):
        n = len(arr)
        if n == 2:
            return abs(arr[1] - arr[0])
        if n == 1:
            return 0

        dp = {i: {j: float('inf') for j in range(n)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = abs(arr[0] - arr[j])

        for index in range(1, n):
            for prev_index in range(n):
                right = float('inf')
                if index - 2 >= 0:
                    right = dp[index - 2][index]
                left = dp[index - 1][index]
                dp[index][prev_index] = min(left, right) + abs(arr[prev_index] - arr[index])

        return min(dp[n - 3][n - 1], dp[n - 2][n - 1])

    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))


def space_optimized():
    # T: O(n^2) and S: O(n)
    def frog_jump(arr):
        n = len(arr)
        if n == 2:
            return abs(arr[1] - arr[0])
        if n == 1:
            return 0

        prev_prev = {j: float('inf') for j in range(n)}
        prev = {j: float('inf') for j in range(n)}
        for j in prev:
            prev[j] = abs(arr[0] - arr[j])

        for index in range(1, n):
            curr = {j: float('inf') for j in range(n)}
            for prev_index in range(n):
                right = float('inf')
                if index - 2 >= 0:
                    right = prev_prev[index]
                left = prev[index]
                curr[prev_index] = min(left, right) + abs(arr[prev_index] - arr[index])
            prev_prev = prev
            prev = curr

        return min(prev_prev[n - 1], prev[n - 1])

    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()