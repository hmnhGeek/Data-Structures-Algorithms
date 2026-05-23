package BinaryTrees.Problem21;


public class Point implements Comparable<Point> {
    public Integer value, index;

    public Point(Integer value, Integer index) {
        this.value = value;
        this.index = index;
    }

    @Override
    public int compareTo(Point o) {
        return this.value.compareTo(o.value);
    }
}
