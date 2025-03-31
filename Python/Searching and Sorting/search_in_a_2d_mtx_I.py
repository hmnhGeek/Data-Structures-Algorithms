# Problem link - https://leetcode.com/problems/search-a-2d-matrix/description/

def convert_to_coordinates(x, m):
    # x // m denotes consumed rows in the matrix which is apparently the row index at
    # which the element denoted by x is residing. x % m denotes the column index.
    return x // m, x % m


def search(mtx, target):
    # this takes O(log(mn)) time and O(1) space.
    n, m = len(mtx), len(mtx[0])

    low = 0
    high = m*n - 1

    # typical binary search, if target is found return true, else modify low and high.
    while low <= high:
        mid = int(low + (high - low)/2)
        row, col = convert_to_coordinates(mid, m)

        if mtx[row][col] == target:
            return True
        elif target > mtx[row][col]:
            low = mid + 1
        else:
            high = mid - 1

    return False

print(
    search(
        [
            [3, 4, 7, 9],
            [12, 13, 16, 18],
            [20, 21, 23, 24]
        ],
        23
    )
)

print(
    search(
        [
            [3, 4, 7, 9],
            [12, 13, 16, 18],
            [20, 21, 23, 24]
        ],
        77
    )
)

print(
    search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
)

print(
    search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
)