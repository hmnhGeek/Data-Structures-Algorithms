# Problem link - https://www.naukri.com/code360/problems/rotation_7449070
# Solution - https://www.youtube.com/watch?v=jtSiWTPLwd0&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=8


class Solution:
    @staticmethod
    def get_min_in_rotated(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        n = len(arr)
        low = 0
        high = n - 1
        ans = 1e6
        result = None
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] <= arr[mid]:
                if ans > arr[low]:
                    ans = arr[low]
                    result = low
                low = mid + 1
            else:
                if ans > arr[mid]:
                    ans = arr[mid]
                    result = mid
                high = mid - 1
        return result


print(Solution.get_min_in_rotated([4, 5, 6, 7, 0, 1, 2]))
print(Solution.get_min_in_rotated([4, 1, 2, 3]))
print(Solution.get_min_in_rotated([3, 4, 5, 1, 2]))
print(Solution.get_min_in_rotated([3, 4, 1, 2]))
print(Solution.get_min_in_rotated([25, 30, 5, 10, 15, 20]))
print(Solution.get_min_in_rotated([11, 13, 15, 17]))
print(Solution.get_min_in_rotated([7, 8, 1, 2, 3, 4, 5, 6]))
print(Solution.get_min_in_rotated([1, 2]))
print(Solution.get_min_in_rotated([2, 1]))
print(Solution.get_min_in_rotated([3, 3, 3, 3, 3]))
print(Solution.get_min_in_rotated([1, 2, 2, 3, 3, 3, 5]))
print(Solution.get_min_in_rotated([5, 5, 5, 5, 1, 2, 3, 3]))
