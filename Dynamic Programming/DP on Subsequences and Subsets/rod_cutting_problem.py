def recursive():
    def solve_the_rod_cutting_problem(profits_per_cut, index, available_length_of_rod):
        # Since we are staying at the same index in case of "considering index", the time complexity is >= O(2^n) or
        # simply exponential and the space complexity O(available_length_of_rod)

        # if at any point, the available length of the rod becomes 0, return 0 as there is no profit that can be made
        if available_length_of_rod == 0:
            return 0

        # if you are at index 0, i.e., you can make 1 unit cuts, then, for available length of rod = N, you can make
        # N cuts of unit 1, isn't it? 1 unit costs profits_per_cut[0]. What would be the total cost? It would be
        # N * profits_per_cut[0], return this.
        if index == 0:
            return available_length_of_rod * profits_per_cut[0]

        # first assume that you cannot cut the rod into (index + 1) unit cuts. So you will get -inf profit. This will be
        # useful when you have to compare max profit.
        left_recursion = float('-inf')

        # However, if the cut length <= available rod length, then you can actually make index + 1 unit cuts
        if index + 1 <= available_length_of_rod:
            # add the profit by making one (index + 1) cut, and recurse on same index (as you can make multiple such
            # cuts) by decreasing the length of available rod by the cut length unit.
            left_recursion = profits_per_cut[index] + solve_the_rod_cutting_problem(profits_per_cut, index, available_length_of_rod - index - 1)

        # in the case when you decide not to cut the rod in (index + 1) unit cut, simply move to index - 1 with same
        # length of the rod.
        right_recursion = solve_the_rod_cutting_problem(profits_per_cut, index - 1, available_length_of_rod)

        # return the max profit obtained from both the approaches.
        return max(left_recursion, right_recursion)

    def rod_cutting_problem(length_of_rod, profits_per_cut):
        # store the length of the array of prices
        n = len(profits_per_cut)

        # since the indices of the prices array denotes cuts, and in question it is given that the max number of cuts
        # that are allowed is equal to the length of the rod, check the edge case where the length of cuts from the
        # prices array is more than the length of the rod.
        if n > length_of_rod:
            return -1

        # recursively solve the rod cutting problem
        return solve_the_rod_cutting_problem(profits_per_cut, n - 1, length_of_rod)

    print(
        rod_cutting_problem(
            5,
            [2, 5, 7, 8, 10]
        )
    )

    print(
        rod_cutting_problem(
            8,
            [3, 5, 8, 9, 10, 17, 17, 20]
        )
    )

    print(
        rod_cutting_problem(
            6,
            [3, 5, 6, 7, 10, 12]
        )
    )


def memoized():
    def solve_the_rod_cutting_problem(profits_per_cut, index, available_length_of_rod, dp):
        # Time complexity would be O(len(profits_per_cut) * length of full rod) and space complexity would be
        # O(len(profits_per_cut) * length of full rod + length of the full rod) (including the DP array). Also,
        # n = length of full rod = len(profits_per_cut). Hence T: O(N^2) and space would be O(N^2 + N)

        # if at any point, the available length of the rod becomes 0, return 0 as there is no profit that can be made
        if available_length_of_rod == 0:
            return 0

        # if you are at index 0, i.e., you can make 1 unit cuts, then, for available length of rod = N, you can make
        # N cuts of unit 1, isn't it? 1 unit costs profits_per_cut[0]. What would be the total cost? It would be
        # N * profits_per_cut[0], return this.
        if index == 0:
            return available_length_of_rod * profits_per_cut[0]

        if dp[index][available_length_of_rod] is not None:
            return dp[index][available_length_of_rod]

        # first assume that you cannot cut the rod into (index + 1) unit cuts. So you will get -inf profit. This will be
        # useful when you have to compare max profit.
        left_recursion = float('-inf')

        # However, if the cut length <= available rod length, then you can actually make index + 1 unit cuts
        if index + 1 <= available_length_of_rod:
            # add the profit by making one (index + 1) cut, and recurse on same index (as you can make multiple such
            # cuts) by decreasing the length of available rod by the cut length unit.
            left_recursion = profits_per_cut[index] + solve_the_rod_cutting_problem(profits_per_cut, index, available_length_of_rod - index - 1, dp)

        # in the case when you decide not to cut the rod in (index + 1) unit cut, simply move to index - 1 with same
        # length of the rod.
        right_recursion = solve_the_rod_cutting_problem(profits_per_cut, index - 1, available_length_of_rod, dp)

        # return the max profit obtained from both the approaches.
        dp[index][available_length_of_rod] = max(left_recursion, right_recursion)
        return dp[index][available_length_of_rod]

    def rod_cutting_problem(length_of_rod, profits_per_cut):
        # store the length of the array of prices
        n = len(profits_per_cut)

        # since the indices of the prices array denotes cuts, and in question it is given that the max number of cuts
        # that are allowed is equal to the length of the rod, check the edge case where the length of cuts from the
        # prices array is more than the length of the rod.
        if n > length_of_rod:
            return -1

        dp = {i: {j: None for j in range(length_of_rod + 1)} for i in range(n)}

        # recursively solve the rod cutting problem
        return solve_the_rod_cutting_problem(profits_per_cut, n - 1, length_of_rod, dp)

    print(
        rod_cutting_problem(
            5,
            [2, 5, 7, 8, 10]
        )
    )

    print(
        rod_cutting_problem(
            8,
            [3, 5, 8, 9, 10, 17, 17, 20]
        )
    )

    print(
        rod_cutting_problem(
            6,
            [3, 5, 6, 7, 10, 12]
        )
    )


memoized()