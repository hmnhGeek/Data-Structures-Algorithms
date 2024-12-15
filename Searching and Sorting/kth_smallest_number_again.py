class Solution:
    @staticmethod
    def _merge_intervals(intervals):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        merged = []
        for i in range(len(intervals)):
            # if it is the first interval to be added, simply add in the result
            if len(merged) == 0:
                merged.append(list(intervals[i]))
            # if the current interval's starting time > last interval's ending time, there's no overlap, simply add this
            # interval again.
            elif merged[-1][1] < intervals[i][0]:
                merged.append(list(intervals[i]))
            else:
                # else, if there's an overlap, update the end time by taking max of end times of both current interval
                # and the last interval.
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        # return merged intervals
        return merged

    @staticmethod
    def kth_smallest(intervals, k):
        """
            Overall time complexity is O(n*log(n) + 2n) and space complexity is O(n).
        """

        # in O(nlog(n)) time, sort the intervals on the starting time.
        intervals.sort(key=lambda x: x[0])
        # merge the intervals in O(n) time and O(n) space.
        merged_intervals = Solution._merge_intervals(intervals)
        # start iterating on the merged intervals in O(n) time.
        for interval in merged_intervals:
            # if the current interval size is less than k, update k by removing the length of this interval from k.
            if interval[1] - interval[0] + 1 < k:
                k -= (interval[1] - interval[0] + 1)
            else:
                # if k falls within the interval, return the value by using k as offset.
                return interval[0] + k - 1
        # if k is an outlier, return -1.
        return -1


print(Solution.kth_smallest([[1, 5], [3, 7], [10, 15]], 9))
print(Solution.kth_smallest([[1, 4], [6, 8]], 10))
print(Solution.kth_smallest([[1, 4], [6, 8]], 6))
print(Solution.kth_smallest([[2, 6], [5, 7]], 5))
print(Solution.kth_smallest([[2, 6], [5, 7]], 8))
