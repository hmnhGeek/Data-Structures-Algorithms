# Problem link - https://www.naukri.com/code360/problems/rotated-array_1093219
# Solution - https://www.youtube.com/watch?v=nhEMDKMB44g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=7


class Solution:
    @staticmethod
    def get_min(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # define the search space
        low, high = 0, len(arr) - 1

        # store final answer in a variable.
        ans = 1e6

        # binary search
        while low <= high:
            mid = int(low + (high - low)/2)

            # if there are duplicates, and you cannot decide where to move, then shrink the search space.
            if arr[low] == arr[mid] == arr[high]:
                ans = min(ans, arr[low])
                low += 1
                high -= 1
                continue

            # if the left half is sorted, then update `ans` with arr[low] because that will be the minimum in the sorted
            # part and then move to the right half.
            if arr[low] <= arr[mid]:
                ans = min(ans, arr[low])
                low = mid + 1
            else:
                # if the right part is sorted, update `ans` with arr[mid] because that would be the min in right half
                # and then move to the left half.
                ans = min(ans, arr[mid])
                high = mid - 1

        # finally, return the answer
        return ans


print(Solution.get_min([3, 4, 5, 1, 2]))
print(Solution.get_min([1, 2, 3, 4]))
print(Solution.get_min([25, 30, 5, 10, 15, 20]))
print(Solution.get_min([4, 5, 6, 7, 0, 1, 2]))
print(Solution.get_min([3, 3, 3, 3, 2, 3, 3]))
