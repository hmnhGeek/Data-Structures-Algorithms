# Problem link - https://www.naukri.com/code360/problems/merge-overlapping-intervals_1082151
# Solution - https://www.youtube.com/watch?v=IexN60k62jo&t=306s


from typing import List


class Interval:
    def __init__(self, start_time, end_time):
        self.start = start_time
        self.end = end_time

    def get_start_time(self):
        return self.start

    def get_end_time(self):
        return self.end

    def __str__(self):
        return f"({self.start}, {self.end})"


class MySolution:
    @staticmethod
    def _merge(intervals, interval, index):
        # define the search space.
        low = index
        high = len(intervals) - 1

        # start the binary search
        while low <= high:
            mid = int(low + (high - low) / 2)
            target_interval = intervals[mid]

            # if the overlap is possible, then we can search for intervals to the right. Who knows, we can get even
            # higher end time to maximize the range.
            if interval.get_end_time() >= target_interval.get_start_time():
                low = mid + 1
            else:
                # if the overlap is not possible, maybe we can decrease the search space to the left side as lower
                # intervals can have some overlap.
                high = mid - 1

        # at the end, `high` will point to a possible overlapping interval.
        return high

    @staticmethod
    def merge_intervals(intervals: List[Interval]):
        """
            Time complexity is O(n*log(n)) and space complexity is O(n) for the merged array in the worst case.
        """

        # This will take O(n*log(n)) time
        intervals.sort(key=lambda x: x.start)
        # store a merged array for the merged intervals.
        merged_intervals = []
        # start with current interval as 0th interval.
        interval = intervals[0]
        # start checking for overlapping intervals from 1st index till end.
        idx = 1

        # assuming that in the worst case it runs for about all the intervals, i.e., `n`, hence overall time complexity
        # of the while loop will be O(n*log(n)).
        while idx < len(intervals):
            # find the index of an interval which is overlapping with the interval `interval`. This will take O(log(n))
            # time due to a binary search operation.
            mid = MySolution._merge(intervals, interval, idx)

            # if the `mid` index is on the left side of the search space, you can't merge it as it was already merged
            # in some previous iterations. This means that the next interval to `mid` (a non-overlapping interval)
            # should be added to our merged intervals. Do that!
            if mid < idx and 0 <= mid + 1 < len(intervals):
                merged_intervals.append(intervals[mid + 1])
                # update the current interval `interval` to this non-overlapping interval for the next iteration.
                interval = intervals[mid + 1]
            else:
                # however, if a `mid` indexed interval is found which is overlapping with `interval`, then merge the
                # intervals into a merged_interval variable.
                target_interval = intervals[mid]
                merged_interval = Interval(
                    min(interval.get_start_time(), target_interval.get_start_time()),
                    max(interval.get_end_time(), target_interval.get_end_time())
                )
                # it is ensured that the last interval in the merged intervals is actually `interval`, which we have
                # just merged with the target interval. Hence, we do not need this last interval in the merged
                # intervals. So pop it.
                if len(merged_intervals) > 0:
                    merged_intervals.pop(-1)
                # append the merged interval into merged intervals list.
                merged_intervals.append(merged_interval)
                # and as you can see, we have updated current interval `interval` to the last interval from the merged
                # intervals.
                interval = merged_interval
            # finally, move `idx` to `mid + 1` because all the intervals till `mid` index will actually get merged in
            # to the merged intervals.
            idx = mid + 1

        # print the merged intervals.
        for merged_interval in merged_intervals:
            print(merged_interval, end=" ")
        print()


MySolution.merge_intervals([
    Interval(1, 4),
    Interval(3, 5),
    Interval(6, 8),
    Interval(10, 12),
    Interval(8, 9)
])

print()
MySolution.merge_intervals(
    [
        Interval(1, 3),
        Interval(2, 7),
        Interval(3, 5),
        Interval(1, 8),
        Interval(9, 10),
        Interval(5, 11),
        Interval(11, 12),
        Interval(7, 10),
        Interval(12, 12),
        Interval(14, 17)
    ]
)

print()
MySolution.merge_intervals(
    [
        Interval(1, 2),
        Interval(4, 6),
        Interval(2, 7),
        Interval(5, 6),
        Interval(6, 9),
        Interval(2, 11),
        Interval(8, 12),
    ]
)

print()
MySolution.merge_intervals(
    [
        Interval(7, 8),
        Interval(1, 5),
        Interval(2, 4),
        Interval(4, 6)
    ]
)

print()
MySolution.merge_intervals(
    [
        Interval(1, 3),
        Interval(2, 4),
        Interval(6, 8),
        Interval(9, 10)
    ]
)
