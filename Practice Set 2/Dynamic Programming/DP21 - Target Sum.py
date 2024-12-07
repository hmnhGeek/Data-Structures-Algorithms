def recursive():
    """
        T: O(2^n) and S: O(n)
    """

    def solve(arr, index, target):
        if target == 0:
            return 1
        if index == 0:
            return 1 if arr[0] == target else 0

        left = 0
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index])
        right = solve(arr, index - 1, target)
        return left + right

    def target_sum(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(target_sum([1, 2, 3, 1], 3))


recursive()