package Graphs.G37;

public class HeapElement<T extends Comparable<T>> implements Comparable<HeapElement<T>> {
    public T data;
    public Integer i, j;

    public HeapElement(T data, Integer i, Integer j) {
        this.data = data;
        this.i = i;
        this.j = j;
    }

    @Override
    public int compareTo(HeapElement<T> o) {
        return this.data.compareTo(o.data);
    }
}
