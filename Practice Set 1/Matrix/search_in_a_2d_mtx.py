# Problem link - https://leetcode.com/problems/search-a-2d-matrix/description/


def search(mtx, target):
    n, m = len(mtx), len(mtx[0])
    low = 0
    high = m * n - 1

    while low <= high:
        mid = int(low + (high - low) / 2)
        i, j = mid // m, mid % m
        if mtx[i][j] == target:
            return i, j
        if mtx[i][j] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(
    search(
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ],
        3
    )
)

print(search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
