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


recursive()