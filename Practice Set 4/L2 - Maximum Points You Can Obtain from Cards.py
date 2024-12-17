class Solution:
    @staticmethod
    def max_pts_from_cards(arr, k):
        n = len(arr)
        if k == n:
            return sum(arr)
        if k not in range(n):
            return -1
        _sum = tracker = sum(arr[:k])
        i, j = k - 1, n
        while i >= 0:
            tracker += (arr[j - 1] - arr[i])
            _sum = max(_sum, tracker)
            i -= 1
            j -= 1
        return _sum


print(Solution.max_pts_from_cards([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.max_pts_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.max_pts_from_cards([2, 2, 2], 2))
print(Solution.max_pts_from_cards([9, 7, 7, 9, 7, 7, 9], 7))
print(Solution.max_pts_from_cards([8, 6, 2, 4, 5], 5))
print(Solution.max_pts_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.max_pts_from_cards([9, 7, 5, 3, 2, 1, 8], 4))
print(Solution.max_pts_from_cards([8, 7, 5, 3, 2], 3))
print(Solution.max_pts_from_cards([5, 4, 9, 7, 8], 5))
