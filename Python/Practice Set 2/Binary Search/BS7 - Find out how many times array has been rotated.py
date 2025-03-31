# Problem link - https://www.naukri.com/code360/problems/rotation_7449070
# Solution - https://www.youtube.com/watch?v=jtSiWTPLwd0&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=8


class Solution:
    @staticmethod
    def get_num_rotations(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # define search space
        low = 0
        high = len(arr) - 1

        # define ans and index for storing min value and the index of the min value as that will be the number of
        # rotations done in the array.
        ans = 1e6
        index = None

        while low <= high:
            mid = int(low + (high - low)/2)

            # if all the indices are same, shrink the search space.
            if arr[low] == arr[mid] == arr[high]:
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                low += 1
                high -= 1
                continue

            # if left part is sorted
            if arr[low] <= arr[mid]:
                # and low element is < ans, update ans and set index = low.
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                # move to right half.
                low = mid + 1
            else:
                # if right part is sorted and mid-element is < ans, update ans and set index = mid.
                if arr[mid] < ans:
                    ans = arr[mid]
                    index = mid
                # move to the left half.
                high = mid - 1

        # return the index of min value, which represents the number of rotations done.
        return index


print(Solution.get_num_rotations([3, 4, 5, 1, 2]))
print(Solution.get_num_rotations([1, 2, 4, 5, 7]))
print(Solution.get_num_rotations([3, 3, 3, 3, 2, 3, 3]))
print(Solution.get_num_rotations([1, 2, 3]))
print(Solution.get_num_rotations([2, 3, 4, 1]))
