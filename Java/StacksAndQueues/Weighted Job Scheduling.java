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
        // construct an array of Jobs and then sort them based on their start times in O(n * log(n)) time and O(n) space.
        List<Job> jobs = new ArrayList<>();
        for (int i = 0; i < startTimes.size(); i += 1) {
            jobs.add(new Job(startTimes.get(i), endTimes.get(i), profits.get(i)));
        }
        jobs.sort(Comparator.comparing(Job::getStartTime));

        HashMap<Integer, Double> dp = new HashMap<>();
        for (int i = 0; i < jobs.size(); i += 1) {
            dp.put(i, null);
        }

        // return the max profit starting from the 0th job.
        return getMaxProfitMemoized(jobs, 0, jobs.size(), dp);
    }

    private static Double getMaxProfit(List<Job> jobs, Integer i, Integer n) {
        // base case of recursion.
        if (i >= n) {
            return 0.0;
        }

        // get the next valid job's index in O(log(n)) and space complexity is O(1).
        Integer nextJobIndex = getNextJobIndex(jobs, i, n);

        // add the job's profit if considered.
        double left = jobs.get(i).getProfit() + getMaxProfit(jobs, nextJobIndex, n);

        // simply move to the next job if this job is not considered.
        double right = getMaxProfit(jobs, i + 1, n);

        // return the max profit.
        return Math.max(left, right);
    }

    private static Double getMaxProfitMemoized(List<Job> jobs, Integer i, Integer n, HashMap<Integer, Double> dp) {
        // base case of recursion.
        if (i >= n) {
            return 0.0;
        }

        if (dp.get(i) != null) {
            return dp.get(i);
        }

        // get the next valid job's index in O(log(n)) and space complexity is O(1).
        Integer nextJobIndex = getNextJobIndex(jobs, i, n);

        // add the job's profit if considered.
        double left = jobs.get(i).getProfit() + getMaxProfitMemoized(jobs, nextJobIndex, n, dp);

        // simply move to the next job if this job is not considered.
        double right = getMaxProfitMemoized(jobs, i + 1, n, dp);

        // return the max profit.
        dp.put(i, Math.max(left, right));
        return dp.get(i);
    }

    /**
     *
     * @param jobs List of jobs.
     * @param index Current job's index which is considered for profit.
     * @param n Length of the jobs array.
     * @return The index of the next valid job that can be considered for profit.
     */
    private static Integer getNextJobIndex(List<Job> jobs, Integer index, Integer n) {
        int low = index + 1;
        int high = n - 1;
        Job currentJob = jobs.get(index);

        while (low <= high) {
            int mid = low + (high - low)/2;
            Job nextPossibleJob = jobs.get(mid);

            // if the mid-job's start time < current job's end time, then we must search to the right.
            if (nextPossibleJob.getStartTime() < currentJob.getEndTime()) {
                low = mid + 1;
            } else if (nextPossibleJob.getStartTime() > currentJob.getEndTime()) {
                // if opposite, then we must search for even earlier job.
                high = mid - 1;
            } else {
                // if equal, then also we must search for even earlier job.
                high = mid - 1;
            }
        }

        // low points to the correct answer.
        return low;
    }
}