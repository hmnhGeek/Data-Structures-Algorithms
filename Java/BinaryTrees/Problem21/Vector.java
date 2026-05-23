package BinaryTrees.Problem21;


public class Vector implements Comparable<Vector> {
    public Integer value, index;

    public Vector(Integer value, Integer index) {
        this.value = value;
        this.index = index;
    }

    @Override
    public int compareTo(Vector o) {
        return this.value.compareTo(o.value);
    }
}
