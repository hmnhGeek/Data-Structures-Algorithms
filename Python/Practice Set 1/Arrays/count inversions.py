# Problem link - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
# Solution - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1


class InversionCounter:
    def __init__(self, count):
        self.count = count


class Solution:
    @staticmethod
    def count_inversions(arr):
        """
            Time complexity is O(nlog(n)) and space complexity is O(n).
        """
        inversion_counter = InversionCounter(0)
        Solution._sort(arr, 0, len(arr) - 1, inversion_counter)
        return inversion_counter.count

    @staticmethod
    def _sort(arr, low, high, inversion_counter):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        Solution._sort(arr, low, mid, inversion_counter)
        Solution._sort(arr, mid + 1, high, inversion_counter)
        arr[low:high + 1] = Solution._merge(arr, low, high, inversion_counter)

    @staticmethod
    def _merge(arr, low, high, inversion_counter):
        i, j = 0, 0
        mid = int(low + (high - low)/2)
        left, right = arr[low:mid+1], arr[mid+1:high+1]
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversion_counter.count += (len(left) - i)
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged


print(Solution.count_inversions([5, 4, 3, 2, 1]))
print(Solution.count_inversions([5, 3, 2, 4, 1]))
print(Solution.count_inversions([4, 3, 2, 1]))
print(Solution.count_inversions([10, 10, 10]))
print(Solution.count_inversions([2, 3, 4, 5, 6]))
print(Solution.count_inversions([2, 4, 1, 3, 5]))