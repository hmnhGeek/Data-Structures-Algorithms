# Problem link - https://www.naukri.com/code360/problems/common-elements-present-in-all-rows-of-a-matrix_1118111


def find_common(mtx):
    """
        Time complexity is O(m*n) and space is O(m).
    """

    # store the unique elements from the first row.
    prev = set(mtx[0])

    # iterate from the first row
    for i in range(1, len(mtx)):
        # initialize a current set to store all the common elements till this row.
        curr = set()
        # iterate on each column of this row
        for j in mtx[i]:
            # if the current value is in prev row, add it in curr set
            if j in prev:
                curr.add(j)

        # update prev
        prev = curr

    # return prev
    return prev


print(
    find_common(
        [
            [1, 2, 1, 4, 8],
            [3, 7, 8, 5, 1],
            [8, 7, 7, 3, 1],
            [8, 1, 2, 7, 9]
        ]
    )
)

print(find_common([[2, 3, 4, 7], [0, 0, 3, 5], [1, 3, 8, 9]]))

print(
    find_common(
        [
            [1, 4, 5, 6],
            [3, 4, 5, 6],
            [5, 6, 7, 2]
        ]
    )
)

print(
    find_common(
        [
            [4, 6],
            [6, 4],
            [2, 6]
        ]
    )
)

print(
    find_common(
        [
            [1, 2, 3],
            [2, 2, 3],
            [2, 3, 1],
            [2, 3, 4]
        ]
    )
)

print(
    find_common(
        [
            [1, 2, 3],
            [0, 6, 0],
            [4, 6, 1],
        ]
    )
)
