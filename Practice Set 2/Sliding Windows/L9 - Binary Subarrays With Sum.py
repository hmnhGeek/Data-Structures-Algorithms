# Problem link - https://leetcode.com/problems/binary-subarrays-with-sum/description/
# Solution - https://www.youtube.com/watch?v=XnMdNUkX6VM&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=9


class Solution:
    @staticmethod
    def _get_count(arr, goal):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        if goal < 0:
            return 0

        # define window variables
        left = right = 0
        n = len(arr)
        _sum = 0
        count = 0

        # while there is ground to cover.
        while right < n:
            # add to sum the value of `right`.
            _sum += arr[right]

            # while the sum > goal, shrink from left.
            while _sum > goal:
                _sum -= arr[left]
                left += 1

            # update the count
            count += (right - left + 1)

            # increment right
            right += 1

        # return the count.
        return count

    @staticmethod
    def get_count(arr, goal):
        """
            T: O(2n) and S: O(1).
        """
        return Solution._get_count(arr, goal) - Solution._get_count(arr, goal - 1)


print(Solution.get_count([1, 0, 1, 0, 1], 2))
print(Solution.get_count([0, 0, 0, 0, 0], 0))
print(Solution.get_count([1, 0, 1, 1, 0, 1], 2))
print(Solution.get_count([1, 0, 1, 1, 1, 0, 1], 3))
print(Solution.get_count([1, 1, 0, 1, 1], 5))
