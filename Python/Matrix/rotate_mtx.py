def transpose(mtx):
    # This will take O(n^2) time and O(1) space.
    n = len(mtx)
    for i in range(n):
        for j in range(i + 1, n):
            mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]


def rotate(mtx):
    # overall time is O(n^2) and O(1) space.

    n = len(mtx)

    # this will take O(n) time
    for i in range(n):
        mtx[i] = mtx[i][-1:-n-1:-1]

    # O(n^2) time
    transpose(mtx)

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(m)
print(m)

m2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotate(m2)
print(m2)