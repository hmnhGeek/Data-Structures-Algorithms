class Solution:
    @staticmethod
    def get_kth_missing(arr, k):
        if k <= 0:
            return
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            elem = arr[mid] - mid - 1
            if elem < k:
                low = mid + 1
            elif elem > k:
                high = mid - 1
            else:
                high = mid - 1
        return k + low


print(Solution.get_kth_missing([2, 3, 4, 7, 11], 3))
print(Solution.get_kth_missing([2, 4, 5, 7], 3))
print(Solution.get_kth_missing([4, 7, 9, 10], 1))
print(Solution.get_kth_missing([4, 7, 9, 10], 4))
print(Solution.get_kth_missing([2, 3, 4, 7, 11], 5))
print(Solution.get_kth_missing([1, 2, 3, 4], 2))
print(Solution.get_kth_missing([3, 5, 9, 10, 11, 12], 2))
print(Solution.get_kth_missing([1, 2, 3], 2))
print(Solution.get_kth_missing([1, 2, 3], 0))
