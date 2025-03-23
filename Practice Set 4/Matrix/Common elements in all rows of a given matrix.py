# Problem link - https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/


class Solution:
    @staticmethod
    def get_commons(mtx):
        """
            Time complexity is O(m * n) and space complexity is O(m).
        """

        n, m = len(mtx), len(mtx[0])

        # if there is only one row in the matrix, return that row itself.
        if n == 1:
            return mtx[0]

        # find common elements in the first two rows of the matrix.
        set1 = set(mtx[0])
        set2 = set(mtx[1])
        prev = set1.intersection(set2)

        # if there were only 2 rows, return the common elements between them.
        if n == 2:
            return list(prev)

        # else iterate on the remaining rows by taking common elements.
        i = 2
        while i < n:
            prev = prev.intersection(set(mtx[i]))
            i += 1

        # finally, return the common elements in all the rows.
        return list(prev)


print(
    Solution.get_commons(
        [
            [1, 2, 1, 4, 8],
            [3, 7, 8, 5, 1],
            [8, 7, 7, 3, 1],
            [8, 1, 2, 7, 9]
        ]
    )
)
