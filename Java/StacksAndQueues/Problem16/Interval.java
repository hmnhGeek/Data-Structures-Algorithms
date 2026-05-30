package StacksAndQueues.Problem16;

public class Interval implements Comparable<Interval> {
    public Integer startTime;
    public Integer endTime;

    public Interval(Integer startTime, Integer endTime) {
        this.startTime = startTime;
        this.endTime = endTime;
    }

    @Override
    public int compareTo(Interval o) {
        return this.startTime - o.startTime;
    }
}
