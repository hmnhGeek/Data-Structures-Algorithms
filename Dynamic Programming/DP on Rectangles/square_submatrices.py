def count_square_sub_matrices(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = matrix[i][0]

    for j in range(n):
        dp[0][j] = matrix[0][j]

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

    count = 0
    for i in range(n):
        for j in range(m):
            count += dp[i][j]

    return count


print(
    count_square_sub_matrices(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(
    count_square_sub_matrices(
        [
            [1, 0],
            [0, 1]
        ]
    )
)

print(
    count_square_sub_matrices(
        [
            [0, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 1, 0]
        ]
    )
)