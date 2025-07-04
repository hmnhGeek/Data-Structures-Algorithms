def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, i, k):
        if i == 0:
            return 0
        min_energy = 1e6
        for j in range(1, k + 1):
            if i - j >= 0:
                min_energy = min(min_energy, abs(arr[i - j] - arr[i]) + solve(arr, i - j, k))
        return min_energy

    def frog_jump(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(frog_jump([10, 30, 50, 60, 20, 10], 3))
    print(frog_jump([10, 30, 50, 60, 20, 10], 2))
    print(frog_jump([10, 30, 50, 60, 20, 10], 4))
    print(frog_jump([10, 30, 50, 60, 20, 10], 1))
    print(frog_jump([10, 30, 40, 50, 20], 3))
    print(frog_jump([10, 20, 10], 1))
    print(frog_jump([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))


recursive()