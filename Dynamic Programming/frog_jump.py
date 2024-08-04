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
        # The time complexity is O(2^n) with O(n) space complexity (max recursion stack depth)

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


memoized()