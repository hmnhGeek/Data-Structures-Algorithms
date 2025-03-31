# Problem link - https://leetcode.com/problems/search-a-2d-matrix-ii/
# Solution - https://www.youtube.com/watch?v=9ZbB397jU4k&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=27


class Solution:
    @staticmethod
    def search(mtx, target):
        """
            Time complexity is O(n + m) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])

        # either start searching from top right or bottom left corner
        i, j = 0, m - 1

        # while the pointers are within range.
        while i < n and j >= 0:
            # if the cell at (i, j) is same as target.
            if mtx[i][j] == target:
                return i, j

            # if cell at (i, j) is greater than target, then target can never be found at current column.
            if mtx[i][j] > target:
                j -= 1
            else:
                # similarly, the target cannot be found at current row.
                i += 1

        # if element is not found, return False.
        return False


print(
    Solution.search(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        14
    )
)

print(Solution.search(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
print(Solution.search(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))

print(
    Solution.search(
        [
            [1, 2, 4, 5],
            [3, 4, 9, 16],
            [7, 10, 14, 29]
        ],
        8
    )
)

print(
    Solution.search(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        5
    )
)