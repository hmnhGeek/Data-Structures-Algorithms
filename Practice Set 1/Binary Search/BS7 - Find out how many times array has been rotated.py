class Solution:
    @staticmethod
    def num_rotations(arr):
        """
            Use the code to find the minimum in a rotated sorted array to solve this problem.

            Time complexity is O(log(n)) and space complexity is O(1).
        """

        low, high = 0, len(arr) - 1
        ans, index = 1e6, -1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] <= arr[high]:
                if ans > arr[low]:
                    ans = arr[low]
                    index = low
                    break
            if arr[low] <= arr[mid]:
                if ans > arr[low]:
                    ans = arr[low]
                    index = low
                low = mid + 1
            else:
                if ans > arr[mid]:
                    ans = arr[mid]
                    index = mid
                high = mid - 1
        return index


print(Solution.num_rotations([7, 8, 1, 2, 3, 4, 5, 6]))
print(Solution.num_rotations([3, 4, 5, 1, 2]))
print(Solution.num_rotations([2, 3, 4, 1]))
print(Solution.num_rotations([1, 2, 3]))