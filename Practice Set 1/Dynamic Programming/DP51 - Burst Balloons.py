def recursive():
    def solve(points, i, j):
        if i > j:
            return 0

        maxi = 0
        for k in range(i, j + 1):
            earnings = points[i - 1] * points[k] * points[j + 1] + solve(points, i, k - 1) + solve(points, k + 1, j)
            maxi = max(maxi, earnings)
        return maxi

    def burst_balloons(arr):
        points = [1] + arr + [1]
        return solve(points, 1, len(arr))

    print(burst_balloons([3, 1, 5, 8]))
    print(burst_balloons([7, 1, 8]))
    print(burst_balloons([9, 1]))
    print(burst_balloons([1, 2, 3, 4, 5]))
    print(burst_balloons([1, 5, 2, 8]))


recursive()