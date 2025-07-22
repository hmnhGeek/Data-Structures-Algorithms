class Solution:
    @staticmethod
    def _get_max_elem(mtx, mid, n):
        max_elem, max_elem_index = -1e6, -1
        for i in range(n):
            if mtx[i][mid] > max_elem:
                max_elem = mtx[i][mid]
                max_elem_index = i
        return max_elem, max_elem_index

    @staticmethod
    def find_peak(mtx):
        n, m = len(mtx), len(mtx[0])
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            possible_peak_element, max_elem_index_in_mid_col = Solution._get_max_elem(mtx, mid, n)
            peak_flag = Solution._get_peak_flag(mtx, possible_peak_element, max_elem_index_in_mid_col, mid, m)
            if peak_flag == 0:
                return max_elem_index_in_mid_col, mid
            elif peak_flag == 1:
                low = mid + 1
            elif peak_flag == -1:
                high = mid - 1
            else:
                low = mid + 1
        return -1, -1

    @staticmethod
    def _get_peak_flag(mtx, possible_peak_element, i, mid, m):
        left_is_smaller = False
        if 0 <= mid - 1 < m:
            if mtx[i][mid - 1] < possible_peak_element:
                left_is_smaller = True
        else:
            left_is_smaller = True
        right_is_smaller = False
        if 0 <= mid + 1 < m:
            if mtx[i][mid + 1] < possible_peak_element:
                right_is_smaller = True
        else:
            right_is_smaller = True
        if left_is_smaller and right_is_smaller:
            return 0
        if left_is_smaller and not right_is_smaller:
            return 1
        if not left_is_smaller and right_is_smaller:
            return -1
        return 1


print(
    Solution.find_peak(
        [[8, 6], [10, 1]]
    )
)

print(
    Solution.find_peak(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)

print(Solution.find_peak([[1, 4], [3, 2]]))
print(Solution.find_peak([[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
