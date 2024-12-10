class Solution:
    @staticmethod
    def max_pts_from_cards(arr, k):
        _sum = _new_sum = sum(arr[:k])
        i, j = k - 1, len(arr)
        while i >= 0:
            _new_sum = _new_sum + arr[j - 1] - arr[i]
            _sum = max(_sum, _new_sum)
            i -= 1
            j -= 1
        return _sum


print(Solution.max_pts_from_cards([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.max_pts_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.max_pts_from_cards([2, 2, 2], 2))
print(Solution.max_pts_from_cards([9, 7, 7, 9, 7, 7, 9], 7))
