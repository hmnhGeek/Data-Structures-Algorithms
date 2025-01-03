def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, index):
        if index < 0:
            return 0
        take = arr[index] + solve(arr, index - 2)
        not_take = solve(arr, index - 1)
        return max(take, not_take)

    def house_robber(arr):
        n = len(arr)
        return solve(arr, n - 1)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


recursive()