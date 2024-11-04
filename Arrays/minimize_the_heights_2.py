# Problem link - https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1


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


print(RecursiveSolution.minimize_the_heights([1, 5, 8, 10], 2))
print(RecursiveSolution.minimize_the_heights([3, 9, 12, 16, 20], 3))
print(RecursiveSolution.minimize_the_heights([12, 6, 4, 15, 17, 10], 6))
print(RecursiveSolution.minimize_the_heights([12, 6, 4, 15, 17, 10], 3))