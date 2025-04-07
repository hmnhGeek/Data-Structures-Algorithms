class MergeSort:
    @staticmethod
    def sort(arr):
        MergeSort._sort(arr, 0, len(arr) - 1)

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


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, i, j):
        if i > j:
            return 0
        min_cost = 1e6
        for k in range(i, j + 1):
            cost = (arr[j + 1] - arr[i - 1]) + solve(arr, i, k - 1) + solve(arr, k + 1, j)
            min_cost = min(min_cost, cost)
        return min_cost

    def min_cost_to_cut_stick(cuts, length):
        n = len(cuts)
        rod = [0] + cuts + [length]
        MergeSort.sort(rod)
        return solve(rod, 1, n)

    print(min_cost_to_cut_stick([1, 3, 4, 5], 7))
    print(min_cost_to_cut_stick([1, 3], 4))
    print(min_cost_to_cut_stick([1, 3, 4], 5))
    print(min_cost_to_cut_stick([1, 3, 4, 7], 10))
    print(min_cost_to_cut_stick([1, 3], 10))
    print(min_cost_to_cut_stick([5, 6, 1, 4, 2], 9))


def memoized():
    """
        Time complexity is O(n^3) and space complexity is O(n + n^2).
    """

    def solve(arr, i, j, dp):
        if i > j:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        min_cost = 1e6
        for k in range(i, j + 1):
            cost = (arr[j + 1] - arr[i - 1]) + solve(arr, i, k - 1, dp) + solve(arr, k + 1, j, dp)
            min_cost = min(min_cost, cost)
        dp[i][j] = min_cost
        return dp[i][j]

    def min_cost_to_cut_stick(cuts, length):
        n = len(cuts)
        rod = [0] + cuts + [length]
        MergeSort.sort(rod)
        dp = {i: {j: None for j in range(1, n + 1)} for i in range(1, n + 1)}
        return solve(rod, 1, n, dp)

    print(min_cost_to_cut_stick([1, 3, 4, 5], 7))
    print(min_cost_to_cut_stick([1, 3], 4))
    print(min_cost_to_cut_stick([1, 3, 4], 5))
    print(min_cost_to_cut_stick([1, 3, 4, 7], 10))
    print(min_cost_to_cut_stick([1, 3], 10))
    print(min_cost_to_cut_stick([5, 6, 1, 4, 2], 9))


recursive()
print()
memoized()