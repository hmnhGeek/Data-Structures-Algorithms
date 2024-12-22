class Solution:
    @staticmethod
    def get_pivot(arr):
        n = len(arr)
        low, high = 0, n - 1
        ans = 1e6
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] == arr[mid] == arr[high]:
                ans = min(ans, arr[low])
                low += 1
                high -= 1
                continue
            if arr[low] <= arr[mid]:
                ans = min(ans, arr[low])
                low = mid + 1
            else:
                ans = min(ans, arr[mid])
                high = mid - 1
        return ans


print(Solution.get_pivot([4, 5, 6, 7, 0, 1, 2]))
print(Solution.get_pivot([3, 3, 3, 3, 3, 1, 3, 3]))
print(Solution.get_pivot([2, 3, 3, 3, 4, 5, 6, 6]))
print(Solution.get_pivot([5, 6, 7, 8, 9, 10, 1, 2, 3]))
print(Solution.get_pivot([3, 5, 1, 2]))
print(Solution.get_pivot([33, 42, 72, 99]))
print(Solution.get_pivot([6, 7, 8, 1, 2, 3, 4, 5]))