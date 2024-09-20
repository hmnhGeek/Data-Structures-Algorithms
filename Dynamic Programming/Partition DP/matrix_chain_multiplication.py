def recursive():
    def solve_problem(sizes_array, i, j):
        if i == j:
            return 0

        mini = float('inf')
        for k in range(i, j):
            steps = sizes_array[i - 1] * sizes_array[k] * sizes_array[j] + \
                solve_problem(sizes_array, i, k) + solve_problem(sizes_array, k + 1, j)
            mini = min(mini, steps)

        return mini

    def matrix_chain_multiplication(sizes_array):
        n = len(sizes_array)
        return solve_problem(sizes_array, 1, n - 1)

    print(matrix_chain_multiplication([4, 5, 3, 2]))
    print(matrix_chain_multiplication([10, 15, 20, 25]))
    print(matrix_chain_multiplication([1, 4, 3, 2]))


def memoized():
    def solve_problem(sizes_array, i, j, dp):
        if i == j:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        mini = float('inf')
        for k in range(i, j):
            steps = sizes_array[i - 1] * sizes_array[k] * sizes_array[j] + \
                solve_problem(sizes_array, i, k, dp) + solve_problem(sizes_array, k + 1, j, dp)
            mini = min(mini, steps)

        dp[i][j] = mini
        return dp[i][j]

    def matrix_chain_multiplication(sizes_array):
        n = len(sizes_array)
        dp = {i: {j: None for j in range(n)} for i in range(n)}
        return solve_problem(sizes_array, 1, n - 1, dp)

    print(matrix_chain_multiplication([4, 5, 3, 2]))
    print(matrix_chain_multiplication([10, 15, 20, 25]))
    print(matrix_chain_multiplication([1, 4, 3, 2]))


recursive()
print()
memoized()