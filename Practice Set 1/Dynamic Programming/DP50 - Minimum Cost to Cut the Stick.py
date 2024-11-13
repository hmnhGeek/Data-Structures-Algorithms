def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(rod, i, j):
        if i > j:
            return 0
        min_cost = 1e6
        for k in range(i, j + 1):
            cost = rod[j + 1] - rod[i - 1] + solve(rod, i, k - 1) + solve(rod, k + 1, j)
            min_cost = min(min_cost, cost)
        return min_cost

    def get_min_cost_to_cut(cut_coordinates, length_of_rod):
        cut_coordinates.sort()
        rod = [0,] + cut_coordinates + [length_of_rod,]
        return solve(rod, 1, len(cut_coordinates))

    print(get_min_cost_to_cut([1, 3, 4, 5], 7))
    print(get_min_cost_to_cut([1, 3], 4))
    print(get_min_cost_to_cut([1, 3, 4], 5))
    print(get_min_cost_to_cut([1, 3, 4, 7], 10))
    print(get_min_cost_to_cut([1, 3], 10))


def memoized():
    """
        Time complexity is O(n^3) and space complexity is O(n + n^2), where n is the length of the cuts array.
    """

    def solve(rod, i, j, dp):
        if i > j:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]
        min_cost = 1e6
        # will take additional n iterations.
        for k in range(i, j + 1):
            cost = rod[j + 1] - rod[i - 1] + solve(rod, i, k - 1, dp) + solve(rod, k + 1, j, dp)
            min_cost = min(min_cost, cost)
        dp[i][j] = min_cost
        return min_cost

    def get_min_cost_to_cut(cut_coordinates, length_of_rod):
        cut_coordinates.sort()
        rod = [0,] + cut_coordinates + [length_of_rod,]
        dp = {i: {j: None for j in range(len(rod))} for i in range(len(rod))}
        return solve(rod, 1, len(cut_coordinates), dp)

    print(get_min_cost_to_cut([1, 3, 4, 5], 7))
    print(get_min_cost_to_cut([1, 3], 4))
    print(get_min_cost_to_cut([1, 3, 4], 5))
    print(get_min_cost_to_cut([1, 3, 4, 7], 10))
    print(get_min_cost_to_cut([1, 3], 10))


def tabulation():
    """
        Time complexity is O(n^3) and space complexity is O(n^2), where n is the length of the cuts array.
    """
    def get_min_cost_to_cut(cut_coordinates, length_of_rod):
        cut_coordinates.sort()
        rod = [0,] + cut_coordinates + [length_of_rod,]
        dp = {i: {j: 0 for j in range(len(cut_coordinates) + 2)} for i in range(len(cut_coordinates) + 2)}

        for i in range(len(cut_coordinates), 0, -1):
            for j in range(i, len(cut_coordinates) + 1):
                min_cost = 1e6
                # will take additional n iterations.
                for k in range(i, j + 1):
                    cost = rod[j + 1] - rod[i - 1] + dp[i][k - 1] + dp[k + 1][j]
                    min_cost = min(min_cost, cost)
                dp[i][j] = min_cost

        return dp[1][len(cut_coordinates)]

    print(get_min_cost_to_cut([1, 3, 4, 5], 7))
    print(get_min_cost_to_cut([1, 3], 4))
    print(get_min_cost_to_cut([1, 3, 4], 5))
    print(get_min_cost_to_cut([1, 3, 4, 7], 10))
    print(get_min_cost_to_cut([1, 3], 10))


recursive()
print()
memoized()
print()
tabulation()