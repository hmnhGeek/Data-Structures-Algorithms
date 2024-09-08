# Problem link - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1


def count_1s(row, low, high):
    # Time complexity is O(log(len(row)))
    # Typical binary search algorithm to find that index (given by `low` value at end), which denotes
    # the index of first 1 in the row.
    while low <= high:
        mid = int(low + (high - low) / 2)
        if row[mid] == 1:
            high = mid - 1
        else:
            low = mid + 1

    # return the count of 1s in this row.
    return len(row) - low


def get_row_with_max_1s(mtx):
    result = None
    mx_count = 0
    n, m = len(mtx), len(mtx[0])

    # This will take O(n*log(m)) time
    for row in range(n):
        one_count = count_1s(mtx[row], 0, m - 1)
        if mx_count < one_count:
            mx_count = one_count
            result = row
    return result


print(
    get_row_with_max_1s(
        [[0, 1, 1, 1],
         [0, 0, 1, 1],
         [1, 1, 1, 1],
         [0, 0, 0, 0]]
    )
)

print(
    get_row_with_max_1s(
        [[0, 0],
         [1, 1]]
    )
)

print(
    get_row_with_max_1s(
        [
            [0, 0, 1, 1],
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 0]
        ]
    )
)

print(
    get_row_with_max_1s(
        [
            [0, 0, 0],
            [0, 1, 1]
        ]
    )
)