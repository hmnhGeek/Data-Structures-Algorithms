# Problem link - https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/0
# Solution - https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2


class Solution:
    @staticmethod
    def get_max_points(cards, k):
        """
            Time complexity is O(k) and space complexity is O(1).
        """
        n = len(cards)
        i, j = k - 1, n
        max_points = tracking_points = sum(cards[:k])
        while i >= 0:
            tracking_points -= cards[i]
            i -= 1
            j -= 1
            tracking_points += cards[j]
            max_points = max(max_points, tracking_points)
        return max_points


print(Solution.get_max_points([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.get_max_points([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.get_max_points([2, 2, 2], 2))
print(Solution.get_max_points([8, 6, 2, 4, 5], 5))
