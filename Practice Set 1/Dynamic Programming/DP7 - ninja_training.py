# Problem link - https://www.naukri.com/code360/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=AE39gJYuRog&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=8


def recursive():
    def solve(arr, day_index, activity_index, num_activities):
        if day_index == 0:
            return arr[0][activity_index]
        max_pts = 0
        for next_activity_index in range(num_activities):
            if next_activity_index != activity_index:
                max_pts = max(max_pts, solve(arr, day_index - 1, next_activity_index, num_activities))
        return arr[day_index][activity_index] + max_pts

    def ninja_training(mtx):
        """
            Overall time complexity is O(m*2^n) and space complexity is O(n).
        """

        # let num_activities = m and num_days = n
        num_days = len(mtx)
        num_activities = len(mtx[0])
        max_pts = 0
        # This will run for m times
        for activity_index in range(num_activities):
            # This function will have space complexity of O(2^n)
            max_pts = max(max_pts, solve(mtx, num_days - 1, activity_index, num_activities))
        return max_pts

    print(
        ninja_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninja_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninja_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )

    print(
        ninja_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )


def memoized():
    def solve(arr, day_index, activity_index, num_activities, dp):
        if day_index == 0:
            return arr[0][activity_index]
        if dp[day_index][activity_index] is not None:
            return dp[day_index][activity_index]
        max_pts = 0
        for next_activity_index in range(num_activities):
            if next_activity_index != activity_index:
                max_pts = max(max_pts, solve(arr, day_index - 1, next_activity_index, num_activities, dp))
        dp[day_index][activity_index] = arr[day_index][activity_index] + max_pts
        return dp[day_index][activity_index]

    def ninja_training(mtx):
        """
            Overall time complexity is O(m*n) and space complexity is O(n*m + n).
        """

        # let num_activities = m and num_days = n
        num_days = len(mtx)
        num_activities = len(mtx[0])
        max_pts = 0
        dp = {i: {j: None for j in range(num_activities)} for i in range(num_days)}
        # This will run for m times
        for activity_index in range(num_activities):
            max_pts = max(max_pts, solve(mtx, num_days - 1, activity_index, num_activities, dp))
        return max_pts

    print(
        ninja_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninja_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninja_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )

    print(
        ninja_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )


def tabulation():
    def ninja_training(mtx):
        """
            Overall time complexity is O(nm^2) and space complexity is O(n*m).
        """

        # let num_activities = m and num_days = n
        num_days = len(mtx)
        num_activities = len(mtx[0])
        max_pts = 0
        dp = {i: {j: 0 for j in range(num_activities)} for i in range(num_days)}
        for j in dp[0]:
            dp[0][j] = mtx[0][j]

        # This will run for m times
        for activity_index in range(num_activities):
            # This will run for n times.
            for day_index in range(1, num_days):
                sub_max_pts = 0
                # This will run for m times.
                for next_activity_index in range(num_activities):
                    if next_activity_index != activity_index:
                        sub_max_pts = max(sub_max_pts, dp[day_index - 1][next_activity_index])
                dp[day_index][activity_index] = mtx[day_index][activity_index] + sub_max_pts
            max_pts = max(max_pts, dp[num_days - 1][activity_index])
        return max_pts

    print(
        ninja_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninja_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninja_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )

    print(
        ninja_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )


def space_optimized():
    def ninja_training(mtx):
        """
            Overall time complexity is O(nm^2) and space complexity is O(m).
        """

        # let num_activities = m and num_days = n
        num_days = len(mtx)
        num_activities = len(mtx[0])
        prev = {j: 0 for j in range(num_activities)}
        for j in prev:
            prev[j] = mtx[0][j]

        for day_index in range(1, num_days):
            curr = {j: 0 for j in range(num_activities)}
            for activity_index in range(num_activities):
                sub_max_pts = 0
                # This will run for m times.
                for next_activity_index in range(num_activities):
                    if next_activity_index != activity_index:
                        sub_max_pts = max(sub_max_pts, prev[next_activity_index])
                curr[activity_index] = mtx[day_index][activity_index] + sub_max_pts
            prev = curr

        return max(prev.values())

    print(
        ninja_training(
            [
                [10, 40, 70],
                [20, 50, 80],
                [30, 60, 90]
            ]
        )
    )

    print(
        ninja_training(
            [
                [1, 2, 5],
                [3, 1, 1],
                [3, 3, 3]
            ]
        )
    )

    print(
        ninja_training(
            [
                [18, 11, 19],
                [4, 13, 7],
                [1, 8, 13]
            ]
        )
    )

    print(
        ninja_training(
            [
                [10, 50, 1],
                [5, 100, 11]
            ]
        )
    )


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()