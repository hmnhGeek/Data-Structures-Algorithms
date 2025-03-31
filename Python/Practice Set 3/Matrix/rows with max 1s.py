# Problem link - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1


class Solution:
    @staticmethod
    def _find_count(mtx, i, n, m):
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if mtx[i][mid] == 1:
                # if mid is 1, try searching lower
                high = mid - 1
            else:
                # else search higher.
                low = mid + 1
        return n - low

    @staticmethod
    def max1s_row(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        # store the row index and max count of ones in a variable.
        row_idx = -1
        count_1s = 0

        # loop on the rows
        for i in range(n):
            # count the ones in each row in O(log(m)) time.
            ones_count = Solution._find_count(mtx, i, n, m)

            # if ones count found > max count of ones, update the result variables.
            if ones_count > count_1s:
                count_1s = ones_count
                row_idx = i

        # return the index of the first row with max ones.
        return row_idx


print(Solution.max1s_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max1s_row([[0, 0], [1, 1]]))
print(Solution.max1s_row([[0, 0], [0, 0]]))
print(Solution.max1s_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max1s_row([[1, 1], [1, 1]]))
