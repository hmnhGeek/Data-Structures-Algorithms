package Graphs.G45;

public class HeapElement<T> implements Comparable<HeapElement<T>> {
    public Integer weight;
    public T node;
    public T parent;

    public HeapElement(Integer weight, T node, T parent) {
        this.weight = weight;
        this.node = node;
        this.parent = parent;
    }

    @Override
    public int compareTo(HeapElement<T> o) {
        return this.weight.compareTo(o.weight);
    }
}
