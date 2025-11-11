def recursive():
    def subset_sum(arr, target):
        """
            Time complexity is exponential and space complexity is O(n).
        """
        n = len(arr)
        return solve(arr, n - 1, target)

    def solve(arr, i, j):
        if j == 0:
            return True
        if i == 0:
            return arr[0] == j
        left = False
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left or right

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


recursive()
