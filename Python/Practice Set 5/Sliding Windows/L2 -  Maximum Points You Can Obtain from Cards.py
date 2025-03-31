# Problem link - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
# Solution - https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2


class Solution:
    @staticmethod
    def max_pts_from_cards(cards, k):
        """
            Time complexity is O(k) and space complexity is O(1).
        """
        if 0 >= k > len(cards):
            return -1
        max_sum = tracking_sum = sum(cards[:k])
        i, j = k - 1, len(cards)
        while i >= 0:
            tracking_sum -= cards[i]
            i -= 1
            j -= 1
            tracking_sum += cards[j]
            max_sum = max(max_sum, tracking_sum)
        return max_sum


print(Solution.max_pts_from_cards([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.max_pts_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.max_pts_from_cards([2, 2, 2], 2))
print(Solution.max_pts_from_cards([9, 7, 7, 9, 7, 7, 9], 7))
print(Solution.max_pts_from_cards([8, 6, 2, 4, 5], 5))
print(Solution.max_pts_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.max_pts_from_cards([9, 7, 5, 3, 2, 1, 8], 4))
print(Solution.max_pts_from_cards([8, 7, 5, 3, 2], 3))
print(Solution.max_pts_from_cards([5, 4, 9, 7, 8], 5))
