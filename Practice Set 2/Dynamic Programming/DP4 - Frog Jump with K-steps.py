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


recursive()