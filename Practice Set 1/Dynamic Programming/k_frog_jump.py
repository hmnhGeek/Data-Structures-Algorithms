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


recursive()