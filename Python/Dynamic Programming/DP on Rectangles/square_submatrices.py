# Problem link - https://www.naukri.com/code360/problems/count-square-submatrices-with-all-ones_3751502?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=auS1fynpnjo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=58


def count_square_sub_matrices(matrix):
    """
        Overall time complexity is O(nm) and overall space complexity is O(nm).
    """

    n, m = len(matrix), len(matrix[0])

    # create a O(nm) dp matrix.
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # copy the first column as is.
    for i in range(n):
        dp[i][0] = matrix[i][0]

    # copy the first row as is.
    for j in range(n):
        dp[0][j] = matrix[0][j]

    # start from (1, 1) till (n - 1, m - 1).
    for i in range(1, n):
        for j in range(1, m):
            # if the current cell is non-zero, take the min of top, top-left and left and add a 1.
            if matrix[i][j] != 0:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

    # sum the dp-matrix to get the total count as answer.
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