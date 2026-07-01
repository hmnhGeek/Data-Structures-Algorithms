def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def house_robber(arr):
        n = len(arr)
        return solve(arr, n - 1)

    def solve(arr, i):
        if i == -2 or i == -1:
            return 0
        take = arr[i] + solve(arr, i - 2)
        not_take = solve(arr, i - 1)
        return max(take, not_take)

    print(house_robber([6, 5, 5, 7, 4]))
    print(house_robber([1, 5, 3]))
    print(house_robber([4, 4, 4, 4]))
    print(house_robber([6, 7, 1, 3, 8, 2, 4]))
    print(house_robber([5, 3, 4, 11, 2]))


recursive()
print()
