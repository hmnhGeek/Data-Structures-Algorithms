# Problem link - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
# Solution - https://www.youtube.com/watch?v=AseUmwVNaoY&t=1034s


class Solution:
    @staticmethod
    def get_inversion_count(arr):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """
        count = [0]
        Solution._merge_sort(arr, 0, len(arr) - 1, count)
        return count[0]

    @staticmethod
    def _merge_sort(arr, low, high, count):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        Solution._merge_sort(arr, low, mid, count)
        Solution._merge_sort(arr, mid + 1, high, count)
        arr[low:high+1] = Solution._merge(arr, low, high, count)

    @staticmethod
    def _merge(arr, low, high, count):
        mid = int(low + (high - low)/2)
        left, right = arr[low:mid+1], arr[mid+1:high+1]
        i, j = 0, 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count[0] += (len(left) - i)
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged


print(Solution.get_inversion_count([2, 4, 1, 3, 5]))
print(Solution.get_inversion_count([2, 3, 4, 5, 6]))
print(Solution.get_inversion_count([10, 10, 10]))
print(Solution.get_inversion_count([5, 3, 2, 4, 1]))