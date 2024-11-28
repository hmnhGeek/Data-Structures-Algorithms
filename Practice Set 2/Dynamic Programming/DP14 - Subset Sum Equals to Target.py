def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, i, k):
        if k == 0:
            return True
        if i == 0:
            return arr[0] == k

        left = False
        if arr[i] <= k:
            left = solve(arr, i - 1, k - arr[i])
        right = solve(arr, i - 1, k)
        return left or right

    def subset_sum(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


recursive()