# Problem link - https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1
# Solution - https://www.youtube.com/watch?v=30vDmZg5MZ8


class QuickSort:
    @staticmethod
    def _get_partition_index(arr, low, high):
        pivot = arr[low]
        i, j = low, high

        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    @staticmethod
    def _sort(arr, low, high):
        if low < high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._sort(arr, low, partition_index - 1)
            QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        return QuickSort._sort(arr, 0, len(arr) - 1)


class RecursiveSolution:
    @staticmethod
    def solve(arr, index, k, tracking_arr):
        # if you've exhausted the array, return the difference between max and min values.
        if index < 0:
            return max(tracking_arr) - min(tracking_arr)

        # assume that the left recursion returns inf
        left = 1e6
        # if decrementing by `k` still keeps the value positive, proceed with recursion
        if arr[index] - k >= 0:
            left = RecursiveSolution.solve(arr, index - 1, k, tracking_arr + [arr[index] - k])
        # perform right recursion by incrementing with `k`.
        right = RecursiveSolution.solve(arr, index - 1, k, tracking_arr + [arr[index] + k])
        # return the min value of both the recursions
        return min(left, right)

    @staticmethod
    def minimize_the_heights(arr, k):
        """
            Time complexity is O(2^n) and space complexity is O(n) for the recursion stack and tracking array.
        """

        n = len(arr)
        # keep a tracking array for back tracking
        tracking_arr = []
        return RecursiveSolution.solve(arr, n - 1, k, tracking_arr)


print("Using recursive approach")
print(RecursiveSolution.minimize_the_heights([1, 5, 8, 10], 2))
print(RecursiveSolution.minimize_the_heights([3, 9, 12, 16, 20], 3))
print(RecursiveSolution.minimize_the_heights([12, 6, 4, 15, 17, 10], 6))
print(RecursiveSolution.minimize_the_heights([12, 6, 4, 15, 17, 10], 3))


class EfficientSolution:
    @staticmethod
    def minimize_the_heights(arr, k):
        """
            Overall time complexity is O(nlog(n)) and space complexity is O(1).
        """

        # This will take O(nlog(n)) time.
        QuickSort.sort(arr)
        result = arr[-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k

        # This will take O(n) time.
        for i in range(len(arr) - 1):
            mini = min(smallest, arr[i + 1] - k)
            maxi = max(largest, arr[i] + k)
            if mini < 0:
                continue
            result = min(result, maxi - mini)
        return result


print("\nUsing efficient approach")
print(EfficientSolution.minimize_the_heights([1, 5, 8, 10], 2))
print(EfficientSolution.minimize_the_heights([3, 9, 12, 16, 20], 3))
print(EfficientSolution.minimize_the_heights([12, 6, 4, 15, 17, 10], 6))
print(EfficientSolution.minimize_the_heights([12, 6, 4, 15, 17, 10], 3))