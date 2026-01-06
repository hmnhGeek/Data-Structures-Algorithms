# Problem link - https://www.geeksforgeeks.org/problems/aggressive-cows/0
# Solution - https://www.youtube.com/watch?v=R_Mfw4ew-Vo&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=18


class MergeSort:
    @staticmethod
    def sort(arr):
        MergeSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low) / 2)
        left, right = arr[low:mid+1], arr[mid+1:high+1]
        merged = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        MergeSort._sort(arr, low, mid)
        MergeSort._sort(arr, mid + 1, high)
        arr[low:high+1] = MergeSort._merge(arr, low, high)


class Solution:
    @staticmethod
    def aggressive_cows(arr, k):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """
        if k <= 0:
            return
        n = len(arr)
        low, high = 0, max(arr) - min(arr)
        MergeSort.sort(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            placed_cows = Solution._get_placed_cows_count(arr, mid)
            if placed_cows < k:
                high = mid - 1
            else:
                low = mid + 1
        return high

    @staticmethod
    def _get_placed_cows_count(arr, mid):
        last_placed_at = 0
        cows_placed = 1
        i = 1
        while i < len(arr):
            if arr[i] - arr[last_placed_at] >= mid:
                last_placed_at = i
                cows_placed += 1
            i += 1
        return cows_placed


print(Solution.aggressive_cows([0, 3, 4, 7, 9, 10], 4))
print(Solution.aggressive_cows([1, 2, 3], 2))
print(Solution.aggressive_cows([4, 2, 1, 3, 6], 2))
print(Solution.aggressive_cows([1, 2, 4, 8, 9], 3))
print(Solution.aggressive_cows([10, 1, 2, 7, 5], 3))
print(Solution.aggressive_cows([2, 12, 11, 3, 26, 7], 5))
print(Solution.aggressive_cows([6, 7,  9, 11, 13, 15], 4))
