package Arrays.Problem14;

import java.util.Comparator;

public class Interval implements Comparator<Interval> {
    public Integer startTime;
    public Integer endTime;

    public Interval(Integer startTime, Integer endTime) {
        this.startTime = startTime;
        this.endTime = endTime;
    }

    @Override
    public int compare(Interval o1, Interval o2) {
        return o1.startTime - o2.startTime;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)", startTime, endTime);
    }
}
