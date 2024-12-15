class Solution:
    @staticmethod
    def _merge_intervals(intervals):
        merged = []
        for i in range(len(intervals)):
            if len(merged) == 0:
                merged.append(list(intervals[i]))
            elif merged[-1][1] < intervals[i][0]:
                merged.append(list(intervals[i]))
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        return merged

    @staticmethod
    def kth_smallest(intervals, k):
        intervals.sort(key=lambda x: x[0])
        merged_intervals = Solution._merge_intervals(intervals)
        for interval in merged_intervals:
            if interval[1] - interval[0] + 1 < k:
                k -= (interval[1] - interval[0] + 1)
            else:
                return interval[0] + k - 1
        return -1


print(Solution.kth_smallest([[1, 5], [3, 7], [10, 15]], 9))
print(Solution.kth_smallest([[1, 4], [6, 8]], 10))
print(Solution.kth_smallest([[1, 4], [6, 8]], 6))
print(Solution.kth_smallest([[2, 6], [5, 7]], 5))
print(Solution.kth_smallest([[2, 6], [5, 7]], 8))
