package StacksAndQueues;

import java.util.*;

class Job {
    private Integer startTime;
    private Integer endTime;
    private Double profit;

    public Job(Integer startTime, Integer endTime, Double profit) {
        this.startTime = startTime;
        this.endTime = endTime;
        this.profit = profit;
    }

    public Integer getStartTime() {
        return startTime;
    }

    public void setStartTime(Integer startTime) {
        this.startTime = startTime;
    }

    public Integer getEndTime() {
        return endTime;
    }

    public void setEndTime(Integer endTime) {
        this.endTime = endTime;
    }

    public Double getProfit() {
        return profit;
    }

    public void setProfit(Double profit) {
        this.profit = profit;
    }
}


class Solution {
    public static void main(String[] args) {
        System.out.println(
                getMaxProfitHelper(
                        Arrays.asList(1, 2, 3, 3),
                        Arrays.asList(3, 4, 5, 6),
                        Arrays.asList(50.0, 10.0, 40.0, 70.0)
                )
        );

        System.out.println(
                getMaxProfitHelper(
                        Arrays.asList(1, 3, 6, 2),
                        Arrays.asList(2, 5, 19, 100),
                        Arrays.asList(50.0, 20.0, 100.0, 200.0)
                )
        );

        System.out.println(
                getMaxProfitHelper(
                        Arrays.asList(1, 2, 4, 5),
                        Arrays.asList(3, 5, 6, 7),
                        Arrays.asList(60.0, 50.0, 70.0, 30.0)
                )
        );

        System.out.println(
                getMaxProfitHelper(
                        Arrays.asList(1, 2, 3, 4, 6),
                        Arrays.asList(3, 5, 10, 6, 9),
                        Arrays.asList(20.0, 20.0, 100.0, 70.0, 60.0)
                )
        );

        System.out.println(
                getMaxProfitHelper(
                        Arrays.asList(1, 1, 1),
                        Arrays.asList(2, 3, 4),
                        Arrays.asList(5.0, 6.0, 4.0)
                )
        );
    }

    private static Double getMaxProfitHelper(List<Integer> startTimes, List<Integer> endTimes, List<Double> profits) {
        List<Job> jobs = new ArrayList<>();
        for (int i = 0; i < startTimes.size(); i += 1) {
            jobs.add(new Job(startTimes.get(i), endTimes.get(i), profits.get(i)));
        }
        jobs.sort(Comparator.comparing(Job::getStartTime));
        return getMaxProfit(jobs, 0, jobs.size());
    }

    private static Double getMaxProfit(List<Job> jobs, Integer i, Integer n) {
        if (i >= n) {
            return 0.0;
        }
        Integer nextJobIndex = getNextJobIndex(jobs, i, n);
        double left = jobs.get(i).getProfit() + getMaxProfit(jobs, nextJobIndex, n);
        double right = getMaxProfit(jobs, i + 1, n);
        return Math.max(left, right);
    }

    private static Integer getNextJobIndex(List<Job> jobs, Integer index, Integer n) {
        int low = index + 1;
        int high = n - 1;
        Job currentJob = jobs.get(index);

        while (low <= high) {
            int mid = low + (high - low)/2;
            Job nextPossibleJob = jobs.get(mid);
            if (nextPossibleJob.getStartTime() < currentJob.getEndTime()) {
                low = mid + 1;
            } else if (nextPossibleJob.getStartTime() > currentJob.getEndTime()) {
                high = mid - 1;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
}