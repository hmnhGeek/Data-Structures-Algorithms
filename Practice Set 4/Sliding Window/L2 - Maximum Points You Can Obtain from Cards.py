# Problem link - https://www.naukri.com/code360/problems/maximum-points-from-cards_8391016
# Solution - https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2


class Solution:
    @staticmethod
    def max_pts_from_cards(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(arr)

        # edge cases
        if k >= n:
            return sum(arr)
        if k < 0:
            return 0

        # create variables to track max sum and current sum, initially both equal.
        _sum = tracker = sum(arr[:k])
        # keep i at k - 1 index and j at n (out of bounds)
        i, j = k - 1, n

        while i >= 0:
            # update the new sum by add j - 1 index and excluding i index
            tracker += (arr[j - 1] - arr[i])
            # update max sum
            _sum = max(_sum, tracker)
            # decrement both i and j
            i -= 1
            j -= 1
        # return max sum
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
