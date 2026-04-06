package Graphs.G38;

public class HeapElement<T> implements Comparable<HeapElement<T>> {
    public Integer distance;
    public Integer intermediateStops;
    public T node;

    public HeapElement(Integer distance, Integer intermediateStops, T node) {
        this.distance = distance;
        this.intermediateStops = intermediateStops;
        this.node = node;
    }

    @Override
    public int compareTo(HeapElement<T> o) {
        return this.distance.compareTo(o.distance);
    }
}
