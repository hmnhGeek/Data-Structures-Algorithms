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


recursive()
print()
memoized()