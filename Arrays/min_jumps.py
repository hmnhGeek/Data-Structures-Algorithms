def recursive():
    def solve(arr, index, n):
        if index >= n - 1:
            return 0
        if arr[index] == 0:
            return 1e6

        min_steps = 1e6
        for i in range(1, arr[index] + 1):
            min_steps = min(min_steps, 1 + solve(arr, index + i, n))
        return min_steps

    def min_jumps(arr):
        n = len(arr)
        min_steps_found = solve(arr, 0, n)
        return min_steps_found if min_steps_found < 1e6 else -1

    print(min_jumps([1, 4, 3, 2, 6, 7]))
    print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    print(min_jumps([0, 10, 20]))
    print(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(min_jumps([2, 3, 1, 1, 4]))
    print(min_jumps([2, 3, 0, 1, 4]))


recursive()
