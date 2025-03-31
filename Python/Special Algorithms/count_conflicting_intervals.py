# Problem link - https://www.geeksforgeeks.org/given-n-appointments-find-conflicting-appointments/


def search_conflicting_intervals(intervals, low, high, end_time):
    conflicting_intervals = []
    last_slot = low
    while low <= high:
        mid = int(low + (high - low) / 2)
        possible_interval = intervals[mid]
        # if the start time of the mid-interval is less than or equal to the end time,
        # then there is an overlap and conflict
        if possible_interval[0] <= end_time:
            # add all the conflicting intervals
            conflicting_intervals.extend(intervals[last_slot:mid + 1])
            # set low and last slot to mid + 1
            low = last_slot = mid + 1
        else:
            high = mid - 1
    # return the conflicting intervals
    return conflicting_intervals


def get_conflicting_intervals(intervals):
    # sort the intervals based on starting time in O(n*log(n)) time.
    intervals.sort(key=lambda x: x[0])

    # create a blank dictionary to store the conflicting intervals.
    conflicting_intervals = {}

    # loop on all the intervals... this will also take O(n*log(n)).
    for idx in range(len(intervals)):
        current_interval = intervals[idx]
        # get all the conflicting intervals for this interval from idx +1 till end using binary search.
        conflicting_intervals[current_interval] = search_conflicting_intervals(intervals, idx + 1, len(intervals) - 1,
                                                                               current_interval[1])
    for i in conflicting_intervals:
        for j in conflicting_intervals[i]:
            print(i, j)


get_conflicting_intervals(
    [(1, 5), (3, 7), (2, 6), (10, 15), (5, 6), (4, 100)]
)
