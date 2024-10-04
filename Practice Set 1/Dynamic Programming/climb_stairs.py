def recursive():
    # T: O(2^n) and space is O(n)
    def solve(index):
        if index < 0:
            return 0
        if index == 0:
            return 1
        return solve(index - 1) + solve(index - 2)

    def climb_stairs(num_stairs):
        return solve(num_stairs)

    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(4))
    print(climb_stairs(5))


def memoized():
    # T: O(n) and space is O(n + n)
    def solve(index, dp):
        if index < 0:
            return 0
        if index == 0:
            return 1

        if dp[index] is not None:
            return dp[index]

        dp[index] = solve(index - 1, dp) + solve(index - 2, dp)
        return dp[index]

    def climb_stairs(num_stairs):
        dp = {i: None for i in range(num_stairs + 1)}
        return solve(num_stairs, dp)

    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(4))
    print(climb_stairs(5))


def tabulation():
    # T: O(n) and space is O(n)
    def climb_stairs(num_stairs):
        dp = {i: 0 for i in range(num_stairs + 1)}
        dp[0] = 1

        for index in range(1, num_stairs + 1):
            if 0 <= index - 2 < num_stairs + 1:
                right = dp[index - 2]
            else:
                right = 0
            dp[index] = dp[index - 1] + right

        return dp[num_stairs]

    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(4))
    print(climb_stairs(5))


def space_optimized():
    # T: O(n) and space is O(1)
    def climb_stairs(num_stairs):
        prev_prev = 0
        prev = 1
        for index in range(1, num_stairs + 1):
            curr = 0
            if 0 <= index - 2 < num_stairs + 1:
                right = prev_prev
            else:
                right = 0
            curr = prev + right
            prev_prev = prev
            prev = curr

        return prev

    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(4))
    print(climb_stairs(5))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()