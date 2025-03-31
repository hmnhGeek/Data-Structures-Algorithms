# Problem link - https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557
# Solution - https://www.youtube.com/watch?v=thUd_WJn6wk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=20

"""
    For explanation, please refer to BS18 as the problem is exactly the same.
"""


class Solution:
    @staticmethod
    def _get_count(arr, mid):
        painters = 0
        time = 0
        for i in range(len(arr)):
            if arr[i] + time <= mid:
                time += arr[i]
            else:
                painters += 1
                time = arr[i]
        if time > 0:
            painters += 1
            time = 0
        return painters

    @staticmethod
    def painter_partition(arr, k):
        """
           Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        n = len(arr)
        if n < k:
            return -1
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            painters = Solution._get_count(arr, mid)
            if painters <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.painter_partition([10, 20, 30, 40], 2))
print(Solution.painter_partition([2, 1, 5, 6, 2, 3], 2))
print(Solution.painter_partition([48, 90], 2))
print(Solution.painter_partition([5, 10, 30, 20, 15], 3))
print(Solution.painter_partition([5]*4, 2))
