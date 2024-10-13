def recursive():
    def solve(arr, i, target):
        # Time complexity is O(2^n) and space complexity is O(n)

        if target == 0:
            return True
        if i == 0:
            return arr[0] == target

        left = False
        if target >= arr[i]:
            left = solve(arr, i - 1, target - arr[i])
        right = solve(arr, i - 1, target)
        return left or right

    def subset_sum(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


recursive()