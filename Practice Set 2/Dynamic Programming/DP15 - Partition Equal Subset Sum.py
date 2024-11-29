def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, index, k):
        if k == 0:
            return True
        if index == 0:
            return arr[index] == k

        left = False
        if arr[index] <= k:
            left = solve(arr, index - 1, k - arr[index])
        right = solve(arr, index - 1, k)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(subset_sum([2, 3, 3, 3, 4, 5], 10))


recursive()