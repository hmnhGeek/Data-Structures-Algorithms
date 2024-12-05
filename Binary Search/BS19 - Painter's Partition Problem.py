# Problem link - https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557
# Solution - https://www.youtube.com/watch?v=thUd_WJn6wk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=20

"""
    For explanation, please refer to BS18 as the problem is exactly the same.
"""


class Solution:
    @staticmethod
    def _get_painters(arr, mid):
        painters_used = 1
        units = arr[0]
        for i in range(1, len(arr)):
            if arr[i] + units <= mid:
                units += arr[i]
            else:
                painters_used += 1
                units = arr[i]
        return painters_used

    @staticmethod
    def painter(arr, k):
        """
            Time complexity is O(n*log(sum(arr) - max(arr))) and space complexity is O(1).
        """

        if k > len(arr):
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            painters_used = Solution._get_painters(arr, mid)
            if painters_used <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.painter([2, 1, 5, 6, 2, 3], 2))
print(Solution.painter([10, 20, 30, 40], 2))
print(Solution.painter([48, 90], 2))
print(Solution.painter([5, 10, 30, 20, 15], 3))
print(Solution.painter([5, 5, 5, 5], 2))