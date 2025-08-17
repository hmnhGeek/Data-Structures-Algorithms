# Problem link - https://www.geeksforgeeks.org/dsa/in-place-merge-sort/


class Solution:
    @staticmethod
    def sort(arr):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """
        low = 0
        high = len(arr) - 1
        Solution._sort(arr, low, high)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low) / 2)
        Solution._sort(arr, low, mid)
        Solution._sort(arr, mid + 1, high)
        arr[low:high + 1] = Solution._merge(arr, low, high)

    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low) / 2)
        left, right = arr[low:mid + 1], arr[mid + 1:high + 1]
        i, j = 0, 0
        merged = []

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


if __name__ == '__main__':
    a1 = [2, 3, 4, 1]
    Solution.sort(a1)
    print(a1)

    a2 = [56, 2, 45]
    Solution.sort(a2)
    print(a2)

    a3 = [2, 1, 8, 6, 4, 3, 2, 9]
    Solution.sort(a3)
    print(a3)
