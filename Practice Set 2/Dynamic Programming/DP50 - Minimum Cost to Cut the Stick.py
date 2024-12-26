class MergeSort:
    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low) / 2)
        left, right = arr[low:mid + 1], arr[mid + 1:high + 1]
        i, j, merged = 0, 0, []

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
        mid = int(low + (high - low) / 2)
        MergeSort._sort(arr, low, mid)
        MergeSort._sort(arr, mid + 1, high)
        arr[low:high + 1] = MergeSort._merge(arr, low, high)

    @staticmethod
    def sort(arr):
        return MergeSort._sort(arr, 0, len(arr) - 1)


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, i, j):
        if i > j:
            return 0
        min_cost = 1e6
        for index in range(i, j + 1):
            cost = (arr[j + 1] - arr[i - 1]) + solve(arr, i, index - 1) + solve(arr, index + 1, j)
            min_cost = min(min_cost, cost)
        return min_cost

    def min_cost_to_cut_stick(arr, length):
        MergeSort.sort(arr)
        n = len(arr)
        arr = [0, ] + arr + [length, ]
        return solve(arr, 1, n)

    print(min_cost_to_cut_stick([1, 3, 4, 5], 7))
    print(min_cost_to_cut_stick([1, 3], 4))
    print(min_cost_to_cut_stick([1, 3, 4], 5))
    print(min_cost_to_cut_stick([1, 3, 4, 7], 10))
    print(min_cost_to_cut_stick([1, 3], 10))
    print(min_cost_to_cut_stick([5, 6, 1, 4, 2], 9))


recursive()
