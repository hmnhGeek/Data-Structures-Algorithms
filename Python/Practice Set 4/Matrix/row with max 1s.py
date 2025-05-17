# Problem link - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1


class Solution:
    @staticmethod
    def _get_ones_count(mtx, i, low, high, m):
        arr = mtx[i]
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return m - low

    @staticmethod
    def max1s_row(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])

        # store the row index and max count of ones in a variable.
        max_1s = 0
        row = -1

        # loop on the rows
        for i in range(n):
            # count the ones in each row in O(log(m)) time.
            ones_count = Solution._get_ones_count(mtx, i, 0, m - 1, m)

            # if ones count found > max count of ones, update the result variables.
            if ones_count > max_1s:
                row = i
                max_1s = ones_count

        # return the index of the first row with max ones.
        return row


print(Solution.max1s_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max1s_row([[0, 0], [1, 1]]))
print(Solution.max1s_row([[0, 0], [0, 0]]))
print(Solution.max1s_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max1s_row([[1, 1], [1, 1]]))
