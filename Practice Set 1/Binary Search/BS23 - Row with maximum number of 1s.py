# Problem link - https://www.naukri.com/code360/problems/row-with-maximum-1-s_1112656
# Solution - https://www.youtube.com/watch?v=SCz-1TtYxDI&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=25


class Solution:
    @staticmethod
    def _count_1s(arr, low, high, n):
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return n - low

    @staticmethod
    def max_1_row(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(m).
        """

        n, m = len(mtx), len(mtx[0])
        max_1s_till_now = 0
        row = -1
        for i in range(n - 1, -1, -1):
            # update the max count of 1s by finding the count of 1s for this row in O(log(m)) time.
            count_of_1s = Solution._count_1s(mtx[i], 0, m - 1, m)
            if max_1s_till_now <= count_of_1s:
                max_1s_till_now = count_of_1s
                row = i
        return row


print(Solution.max_1_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max_1_row([[1, 1], [1, 1]]))
print(Solution.max_1_row([[0, 0, 0], [0, 1, 1]]))
print(Solution.max_1_row([[0, 0], [1, 1], [0, 0]]))
print(Solution.max_1_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max_1_row([[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0]]))
