def search_conflicting_intervals(intervals, low, high, end_time):
    conflicting_intervals = []
    last_slot = low
    while low <= high:
        mid = int(low + (high - low) / 2)
        possible_interval = intervals[mid]
        if possible_interval[0] <= end_time:
            conflicting_intervals.extend(intervals[last_slot:mid+1])
            low = last_slot = mid + 1
        else:
            high = mid - 1
    return conflicting_intervals


def get_conflicting_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    conflicting_intervals = {}
    for idx in range(len(intervals)):
        current_interval = intervals[idx]
        conflicting_intervals[current_interval] = search_conflicting_intervals(intervals, idx + 1, len(intervals) - 1,
                                                                               current_interval[1])
    for i in conflicting_intervals:
        for j in conflicting_intervals[i]:
            print(i, j)


get_conflicting_intervals(
        [(1, 5), (3, 7), (2, 6), (10, 15), (5, 6), (4, 100)]
    )
