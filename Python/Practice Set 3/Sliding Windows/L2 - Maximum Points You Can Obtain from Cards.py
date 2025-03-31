# Problem link - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
# Solution - https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2


class Solution:
    @staticmethod
    def max_pts_from_cards(arr, k):
        """
            Time complexity is O(k) and space complexity is O(1).
        """

        # edge case check
        if k not in range(len(arr) + 1):
            return -1

        # calculate sum till k index.
        _sum = _new_sum = sum(arr[:k])

        # store i, j tracking pointers
        i, j = k - 1, len(arr)

        # while there is ground to cover
        while i >= 0:
            # update the new sum by reducing the ith index value and adding the (j - 1)th index value.
            _new_sum = _new_sum + arr[j - 1] - arr[i]
            # update the _sum with max value
            _sum = max(_sum, _new_sum)
            # reduce i and j
            i -= 1
            j -= 1

        # return max _sum value.
        return _sum


print(Solution.max_pts_from_cards([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.max_pts_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.max_pts_from_cards([2, 2, 2], 2))
print(Solution.max_pts_from_cards([9, 7, 7, 9, 7, 7, 9], 7))
