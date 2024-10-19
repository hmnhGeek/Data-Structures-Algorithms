def recursive():
    def solve(arr, index, target):
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target

        left = False
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index])
        right = solve(arr, index - 1, target)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)