package Arrays.Problem14;

public class Interval implements Comparable<Interval> {
    public Integer startTime;
    public Integer endTime;

    public Interval(Integer startTime, Integer endTime) {
        this.startTime = startTime;
        this.endTime = endTime;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)", startTime, endTime);
    }

    @Override
    public int compareTo(Interval o) {
        int diff = startTime - o.startTime;
        if (diff < 0) {
            return -1;
        } else if (diff > 0) {
            return 1;
        } else {
            return endTime.compareTo(o.endTime);
        }
    }
}
