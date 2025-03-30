// Problem link - https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
// Solution - https://www.youtube.com/watch?v=LL0tVxlAeV4

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
                getMaxProfit(
                        Arrays.asList(1, 2, 3, 3),
                        Arrays.asList(3, 4, 5, 6),
                        Arrays.asList(50.0, 10.0, 40.0, 70.0)
                )
        );

        System.out.println(
                getMaxProfit(
                        Arrays.asList(1, 3, 6, 2),
                        Arrays.asList(2, 5, 19, 100),
                        Arrays.asList(50.0, 20.0, 100.0, 200.0)
                )
        );

        System.out.println(
                getMaxProfit(
                        Arrays.asList(1, 2, 4, 5),
                        Arrays.asList(3, 5, 6, 7),
                        Arrays.asList(60.0, 50.0, 70.0, 30.0)
                )
        );

        System.out.println(
                getMaxProfit(
                        Arrays.asList(1, 2, 3, 4, 6),
                        Arrays.asList(3, 5, 10, 6, 9),
                        Arrays.asList(20.0, 20.0, 100.0, 70.0, 60.0)
                )
        );

        System.out.println(
                getMaxProfit(
                        Arrays.asList(1, 1, 1),
                        Arrays.asList(2, 3, 4),
                        Arrays.asList(5.0, 6.0, 4.0)
                )
        );
    }

    private static Double getMaxProfit(List<Integer> startTimes, List<Integer> endTimes, List<Double> profits) {
        /*
        * Overall time complexity is O(n * log(n)) and space complexity is O(n).
        * */

        // construct an array of Jobs and then sort them based on their start times in O(n * log(n)) time and O(n) space.
        List<Job> jobs = new ArrayList<>();
        for (int i = 0; i < startTimes.size(); i += 1) {
            jobs.add(new Job(startTimes.get(i), endTimes.get(i), profits.get(i)));
        }
        jobs.sort(Comparator.comparing(Job::getStartTime));

        int n = jobs.size();

        // define a dp hash map of size O(n + 1).
        HashMap<Integer, Double> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            dp.put(i, null);
        }

        // put the base case in dp.
        dp.put(n, 0.0);

        // since i : 0 --> n - 1, we do it the reverse way here. This will take another O(n * log(n)) time.
        for (int i = n - 1; i >= 0; i--) {
            // get the next valid job's index in O(log(n)) and space complexity is O(1).
            Integer nextJobIndex = getNextJobIndex(jobs, i, n);

            // add the job's profit if considered.
            double left = jobs.get(i).getProfit() + dp.get(nextJobIndex);

            // simply move to the next job if this job is not considered.
            double right = dp.get(i + 1);

            // return the max profit.
            dp.put(i, Math.max(left, right));
        }

        // return the max profit starting from the 0th job.
        return dp.get(0);
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