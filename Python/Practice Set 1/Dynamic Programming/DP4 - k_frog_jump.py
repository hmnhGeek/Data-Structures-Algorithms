def recursive():
    def solve(arr, index, k):
        if index == 0:
            return 0

        min_energy = float('inf')
        for j in range(1, k + 1):
            if index - j >= 0:
                energy = solve(arr, index - j, k) + abs(arr[index] - arr[index - j])
                min_energy = min(min_energy, energy)
        return min_energy

    def k_frog_jump(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(k_frog_jump([10, 30, 40, 50, 20], 3))
    print(k_frog_jump([10, 20, 10], 1))
    print(k_frog_jump([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))


def memoized():
    # T: O(n) and S: O(2n)
    def solve(arr, index, k, dp):
        if index == 0:
            return 0

        if dp[index] is not None:
            return dp[index]

        min_energy = float('inf')
        for j in range(1, k + 1):
            if index - j >= 0:
                energy = solve(arr, index - j, k, dp) + abs(arr[index] - arr[index - j])
                min_energy = min(min_energy, energy)
        dp[index] = min_energy
        return dp[index]

    def k_frog_jump(arr, k):
        n = len(arr)
        dp = {i: None for i in range(n)}
        return solve(arr, n - 1, k, dp)

    print(k_frog_jump([10, 30, 40, 50, 20], 3))
    print(k_frog_jump([10, 20, 10], 1))
    print(k_frog_jump([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))


def tabulation():
    # T: O(n) and S: O(n)
    def k_frog_jump(arr, k):
        n = len(arr)
        dp = {i: float('inf') for i in range(n)}
        dp[0] = 0

        for index in range(1, n):
            min_energy = float('inf')
            for j in range(1, k + 1):
                if index - j >= 0:
                    energy = dp[index - j] + abs(arr[index] - arr[index - j])
                    min_energy = min(min_energy, energy)
            dp[index] = min_energy
        return dp[n - 1]

    print(k_frog_jump([10, 30, 40, 50, 20], 3))
    print(k_frog_jump([10, 20, 10], 1))
    print(k_frog_jump([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))


recursive()
print()
memoized()
print()
tabulation()