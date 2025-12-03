# Problem link - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1


class Solution:
    @staticmethod
    def get_1_count(arr):
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == 0:
                low = mid + 1
            else:
                high = mid - 1
        return n - low

    @staticmethod
    def get_row_with_max_1s(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """
        n, m = len(mtx), len(mtx[0])
        index = -1
        one_count = 0
        for i in range(n):
            row = mtx[i]
            x = Solution.get_1_count(row)
            if x > one_count:
                one_count = x
                index = i
        return index


print(Solution.get_row_with_max_1s([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.get_row_with_max_1s([[0, 0], [1, 1]]))
print(Solution.get_row_with_max_1s([[0, 0], [0, 0]]))
print(Solution.get_row_with_max_1s([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.get_row_with_max_1s([[1, 1], [1, 1]]))
