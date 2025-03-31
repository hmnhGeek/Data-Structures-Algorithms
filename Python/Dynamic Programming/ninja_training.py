def recursive():
    def get_available_activities(activity_index):
        if activity_index == 0:
            return 1, 2
        elif activity_index == 1:
            return 0, 2
        else:
            return 0, 1

    def solve_max_points_for_ninja(activities, index, activity_index):
        # if you've reached index 0, simply return the points for activity_index
        if index == 0:
            return activities[0][activity_index]

        # if you've used activity_index, find out which other two indices are available
        available_activity1, available_activity2 = get_available_activities(activity_index)

        # add the points from current activity with max of available activities
        return activities[index][activity_index] + max(
            solve_max_points_for_ninja(activities, index - 1, available_activity1),
            solve_max_points_for_ninja(activities, index - 1, available_activity2)
        )

    def max_ninja_points(ninja_activities):
        n = len(ninja_activities)

        # start with the last index and go down till index 0. From last index,
        # we can pick any of the 3 activities. Find the maximum points that can be
        # made out of those 3.
        return max(
            solve_max_points_for_ninja(ninja_activities, n - 1, 0),
            solve_max_points_for_ninja(ninja_activities, n - 1, 1),
            solve_max_points_for_ninja(ninja_activities, n - 1, 2)
        )

    print(max_ninja_points([
        [10, 50, 1],
        [5, 100, 11],
        [15, 30, 80]
    ]))
    print(max_ninja_points([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(max_ninja_points([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))
    print(max_ninja_points([[18, 11, 19], [4, 13, 7], [1, 8, 13]]))


def memoized():
    def get_available_activities(activity_index):
        if activity_index == 0:
            return 1, 2
        elif activity_index == 1:
            return 0, 2
        else:
            return 0, 1

    def solve_max_points_for_ninja(activities, index, activity_index, dp):
        # if you've reached index 0, simply return the points for activity_index
        if index == 0:
            return activities[0][activity_index]

        if dp[index][activity_index] != float('-inf'):
            return dp[index][activity_index]

        # if you've used activity_index, find out which other two indices are available
        available_activity1, available_activity2 = get_available_activities(activity_index)

        # add the points from current activity with max of available activities
        dp[index][activity_index] = activities[index][activity_index] + max(
            solve_max_points_for_ninja(activities, index - 1, available_activity1, dp),
            solve_max_points_for_ninja(activities, index - 1, available_activity2, dp)
        )

        return dp[index][activity_index]

    def max_ninja_points(ninja_activities):
        n = len(ninja_activities)
        dp = {i: {0: float('-inf'), 1: float('-inf'), 2: float('-inf')} for i in range(n)}

        # start with the last index and go down till index 0. From last index,
        # we can pick any of the 3 activities. Find the maximum points that can be
        # made out of those 3.
        dp[n - 1][0] = solve_max_points_for_ninja(ninja_activities, n - 1, 0, dp)
        dp[n - 1][1] = solve_max_points_for_ninja(ninja_activities, n - 1, 1, dp)
        dp[n - 1][2] = solve_max_points_for_ninja(ninja_activities, n - 1, 2, dp)
        return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])

    print(max_ninja_points([
        [10, 50, 1],
        [5, 100, 11],
        [15, 30, 80]
    ]))
    print(max_ninja_points([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(max_ninja_points([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))
    print(max_ninja_points([[18, 11, 19], [4, 13, 7], [1, 8, 13]]))


def tabulation():
    def get_available_activities(activity_index):
        if activity_index == 0:
            return 1, 2
        elif activity_index == 1:
            return 0, 2
        else:
            return 0, 1

    def max_ninja_points(activities):
        n = len(activities)
        num_of_activities = len(activities[0])
        dp = {i: {0: float('-inf'), 1: float('-inf'), 2: float('-inf')} for i in range(n)}

        # convert the base condition of the recursive solution to tabulized dp base condition
        # i.e., assign values to dp[0]
        dp[0][0] = activities[0][0]
        dp[0][1] = activities[0][1]
        dp[0][2] = activities[0][2]

        # tabulized solution starts from opposite direction of memoized solution
        # since dp[0] (acting as base condition) is already defined, start iterating from index = 1
        for index in range(1, n):
            for activity_index in range(num_of_activities):
                # if you've used activity_index, find out which other two indices are available
                available_activity1, available_activity2 = get_available_activities(activity_index)

                # add the points from current activity with max of available activities
                dp[index][activity_index] = activities[index][activity_index] + max(
                    dp[index - 1][available_activity1],
                    dp[index - 1][available_activity2]
                )

        # the answer is present at dp[last index]. However, we need to print maximum points.
        return max(dp[n-1].values())

    print(max_ninja_points([
        [10, 50, 1],
        [5, 100, 11],
        [15, 30, 80]
    ]))
    print(max_ninja_points([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(max_ninja_points([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))
    print(max_ninja_points([[18, 11, 19], [4, 13, 7], [1, 8, 13]]))


def space_optimized():
    def get_available_activities(activity_index):
        if activity_index == 0:
            return 1, 2
        elif activity_index == 1:
            return 0, 2
        else:
            return 0, 1

    def max_ninja_points(activities):
        n = len(activities)
        num_of_activities = len(activities[0])

        # prev stores the points from activities on a given day
        prev = [float('-inf')]*num_of_activities

        # initially, prev represents the 0th day
        prev[0] = activities[0][0]
        prev[1] = activities[0][1]
        prev[2] = activities[0][2]

        # tabulized solution starts from opposite direction of memoized solution
        # start iterating from index = 1
        for index in range(1, n):
            # for the current day (denoted by index), initialize another row called `current`
            current = [float('-inf')] * num_of_activities

            # for each activity on the current day
            for activity_index in range(num_of_activities):
                # if you've used activity_index, find out which other two indices are available
                available_activity1, available_activity2 = get_available_activities(activity_index)

                # add the points from current activity with max of available activities
                current[activity_index] = activities[index][activity_index] + max(
                    prev[available_activity1],
                    prev[available_activity2]
                )

            # update the prev to current
            prev = current

        # the answer is present in prev. However, it has points from all activities,
        # we must return only the maximum answer.
        return max(prev)

    print(max_ninja_points([
        [10, 50, 1],
        [5, 100, 11],
        [15, 30, 80]
    ]))
    print(max_ninja_points([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(max_ninja_points([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))
    print(max_ninja_points([[18, 11, 19], [4, 13, 7], [1, 8, 13]]))


print("Recursive Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulized Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()
