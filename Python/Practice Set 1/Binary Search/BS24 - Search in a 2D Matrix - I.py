# Problem link - https://leetcode.com/problems/search-a-2d-matrix/
# Solution - https://www.youtube.com/watch?v=JXU4Akft7yk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=26


class Solution:
    @staticmethod
    def search(mtx, target):
        """
            Time complexity is O(log(nm)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])

        # since the entire matrix if flattened to an array, is sorted, define search space of 0 --> nm - 1.
        low = 0
        high = n * m - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            x, y = mid // m, mid % m

            # if mid-element is target, return its coordinates.
            if mtx[x][y] == target:
                return x, y
            if mtx[x][y] > target:
                # if mid-element is larger than target, lower down the search space to left side.
                high = mid - 1
            else:
                # if mid-element is smaller than target, lower down the search space to right side.
                low = mid + 1
        # return -1, -1 if element is not found.
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

print(
    Solution.search(
        [
            [3, 4, 7, 9],
            [12, 13, 16, 18],
            [20, 21, 23, 29]
        ],
        28
    )
)
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(
    Solution.search(
        [[18, 21, 27],
         [38, 55, 67]],
        55
    )
)
