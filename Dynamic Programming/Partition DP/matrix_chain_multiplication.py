

"""
    This is a typical partition DP problem. According to the question, if the matrix sizes are given as
    [10, 20, 30, 40, 50], then these imply as follows:

    Matrix A: 10 X 20
    Matrix B: 20 X 30
    Matrix C: 30 X 40
    Matrix D: 40 X 50

    That is, there are n - 1 matrices. To get the minimum number of operations for multiplying these matrices,
    we can do the following:
                                (ABCD)
                    (A)(BCD)   (AB)(CD)   (ABC)(D)
                (B)(CD)  (BC)(D) ....................

    At each recursion output, we would take the minimum cost from all the branches.
"""


def recursive():
    """
        Overall time complexity is exponential and space complexity is O(N).
    """

    def solve_problem(sizes_array, i, j):
        # if we have a single matrix, then there is no multiplication needed, return 0 operations.
        if i == j:
            return 0

        # we are about to start the partition algorithm, store minimum number of operations as infinite.
        min_operations = float('inf')

        # assume `k` to be the partition index. Partitions would be like (A), (AB), (ABC).
        # So k would assume values from 1 to j - 1.
        for k in range(i, j):
            # the number of operations involved for the current partition would be
            # { A[i - 1] * A[k] * A[j] } + f(i, k) + f(k + 1, j). The number of operations in matrix multiplication is
            # usually x * y * z where first matrix is of size x * y and the second matrix is of size y * z. Please watch
            # the solution video for more understanding.
            steps = sizes_array[i - 1] * sizes_array[k] * sizes_array[j] + \
                solve_problem(sizes_array, i, k) + solve_problem(sizes_array, k + 1, j)

            # update the minimum operations required by performing this partition.
            min_operations = min(min_operations, steps)

        # return the overall minimum number of operations required.
        return min_operations

    def matrix_chain_multiplication(sizes_array):
        n = len(sizes_array)
        # Solve for matrices (ABCD), i.e., i = 1 to i = n - 1. Note that the dimension of ith matrix is
        # A[i - 1] X A[i].
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