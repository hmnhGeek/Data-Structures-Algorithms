# Problem link - https://www.naukri.com/code360/problems/merge-overlapping-intervals_1082151
# Solution - https://www.youtube.com/watch?v=IexN60k62jo&t=306s


from typing import List


class Solution:
    @staticmethod
    def merge_intervals(intervals: List[List[int]]):
        """
            Time complexity is O(n*log(n)) and space complexity is O(n).
        """
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
print(Solution.merge_intervals([[1, 3], [2, 4], [6, 8], [9, 10]]))
print(Solution.merge_intervals([[7, 8], [1, 5], [2, 4], [4, 6]]))
print(Solution.merge_intervals([[1, 3], [1, 5], [6, 7]]))
print(Solution.merge_intervals([[1, 2], [2, 3]]))
