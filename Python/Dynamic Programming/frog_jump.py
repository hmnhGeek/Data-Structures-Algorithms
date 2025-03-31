# Problem link - https://www.naukri.com/code360/problems/frog-jump_3621012

def recursive():
    def solve(energies, index):
        # The time complexity is O(2^n) with O(n) space complexity (max recursion stack depth)

        # if the frog reached 1st stair (0th index), there is no more to go,
        # hence no energy differential is there, thus return 0 energy.
        if index == 0:
            return 0

        # solve for next lower stair and add |E_i - E_{i - 1}|
        one_step = solve(energies, index - 1) + abs(energies[index] - energies[index - 1])

        # assume that taking two steps will make you go out of bounds, so it would require
        # infinite energy
        two_steps = float('inf')

        # now, if taking two steps is possible, go two steps down and also add |E_i - E_{i - 2}|
        # energy while going down.
        if index > 1:
            two_steps = solve(energies, index - 2) + abs(energies[index] - energies[index - 2])

        # return the minimum energy that is consumed.
        return min(one_step, two_steps)

    def total_min_energy(energies):
        # start by placing the frog on the last index, i.e., top most stair.
        return solve(energies, len(energies) - 1)

    print(
        total_min_energy(
            [10, 20, 30, 10]
        )
    )

    print(
        total_min_energy(
            [10, 50, 10]
        )
    )

    print(
        total_min_energy(
            [7, 4, 4, 2, 6, 6, 3, 4]
        )
    )

    print(
        total_min_energy(
            [4, 8, 3, 10, 4, 4]
        )
    )


def memoized():
    def solve(energies, index, dp):
        # The time complexity is O(n) with O(n + n) space complexity,
        # with stack depth and dp array of length n.

        # if the frog reached 1st stair (0th index), there is no more to go,
        # hence no energy differential is there, thus return 0 energy.
        if index == 0:
            return 0

        if dp[index] is not None:
            return dp[index]

        # solve for next lower stair and add |E_i - E_{i - 1}|
        one_step = solve(energies, index - 1, dp) + abs(energies[index] - energies[index - 1])

        # assume that taking two steps will make you go out of bounds, so it would require
        # infinite energy
        two_steps = float('inf')

        # now, if taking two steps is possible, go two steps down and also add |E_i - E_{i - 2}|
        # energy while going down.
        if index > 1:
            two_steps = solve(energies, index - 2, dp) + abs(energies[index] - energies[index - 2])

        # return the minimum energy that is consumed.
        dp[index] = min(one_step, two_steps)
        return dp[index]

    def total_min_energy(energies):
        dp = {i: None for i in range(len(energies))}

        # start by placing the frog on the last index, i.e., top most stair.
        return solve(energies, len(energies) - 1, dp)

    print(
        total_min_energy(
            [10, 20, 30, 10]
        )
    )

    print(
        total_min_energy(
            [10, 50, 10]
        )
    )

    print(
        total_min_energy(
            [7, 4, 4, 2, 6, 6, 3, 4]
        )
    )

    print(
        total_min_energy(
            [4, 8, 3, 10, 4, 4]
        )
    )


def tabulation():
    def total_min_energy(energies):
        # Time complexity is O(n) and space complexity is O(n) with only dp array consuming space
        # and no recursion stack being used.

        # initialize dp array of size n with each stair having energy infinite.
        dp = {i: float('inf') for i in range(len(energies))}

        # initialize the base case, basically the energy required for the frog to jump
        # from 0th stair to 0th stair.
        dp[0] = 0

        # reverse the direction of memoization and start from index = 1.
        for index in range(1, len(energies)):
            # solve for previous lower stair and add |E_i - E_{i - 1}|
            one_step = dp[index - 1] + abs(energies[index] - energies[index - 1])

            # assume that taking two steps will make you go out of bounds, so it would require
            # infinite energy
            two_steps = float('inf')

            # now, if taking two steps is possible, go two steps previous and also add |E_i - E_{i - 2}|
            # energy while going down.
            if index > 1:
                two_steps = dp[index - 2] + abs(energies[index] - energies[index - 2])

            # update the minimum energy that is required to jump from index = `index` to index = 0.
            dp[index] = min(one_step, two_steps)

        # minimum energy would be stored at the last index in the dp dictionary.
        return dp[len(energies) - 1]

    print(
        total_min_energy(
            [10, 20, 30, 10]
        )
    )

    print(
        total_min_energy(
            [10, 50, 10]
        )
    )

    print(
        total_min_energy(
            [7, 4, 4, 2, 6, 6, 3, 4]
        )
    )

    print(
        total_min_energy(
            [4, 8, 3, 10, 4, 4]
        )
    )


def space_optimized():
    def total_min_energy(energies):
        # Time complexity is O(n) and space complexity is O(1) with only prev1 and prev2
        # being used for any problem.

        # initialize prev1 and prev2 such that prev1 denotes the energy taken from 0th to 0th
        # index and prev2 denotes the energy for -1st to 0th index which is infinity.
        prev1 = 0
        prev2 = float('inf')

        # reverse the direction of memoization and start from index = 1.
        for index in range(1, len(energies)):
            # solve for previous lower stair and add |E_i - E_{i - 1}|
            one_step = prev1 + abs(energies[index] - energies[index - 1])

            # assume that taking two steps will make you go out of bounds, so it would require
            # infinite energy
            two_steps = float('inf')

            # now, if taking two steps is possible, go two steps previous and also add |E_i - E_{i - 2}|
            # energy while going down.
            if index > 1:
                two_steps = prev2 + abs(energies[index] - energies[index - 2])

            # update the minimum energy that is required to jump from index = `index` to index = 0.
            curr = min(one_step, two_steps)

            # update the previous pointers
            prev2 = prev1
            prev1 = curr

        # return the energy stored in prev1 which denotes the minimum energy required to
        # jump from n - 1 index to 0th index.
        return prev1

    print(
        total_min_energy(
            [10, 20, 30, 10]
        )
    )

    print(
        total_min_energy(
            [10, 50, 10]
        )
    )

    print(
        total_min_energy(
            [7, 4, 4, 2, 6, 6, 3, 4]
        )
    )

    print(
        total_min_energy(
            [4, 8, 3, 10, 4, 4]
        )
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