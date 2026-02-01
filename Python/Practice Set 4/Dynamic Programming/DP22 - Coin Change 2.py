def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def coin_change_2(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    def solve(arr, i, j):
        if j == 0:
            return 1
        if i == 0:
            if j % arr[0] == 0:
                return 1
            return 0
        left = 0
        if arr[i] <= j:
            left = solve(arr, i, j - arr[i])
        right = solve(arr, i - 1, j)
        return left + right

    print(coin_change_2([1, 2, 3], 4))
    print(coin_change_2([5, 3, 2], 1))
    print(coin_change_2([1, 2, 5], 5))
    print(coin_change_2([2], 3))
    print(coin_change_2([10], 10))
    print(coin_change_2([2, 5, 3, 6], 10))


recursive()
print()
