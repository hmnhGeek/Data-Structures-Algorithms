# Problem Link - https://www.naukri.com/code360/problems/rotation_7449070
# Solution - https://www.youtube.com/watch?v=jtSiWTPLwd0&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=8


"""
    The index of min value in the rotated sorted array represents the number of times the sorted array was rotated.
    Time complexity is O(log(n)) and space complexity is O(1).
"""


class Solution:
    @staticmethod
    def num_rotations(arr):
        n = len(arr)
        low, high = 0, n - 1
        min_val = 1e6
        ans = None
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] <= arr[mid] <= arr[high]:
                return low
            if arr[low] <= arr[mid]:
                if min_val > arr[low]:
                    min_val = arr[low]
                    ans = low
                low = mid + 1
            else:
                if min_val > arr[mid]:
                    min_val = arr[mid]
                    ans = mid
                high = mid - 1
        return ans


print(Solution.num_rotations([3, 4, 5, 1, 2]))
print(Solution.num_rotations([1, 2, 3, 4, 5]))
print(Solution.num_rotations([2, 3, 4, 1]))