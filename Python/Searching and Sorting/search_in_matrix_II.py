# Video - https://www.youtube.com/watch?v=9ZbB397jU4k&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=27

def search(mtx, target):
    # Overall time complexity is O(n + m) in the worst case when target is at (n - 1, 0).
    # It's like exploring a path. To reach (n - 1, 0) you have to cover all the rows, i.e.
    # n steps and all the columns i.e., m steps. In total, n + m depth.
    # Space complexity is O(1).

    n, m = len(mtx), len(mtx[0])

    # we can start from either top right corner or bottom-left corner
    # but not from top-left and bottom right. We have to eliminate possibilities.
    # At cell (0, m - 1), our target can be this cell or if it is greater than this
    # then it cannot be found in its row (because we are at the max elem of the row).
    # However, the element can be found in the column of m - 1, because the cell at
    # which we are standing is the smallest in its column. So we eliminate the row
    # and increase to row += 1. Vice versa scenario also works. In that we do col -= 1.
    start_row = 0
    start_col = m - 1

    # until we have some rows and columns to explore.
    while start_row < n and start_col >= 0:
        if mtx[start_row][start_col] == target:
            return start_row, start_col

        # as explained above, if target is bigger, move to next row.
        if target > mtx[start_row][start_col]:
            start_row += 1
        else:
            # else move to previous column.
            start_col -= 1

    # finally, if you are out of bounds, the element was not found.
    return -1, -1

m = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(search(m, 14))
print(search(m, 100))