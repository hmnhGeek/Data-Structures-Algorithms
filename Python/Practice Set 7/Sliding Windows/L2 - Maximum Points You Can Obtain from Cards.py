# Problem link - https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/0
# Solution - https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2


class Solution:
    @staticmethod
    def get_max_points(arr, k):
        """
            Time complexity is O(k) and space complexity is O(1).
        """

        n = len(arr)

        # if the k value is out of scope, return -1
        if k not in range(1, n + 1):
            return -1

        # else initialize i and j
        i, j = k - 1, n

        # initialize sums
        max_sum, t = sum(arr[:k]), sum(arr[:k])

        # while cards from front can be picked.
        while i >= 0:
            # remove the ith card
            t -= arr[i]

            # add the jth card
            t += arr[j - 1]

            # update the max points obtained.
            if max_sum < t:
                max_sum = t
            i -= 1
            j -= 1

        # return the max points obtained.
        return max_sum


print(Solution.get_max_points([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.get_max_points([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.get_max_points([2, 2, 2], 2))
print(Solution.get_max_points([8, 6, 2, 4, 5], 5))
