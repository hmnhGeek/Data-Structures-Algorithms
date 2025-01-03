def recursive():
    """
        Time complexity is O(k^n) and space complexity is O(n).
    """

    def solve(arr, index, k):
        if index == 0:
            return 0
        min_cost = 1e6
        for i in range(1, k + 1):
            cost = 1e6
            if index - i >= 0:
                cost = abs(arr[index] - arr[index - i]) + solve(arr, index - i, k)
            min_cost = min(min_cost, cost)
        return min_cost

    def frog_jump(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(frog_jump([10, 30, 50, 60, 20, 10], 3))
    print(frog_jump([10, 30, 50, 60, 20, 10], 2))
    print(frog_jump([10, 30, 50, 60, 20, 10], 4))
    print(frog_jump([10, 30, 50, 60, 20, 10], 1))
    print(frog_jump([10, 30, 40, 50, 20], 3))
    print(frog_jump([10, 20, 10], 1))
    print(frog_jump([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))


recursive()