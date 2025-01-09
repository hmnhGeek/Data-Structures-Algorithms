def recursive():
    def solve(arr, index):
        if index < 0:
            return 0
        left = arr[index] + solve(arr, index - 2)
        right = solve(arr, index - 1)
        return max(left, right)

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


def memoized():
    def solve(arr, index, dp):
        if index < 0:
            return 0
        if dp[index] is not None:
            return dp[index]
        left = arr[index] + solve(arr, index - 2, dp)
        right = solve(arr, index - 1, dp)
        dp[index] = max(left, right)
        return dp[index]

    def house_robber(arr):
        n = len(arr)
        dp = {i: None for i in range(-2, n)}
        return solve(arr, n - 1, dp)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def tabulation():
    def house_robber(arr):
        n = len(arr)
        dp = {i: 0 for i in range(-2, n)}
        for index in range(n):
            left = arr[index] + dp[index - 2]
            right = dp[index - 1]
            dp[index] = max(left, right)
        return dp[n - 1]

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def space_optimized():
    def house_robber(arr):
        n = len(arr)
        prev2 = prev = 0
        for index in range(n):
            left = arr[index] + prev2
            right = prev
            curr = max(left, right)
            prev2 = prev
            prev = curr
        return prev

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
