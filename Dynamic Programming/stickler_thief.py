def recursive():
    def solve(arr, index, pick):
        # Time complexity is O(2^n) and space is O(n) for the recursion stack.

        # if during going left, index becomes out of bound, return 0, no profit can be made where there is no house.
        if index < 0:
            return 0

        # if on the first house, and should be looted, return the profit at this house, else return no profit, i.e., 0.
        if index == 0:
            if pick:
                return arr[0]
            return 0

        # if index needs to be looted, add its profit and get the max profit by skipping the adjacent house on the left
        # and check if the profit is max by considering the new house or by not considering it. Add that profit here.
        if pick:
            return arr[index] + max(
                solve(arr, index - 2, True),
                solve(arr, index - 2, False)
            )
        else:
            # if index needs not to be looted, add no profit and get the max profit by considering the adjacent house or
            # by not considering it. Add that profit here to 0.
            return 0 + max(
                solve(arr, index - 1, True),
                solve(arr, index - 1, False)
            )

    def loot_max(houses):
        # Time complexity is O(2^n) and space is O(n) for the recursion stack.
        n = len(houses)
        # return the max profit that can be made by considering the last house or by not considering it.
        return max(solve(houses, n - 1, True), solve(houses, n - 1, False))

    print(
        loot_max([6, 5, 5, 7, 4])
    )

    print(
        loot_max([1, 5, 3])
    )

    print(
        loot_max([1, 2, 3, 1])
    )

    print(
        loot_max([2, 7, 9, 3, 1])
    )


def memoized():
    def solve(arr, index, pick, dp):
        # Time complexity is O(n) and space is O(n + n) for the recursion stack and 2D dp array.

        # if during going left, index becomes out of bound, return 0, no profit can be made where there is no house.
        if index < 0:
            return 0

        # if on the first house, and should be looted, return the profit at this house, else return no profit, i.e., 0.
        if index == 0:
            if pick:
                return arr[0]
            return 0

        if dp[index][pick] is not None:
            return dp[index][pick]

        # if index needs to be looted, add its profit and get the max profit by skipping the adjacent house on the left
        # and check if the profit is max by considering the new house or by not considering it. Add that profit here.
        if pick:
            dp[index][pick] = arr[index] + max(
                solve(arr, index - 2, True, dp),
                solve(arr, index - 2, False, dp)
            )
        else:
            # if index needs not to be looted, add no profit and get the max profit by considering the adjacent house or
            # by not considering it. Add that profit here to 0.
            dp[index][pick] = 0 + max(
                solve(arr, index - 1, True, dp),
                solve(arr, index - 1, False, dp)
            )

        return dp[index][pick]

    def loot_max(houses):
        # Time complexity is O(n) and space is O(n + n) for the recursion stack and 2D dp array.

        n = len(houses)

        # initialize a 2D DP array where each index has two keys: pick or not pick.
        dp = {i: {False: None, True: None} for i in range(n)}

        # return the max profit that can be made by considering the last house or by not considering it.
        return max(solve(houses, n - 1, True, dp), solve(houses, n - 1, False, dp))

    print(
        loot_max([6, 5, 5, 7, 4])
    )

    print(
        loot_max([1, 5, 3])
    )

    print(
        loot_max([1, 2, 3, 1])
    )

    print(
        loot_max([2, 7, 9, 3, 1])
    )


recursive()
memoized()