# Problem link - https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
# Solution - https://www.youtube.com/watch?v=SCz-1TtYxDI&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=25


class Solution:
    @staticmethod
    def _get_1s_count(arr, low, high):
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == 1:
                # since mid is 1, try finding 1 in lower part.
                high = mid - 1
            else:
                # since mid is 0, try finding 1 in higher part.
                low = mid + 1
        return len(arr) - low

    @staticmethod
    def get_max_1s(mtx):
        """
            Overall time complexity is O(n*log(m)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        max_1s = 0
        max_1s_row = None
        # loop from the last row towards the first row as we want the first row having max 1s. Overall time complexity
        # is O(n*log(m)).
        for row in range(n - 1, -1, -1):
            # get the count of 1s in this row in log(m) time.
            ones_count = Solution._get_1s_count(mtx[row], 0, m - 1)
            # even if the 1s count is same, update the row.
            if max_1s <= ones_count:
                max_1s = ones_count
                max_1s_row = row
        # return the first row with max 1s.
        return max_1s_row


print(Solution.get_max_1s([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.get_max_1s([[1, 1], [1, 1]]))
print(Solution.get_max_1s([[0, 0, 0], [0, 1, 1]]))
print(Solution.get_max_1s([[0, 0], [1, 1], [0, 0]]))
print(Solution.get_max_1s([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.get_max_1s([[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0]]))
