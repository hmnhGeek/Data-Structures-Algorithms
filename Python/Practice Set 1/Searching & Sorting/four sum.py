class MergeSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        return MergeSort._sort(arr, 0, n - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        MergeSort._sort(arr, low, mid)
        MergeSort._sort(arr, mid + 1, high)
        arr[low:high+1] = MergeSort._merge(arr, low, high)

    @staticmethod
    def _merge(arr, low, high):
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
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged


class Solution:
    @staticmethod
    def four_sum(arr, target):
        MergeSort.sort(arr)
        i = 0
        n = len(arr)
        result = []
        for i in range(n):
            if i != 0 and arr[i - 1] == arr[i]:
                continue
            for j in range(i + 1, n):
                if j != i + 1 and arr[j - 1] == arr[j]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    _sum = arr[i] + arr[j] + arr[k] + arr[l]
                    if _sum == target:
                        result.append((arr[i], arr[j], arr[k], arr[l]))
                        k += 1
                        l -= 1
                    elif _sum < target:
                        k += 1
                    else:
                        l -= 1
        return result


print(Solution.four_sum([2, 2, 2, 2, 1, 3], 8))
print(Solution.four_sum([1, 1, 1, 0], 4))
print(Solution.four_sum([1, 0, -1, 0, -2, 2], 0))
print(Solution.four_sum([2, 2, 2, 2, 2], 8))