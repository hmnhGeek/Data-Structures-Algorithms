def recursive():
    def solve(arr, i, j):
        if i == j:
            return 0

        min_val = 1e6
        for k in range(i, j):
            steps = (arr[i - 1] * arr[k] * arr[j]) + solve(arr, i, k) + solve(arr, k + 1, j)
            min_val = min(min_val, steps)
        return min_val

    def matrix_chain_multiplication(arr):
        n = len(arr)
        return solve(arr, 1, n - 1)

    print(matrix_chain_multiplication([10, 20, 30, 40, 50]))
    print(matrix_chain_multiplication([4, 5, 3, 2]))
    print(matrix_chain_multiplication([10, 15, 20, 25]))
    print(matrix_chain_multiplication([1, 4, 3, 2]))


recursive()