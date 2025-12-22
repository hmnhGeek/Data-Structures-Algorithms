package Arrays.Problem14;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<Interval> intervals1 = formIntervals(List.of(1, 3, 2, 6, 8, 10, 15, 18));
        System.out.println(mergeIntervals(intervals1));

        List<Interval> intervals2 = formIntervals(List.of(1, 4, 4, 5));
        System.out.println(mergeIntervals(intervals2));

        List<Interval> intervals3 = formIntervals(List.of(4, 7, 1, 4));
        System.out.println(mergeIntervals(intervals3));

        List<Interval> intervals4 = formIntervals(List.of(1, 3, 2, 4, 6, 8, 9, 10));
        System.out.println(mergeIntervals(intervals4));

        List<Interval> intervals5 = formIntervals(List.of(7, 8, 1, 5, 2, 4, 4, 6));
        System.out.println(mergeIntervals(intervals5));
    }

    private static List<Interval> formIntervals(List<Integer> integers) {
        List<Interval> intervals = new ArrayList<>();
        for (int i = 0; i < integers.size(); i += 2) {
            intervals.add(new Interval(integers.get(i), integers.get(i + 1)));
        }
        return intervals;
    }

    public static List<Interval> mergeIntervals(List<Interval> intervals) {
        if (intervals.isEmpty() || intervals.size() == 1) {
            return intervals;
        }
        MergeSort.sort(intervals);
        List<Interval> result = new ArrayList<>();
        Interval trackerInterval = new Interval(intervals.getFirst().startTime, intervals.getFirst().endTime);
        for (int i = 0; i < intervals.size(); i += 1) {
            Interval currentInterval = intervals.get(i);
            if (currentInterval.startTime <= trackerInterval.endTime) {
                trackerInterval.endTime = Math.max(trackerInterval.endTime, currentInterval.endTime);
            } else {
                result.add(new Interval(trackerInterval.startTime, trackerInterval.endTime));
                trackerInterval.startTime = currentInterval.startTime;
                trackerInterval.endTime = currentInterval.endTime;
            }
        }
        result.add(trackerInterval);
        return result;
    }
}
