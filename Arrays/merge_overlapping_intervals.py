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


class Solution:
    @staticmethod
    def _merge(intervals, interval, index, merged_intervals):
        low = index
        high = len(intervals) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            target_interval = intervals[mid]
            if interval.get_end_time() >= target_interval.get_start_time():
                low = mid + 1
            else:
                high = mid - 1
        return high

    @staticmethod
    def merge_intervals(intervals: List[Interval]):
        intervals.sort(key=lambda x: x.start)
        merged_intervals = []
        interval = intervals[0]
        idx = 1
        while idx < len(intervals):
            mid = Solution._merge(intervals, interval, idx, merged_intervals)
            if mid < idx:
                merged_intervals.append(intervals[mid + 1])
                interval = intervals[mid + 1]
            else:
                target_interval = intervals[mid]
                if interval.get_end_time() >= target_interval.get_start_time():
                    merged_interval = Interval(
                        min(interval.get_start_time(), target_interval.get_start_time()),
                        max(interval.get_end_time(), target_interval.get_end_time())
                    )
                    if len(merged_intervals) > 0:
                        merged_intervals.pop(-1)
                    merged_intervals.append(merged_interval)
                    interval = merged_interval
                else:
                    merged_intervals.append(target_interval)
                    interval = target_interval
            idx = mid + 1

        for merged_interval in merged_intervals:
            print(merged_interval, end=" ")
        print()


Solution.merge_intervals([
    Interval(1, 4),
    Interval(3, 5),
    Interval(6, 8),
    Interval(10, 12),
    Interval(8, 9)
])

print()
Solution.merge_intervals(
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
Solution.merge_intervals(
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
