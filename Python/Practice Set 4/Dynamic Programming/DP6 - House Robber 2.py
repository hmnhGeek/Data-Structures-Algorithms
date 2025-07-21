def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i):
        if i < 0:
            return 0
        if i == 0:
            return arr[0]
        left = arr[i] + solve(arr, i - 2)
        right = solve(arr, i - 1)
        return max(left, right)

    def house_robber(arr):
        n = len(arr)
        return solve(arr, n - 1)

    def house_robber2(arr):
        x = house_robber(arr[:-1])
        y = house_robber(arr[1:])
        return max(x, y)

    print(house_robber2([2, 3, 2]))
    print(house_robber2([1, 3, 2, 1]))
    print(house_robber2([1, 5, 1, 2, 6]))
    print(house_robber2([2, 3, 5]))
    print(house_robber2([1, 3, 2, 0]))


recursive()