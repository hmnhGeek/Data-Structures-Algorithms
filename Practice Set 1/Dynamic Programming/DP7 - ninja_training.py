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


recursive()