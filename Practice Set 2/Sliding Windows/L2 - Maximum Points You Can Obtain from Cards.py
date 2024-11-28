# Problem link - https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/0
# Solution - https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2


class Solution:
    """
        Time complexity is O(n) and space complexity is O(1).
    """

    @staticmethod
    def max_points_from_cards(cards, k):
        if k <= 0:
            return 0
        if k >= len(cards):
            return sum(cards)
        left = k - 1
        right = n = len(cards)
        pts = _sum = sum(cards[:k])
        while left >= 0:
            new_pts = _sum - cards[left] + cards[right - 1]
            left -= 1
            right -= 1
            pts = max(pts, new_pts)
            _sum = new_pts
        return pts


print(Solution.max_points_from_cards([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.max_points_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.max_points_from_cards([2, 2, 2], 2))
print(Solution.max_points_from_cards([9, 7, 7, 9, 7, 7, 9], 7))
print(Solution.max_points_from_cards([8, 6, 2, 4, 5], 5))
