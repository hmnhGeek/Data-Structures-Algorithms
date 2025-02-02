# Problem link - https://www.naukri.com/code360/problems/row-with-maximum-1-s_1112656
# Solution - https://www.youtube.com/watch?v=SCz-1TtYxDI&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=25


class Solution:
    @staticmethod
    def _count_of_one(arr, low, high):
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return len(arr) - low

    @staticmethod
    def max_1_row(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        max_1s, index = 0, -1
        for i in range(n):
            one_count = Solution._count_of_one(mtx[i], 0, m - 1)
            if one_count > max_1s:
                max_1s = one_count
                index = i
        return index


print(Solution.max_1_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max_1_row([[1, 1], [1, 1]]))
print(Solution.max_1_row([[0, 0, 0], [0, 1, 1]]))
print(Solution.max_1_row([[0, 0], [1, 1], [0, 0]]))
print(Solution.max_1_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max_1_row([[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0]]))
