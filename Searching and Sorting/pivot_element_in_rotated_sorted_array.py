# Problem link - https://medium.com/@utkarsh.gupta0311/finding-the-pivot-in-a-rotated-and-sorted-array-using-binary-search-in-c-fdac97e566ce
# Solution - https://www.youtube.com/watch?v=nhEMDKMB44g&t=778s


class Solution:
    @staticmethod
    def get_pivot(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        n = len(arr)
        low, high = 0, n - 1
        ans = 1e6
        while low <= high:
            mid = int(low + (high - low)/2)

            # if we can't decide where to move, shrink the search space from both ends. Remember to update ans.
            if arr[low] == arr[mid] == arr[high]:
                ans = min(ans, arr[low])
                low += 1
                high -= 1
                continue

            # if left half is sorted
            if arr[low] <= arr[mid]:
                # update `ans` by taking min of ans and arr[low] and move to mid + 1
                ans = min(ans, arr[low])
                low = mid + 1
            else:
                # update `ans` by taking min of ans and arr[mid] and move to mid - 1
                ans = min(ans, arr[mid])
                high = mid - 1

        # return `ans` which is the pivot element.
        return ans


print(Solution.get_pivot([4, 5, 6, 7, 0, 1, 2]))
print(Solution.get_pivot([3, 3, 3, 3, 3, 1, 3, 3]))
print(Solution.get_pivot([2, 3, 3, 3, 4, 5, 6, 6]))
print(Solution.get_pivot([5, 6, 7, 8, 9, 10, 1, 2, 3]))
print(Solution.get_pivot([3, 5, 1, 2]))
print(Solution.get_pivot([33, 42, 72, 99]))
print(Solution.get_pivot([6, 7, 8, 1, 2, 3, 4, 5]))
