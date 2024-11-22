def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, index, k):
        if index == 0:
            return 0

        min_energy = 1e6
        for i in range(1, k + 1):
            if index - i >= 0:
                min_energy = min(min_energy, abs(arr[index] - arr[index - i]) + solve(arr, index - i, k))
        return min_energy

    def frog_jump(arr, k):
        if k <= 0:
            return
        n = len(arr)
        return solve(arr, n - 1, k)

    print(frog_jump([10, 30, 50, 60, 20, 10], 3))
    print(frog_jump([10, 30, 50, 60, 20, 10], 2))
    print(frog_jump([10, 30, 50, 60, 20, 10], 4))
    print(frog_jump([10, 30, 50, 60, 20, 10], 1))
    print(frog_jump([10, 30, 40, 50, 20], 3))
    print(frog_jump([10, 20, 10], 1))
    print(frog_jump([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(2n).
    """
    def solve(arr, index, k, dp):
        if index == 0:
            return 0

        if dp[index] is not None:
            return dp[index]

        min_energy = 1e6
        for i in range(1, k + 1):
            if index - i >= 0:
                min_energy = min(min_energy, abs(arr[index] - arr[index - i]) + solve(arr, index - i, k, dp))
        dp[index] = min_energy
        return dp[index]

    def frog_jump(arr, k):
        if k <= 0:
            return
        n = len(arr)
        dp = {i: None for i in range(n)}
        return solve(arr, n - 1, k, dp)

    print(frog_jump([10, 30, 50, 60, 20, 10], 3))
    print(frog_jump([10, 30, 50, 60, 20, 10], 2))
    print(frog_jump([10, 30, 50, 60, 20, 10], 4))
    print(frog_jump([10, 30, 50, 60, 20, 10], 1))
    print(frog_jump([10, 30, 40, 50, 20], 3))
    print(frog_jump([10, 20, 10], 1))
    print(frog_jump([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))


def tabulation():
    """
        Time complexity is O(n*k) and space complexity is O(n).
    """
    def frog_jump(arr, k):
        if k <= 0:
            return
        n = len(arr)
        dp = {i: 1e6 for i in range(n)}
        dp[0] = 0
        for index in range(1, n):
            min_energy = 1e6
            for i in range(1, k + 1):
                if index - i >= 0:
                    min_energy = min(min_energy, abs(arr[index] - arr[index - i]) + dp[index - i])
            dp[index] = min_energy
        return dp[n - 1]

    print(frog_jump([10, 30, 50, 60, 20, 10], 3))
    print(frog_jump([10, 30, 50, 60, 20, 10], 2))
    print(frog_jump([10, 30, 50, 60, 20, 10], 4))
    print(frog_jump([10, 30, 50, 60, 20, 10], 1))
    print(frog_jump([10, 30, 40, 50, 20], 3))
    print(frog_jump([10, 20, 10], 1))
    print(frog_jump([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))


recursive()
print()
memoized()
print()
tabulation()