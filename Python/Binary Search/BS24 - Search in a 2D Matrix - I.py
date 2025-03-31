# Problem link - https://www.naukri.com/code360/problems/search-in-a-2d-matrix_980531
# Solution - https://www.youtube.com/watch?v=JXU4Akft7yk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=26


class Solution:
    @staticmethod
    def search(mtx, target):
        """
            Time complexity is O(log(mn)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])

        # define the search space.
        low = 0
        high = n * m - 1

        # typical binary search
        while low <= high:
            # get the mid and then the possible cell coordinates
            mid = int(low + (high - low) / 2)
            row = mid // m
            col = mid % m

            # if the element is found, return the coordinates
            if mtx[row][col] == target:
                return row, col

            # if the element at cell is larger than target, search lower.
            if mtx[row][col] > target:
                high = mid - 1
            else:
                # else search higher.
                low = mid + 1

        # return -1 to denote that target was not found.
        return -1, -1


print(
    Solution.search(
        [
            [3, 4, 7, 9],
            [12, 13, 16, 18],
            [20, 21, 23, 29]
        ],
        23
    )
)

print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution.search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
