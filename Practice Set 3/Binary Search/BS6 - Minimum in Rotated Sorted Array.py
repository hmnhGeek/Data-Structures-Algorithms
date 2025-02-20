class Solution:
    @staticmethod
    def get_min(arr):
        # define the search space.
        low, high = 0, len(arr) - 1

        # hold the minimum value in `ans` variable.
        ans = 1e6

        # typical binary search
        while low <= high:
            mid = int(low + (high - low)/2)

            # if all the variables are same
            if arr[low] == arr[mid] == arr[high]:
                # update the minimum value and update the search space.
                ans = min(ans, arr[low])
                low += 1
                high -= 1
                continue

            # if the left part is sorted
            if arr[low] <= arr[mid]:
                # update the ans with minimum of low and ans.
                ans = min(ans, arr[low])
                low = mid + 1
            else:
                # update the ans with minimum of mid and ans.
                ans = min(ans, arr[mid])
                high = mid - 1

        # return the `ans` which now holds the minimum value.
        return ans


print(Solution.get_min([3, 4, 5, 1, 2]))
print(Solution.get_min([1, 2, 3, 4]))
print(Solution.get_min([25, 30, 5, 10, 15, 20]))
print(Solution.get_min([4, 5, 6, 7, 0, 1, 2]))
print(Solution.get_min([3, 3, 3, 3, 2, 3, 3]))
