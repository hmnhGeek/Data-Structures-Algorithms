def recursive():
    def solve(arr, index, pick):
        # T: O(2^n) and S: O(n)
        if index < 0:
            return 0
        if index == 0:
            if pick:
                return arr[0]
            else:
                return 0

        if pick:
            return arr[index] + max(
                solve(arr, index - 2, True),
                solve(arr, index - 2, False)
            )
        else:
            return max(
                solve(arr, index - 1, True),
                solve(arr, index - 1, False)
            )

    def house_robber(arr):
        n = len(arr)
        return max(
            solve(arr, n - 1, True),
            solve(arr, n - 1, False)
        )

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))


def memoized():
    def solve(arr, index, pick, dp):
        # T: O(2^n) and S: O(n)
        if index < 0:
            return 0
        if index == 0:
            if pick:
                return arr[0]
            else:
                return 0

        if dp[index][pick] is not None:
            return dp[index][pick]

        if pick:
            dp[index][pick] = arr[index] + max(
                solve(arr, index - 2, True, dp),
                solve(arr, index - 2, False, dp)
            )
        else:
            dp[index][pick] = max(
                solve(arr, index - 1, True, dp),
                solve(arr, index - 1, False, dp)
            )
        return dp[index][pick]

    def house_robber(arr):
        n = len(arr)
        dp = {i: {True: None, False: None} for i in range(n)}
        return max(
            solve(arr, n - 1, True, dp),
            solve(arr, n - 1, False, dp)
        )

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))


recursive()
print()
memoized()