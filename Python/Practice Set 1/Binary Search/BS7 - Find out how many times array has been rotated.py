# Problem link - https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
# Solution - https://www.youtube.com/watch?v=jtSiWTPLwd0&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=8


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
            # if the entire array is sorted, just update ans and index and return
            if arr[low] <= arr[high]:
                # compare with low because low will hold the minimum in sorted array.
                if ans > arr[low]:
                    ans = arr[low]
                    index = low
                    break
            if arr[low] <= arr[mid]:
                # if left half is sorted, update and ans and index wrt low.
                if ans > arr[low]:
                    ans = arr[low]
                    index = low
                low = mid + 1
            else:
                # update ans and index wrt mid as arr[mid] <= arr[high] if right part is sorted.
                if ans > arr[mid]:
                    ans = arr[mid]
                    index = mid
                high = mid - 1
        # return the index of the minimum value as this will denote the number of times an array is rotated.
        return index


print(Solution.num_rotations([7, 8, 1, 2, 3, 4, 5, 6]))
print(Solution.num_rotations([3, 4, 5, 1, 2]))
print(Solution.num_rotations([2, 3, 4, 1]))
print(Solution.num_rotations([1, 2, 3]))
print(Solution.num_rotations([15, 18, 2, 3, 6, 12]))
print(Solution.num_rotations([7, 9, 11, 12, 5]))
print(Solution.num_rotations([7, 9, 11, 12, 15]))