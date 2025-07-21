def get_next_index(m, j):
    result = []
    for i in range(m):
        if i == j:
            continue
        result.append(i)
    return result


def recursive():
    """
        Time complexity is O(m^n) and space complexity is O(n).
    """
    def ninjas_training(mtx):
        num_days, num_activities = len(mtx), len(mtx[0])
        max_points_overall = -1e6
        for activity in range(num_activities):
            points_obtained = solve(mtx, num_days - 1, activity, num_activities)
            max_points_overall = max(max_points_overall, points_obtained)
        return max_points_overall

    def solve(mtx, i, j, num_activities):
        if i == 0:
            return mtx[0][j]
        next_possible_activities = get_next_index(num_activities, j)
        max_points = -1e6
        for next_activity in next_possible_activities:
            points_obtained = mtx[i][j] + solve(mtx, i - 1, next_activity, num_activities)
            max_points = max(max_points, points_obtained)
        return max_points

    print(
        ninjas_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )


def memoized():
    """
        Time complexity is O(mn) and space complexity is O(n + mn).
    """
    def ninjas_training(mtx):
        num_days, num_activities = len(mtx), len(mtx[0])
        max_points_overall = -1e6
        for activity in range(num_activities):
            dp = {i: {j: None for j in range(num_activities)} for i in range(num_days)}
            points_obtained = solve(mtx, num_days - 1, activity, num_activities, dp)
            max_points_overall = max(max_points_overall, points_obtained)
        return max_points_overall

    def solve(mtx, i, j, num_activities, dp):
        if i == 0:
            return mtx[0][j]
        if dp[i][j] is not None:
            return dp[i][j]
        next_possible_activities = get_next_index(num_activities, j)
        max_points = -1e6
        for next_activity in next_possible_activities:
            points_obtained = mtx[i][j] + solve(mtx, i - 1, next_activity, num_activities, dp)
            max_points = max(max_points, points_obtained)
        dp[i][j] = max_points
        return dp[i][j]

    print(
        ninjas_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )


def tabulation():
    """
        Time complexity is O(mn) and space complexity is O(mn).
    """
    def ninjas_training(mtx):
        num_days, num_activities = len(mtx), len(mtx[0])
        max_points_overall = -1e6
        for activity in range(num_activities):
            dp = {i: {j: -1e6 for j in range(num_activities)} for i in range(num_days)}
            for first_activity in range(num_activities):
                dp[0][first_activity] = mtx[0][first_activity]
            for day in range(1, num_days):
                for prev_day_activity in range(num_activities):
                    next_possible_activities = get_next_index(num_activities, prev_day_activity)
                    max_points = -1e6
                    for next_activity in next_possible_activities:
                        points_obtained = mtx[day][prev_day_activity] + dp[day - 1][next_activity]
                        max_points = max(max_points, points_obtained)
                    dp[day][prev_day_activity] = max_points
            points_obtained = dp[num_days - 1][activity]
            max_points_overall = max(max_points_overall, points_obtained)
        return max_points_overall

    print(
        ninjas_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninjas_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )


recursive()
print()
memoized()
print()
tabulation()