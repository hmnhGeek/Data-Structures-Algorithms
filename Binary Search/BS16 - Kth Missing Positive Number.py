class Solution:
    @staticmethod
    def find_missing(arr, k):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            diff = arr[mid] - 1 - mid
            if diff < k:
                low = mid + 1
            else:
                high = mid - 1
        return k + low


print(Solution.find_missing([2, 3, 4, 7, 11], 5))
print(Solution.find_missing([5, 7, 10, 12], 4))
print(Solution.find_missing([2, 4, 5, 7], 3))
print(Solution.find_missing([4, 7, 9, 10], 1))
print(Solution.find_missing([4, 7, 9, 10], 4))
print(Solution.find_missing([1, 2, 3, 4], 2))
print(Solution.find_missing([2, 3, 5, 9, 10], 1))
print(Solution.find_missing([1, 2, 3], 2))
print(Solution.find_missing([2, 3, 5, 9, 10, 11, 12], 4))
