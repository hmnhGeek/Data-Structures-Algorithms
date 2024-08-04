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


def tabulation():
    def loot_max(houses):
        # Time complexity is O(n) and space is O(n) for the 2D dp array.

        n = len(houses)

        # initialize a 2D DP array where each index has two keys: pick or not pick.
        # both initialized as 0.
        dp = {i: {False: 0, True: 0} for i in range(n)}

        # Base cases (refer recursion)
        dp[0][True] = houses[0]
        dp[0][False] = 0

        # start in the opposite direction of the memoized solution.
        for index in range(1, n):
            # if index needs to be looted, add its profit and get the max profit by skipping the adjacent house on
            # the left and check if the profit is max by considering the new house or by not considering it. Add that
            # profit here.

            # if index <= 1, then in True case it is certain to pick money from this house, but, in this case,
            # index can be 0 (which is handled in base case), or index can be 1, in which case, index 0 won't be
            # considered. In both the cases, since we are building from bottom to top, an addition of 0 will be done.
            dp[index][True] = houses[index] + 0

            # let's update max money that can be added but only for houses post index 1.
            if index > 1:
                dp[index][True] = houses[index] + max(dp[index - 2][True], dp[index - 2][False])

            # if index needs not to be looted, add no profit and get the max profit by considering the adjacent house or
            # by not considering it. Add that profit here to 0.
            dp[index][False] = 0 + max(dp[index - 1][True], dp[index - 1][False])

        # return the max profit that can be made by considering the last house or by not considering it.
        return max(dp[n - 1][True], dp[n - 1][False])

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


def space_optimized():
    def loot_max(houses):
        # Time complexity is O(n) and space is O(1) for constant space for prev & prev2 used.

        n = len(houses)

        # initialize prev and prev2 denoting money that can be looted for 0th house and -1st house (imaginary),
        # respectively. These are basically the base cases.
        prev2 = {False: 0, True: 0}
        prev = {False: 0, True: houses[0]}

        # start in the opposite direction of the memoized solution.
        for index in range(1, n):
            # if index = 1, then in True case it is certain to pick money from this house, but, in this case,
            # prev index can be 0 (which is handled in base case) and hence nothing needs to be added. For
            # index > 1, max money can be updated.
            curr = {False: 0, True: houses[index]}

            # if index needs to be looted, add its profit and get the max profit by skipping the adjacent house on
            # the left and check if the profit is max by considering the new house or by not considering it. Add that
            # profit here.
            if index > 1:
                curr[True] = houses[index] + max(prev2[True], prev2[False])

            # if index needs not to be looted, add no profit and get the max profit by considering the adjacent house or
            # by not considering it. Add that profit here to 0.
            curr[False] = 0 + max(prev[True], prev[False])

            # update previous variables.
            prev2 = prev
            prev = curr

        # return the max profit that can be made by considering the last house (in prev) or by not considering it.
        return max(prev.values())

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


print("Recursive Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()