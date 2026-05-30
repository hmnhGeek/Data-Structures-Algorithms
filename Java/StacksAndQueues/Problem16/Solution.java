package StacksAndQueues.Problem16;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Interval> mergeIntervals(List<Interval> intervals) {
        intervals.sort(null);
        int n = intervals.size();
        List<Interval> merged = new ArrayList<>();
        merged.add(intervals.getFirst());
        for (int i = 1; i < n; i += 1) {
            Interval currentInterval = intervals.get(i);
            Interval lastInterval = merged.getLast();
            if (lastInterval.endTime >= currentInterval.startTime) {
                // merge the intervals
                Interval mergedInterval = new Interval(null, null);
                mergedInterval.startTime = Math.min(lastInterval.startTime, currentInterval.startTime);
                mergedInterval.endTime = Math.max(lastInterval.endTime, currentInterval.endTime);
                merged.set(merged.size() - 1, mergedInterval);
            } else {
                merged.add(currentInterval);
            }
        }
        return merged;
    }

    public static void main(String[] args) {
        System.out.println(
                mergeIntervals(
                        Arrays.asList(
                                new Interval(1, 3),
                                new Interval(2, 4),
                                new Interval(6, 8),
                                new Interval(9, 10)
                        )
                )
        );

        System.out.println(
                mergeIntervals(
                        Arrays.asList(
                                new Interval(7, 8),
                                new Interval(1, 5),
                                new Interval(2, 4),
                                new Interval(4, 6)
                        )
                )
        );

        System.out.println(
                mergeIntervals(
                        Arrays.asList(
                                new Interval(1, 3),
                                new Interval(2, 6),
                                new Interval(8, 10),
                                new Interval(15, 18)
                        )
                )
        );

        System.out.println(
                mergeIntervals(
                        Arrays.asList(
                                new Interval(1, 4),
                                new Interval(4, 5)
                        )
                )
        );

        System.out.println(
                mergeIntervals(
                        Arrays.asList(
                                new Interval(4, 7),
                                new Interval(1, 4)
                        )
                )
        );
    }
}
