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


recursive()