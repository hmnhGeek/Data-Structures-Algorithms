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

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))


def memoized():
    def solve(arr, index, target, dp):
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target

        if dp[index][target] is not None:
            return dp[index][target]

        left = False
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index], dp)
        right = solve(arr, index - 1, target, dp)
        dp[index][target] = left or right
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))


recursive()
print()
memoized()