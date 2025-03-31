# Problem link - https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/0
# Solution - https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2


class Solution:
    @staticmethod
    def get_max_points(cards, k):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        # if k is negative, no points will be obtained.
        if k <= 0:
            return 0
        # if k is more than the number of cards, return the sum of all the points.
        if k >= len(cards):
            return sum(cards)

        # now, keep j at n - 1 and i at k - 1. Compute the sum till kth index and store the answer in max_points and
        # last_sum variables. `last_sum` variable will be used to update the max points.
        max_points = sum(cards[:k])
        last_sum = max_points
        i, j = k - 1, len(cards) - 1

        # until and unless you have a left window, i.e., i >= 0.
        while i >= 0:
            # subtract current ith value and add current jth value.
            last_sum = last_sum - cards[i] + cards[j]
            # update max_points using last sum.
            max_points = max(max_points, last_sum)
            # decrement both i and j.
            i -= 1
            j -= 1
        # return max_points.
        return max_points


print(Solution.get_max_points([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.get_max_points([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.get_max_points([2, 2, 2], 2))
print(Solution.get_max_points([8, 6, 2, 4, 5], 5))