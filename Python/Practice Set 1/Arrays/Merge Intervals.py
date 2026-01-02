from typing import List


class Solution:
    @staticmethod
    def merge_intervals(intervals: List[List[int]]):
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        s0, e0 = intervals[0][0], intervals[0][1]
        n = len(intervals)
        i = 1
        while i < n:
            si, ei = intervals[i][0], intervals[i][1]
            if si <= e0:
                e0 = max(e0, ei)
            else:
                merged_intervals.append((s0, e0))
                s0, e0 = si, ei
            i += 1
        merged_intervals.append((s0, e0))
        return merged_intervals


print(Solution.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution.merge_intervals([[1, 4], [4, 5]]))
print(Solution.merge_intervals([[4, 7], [1, 4]]))
