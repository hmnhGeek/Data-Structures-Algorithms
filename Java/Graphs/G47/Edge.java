package Graphs.G47;

public class Edge<T> implements Comparable<Edge<T>> {
    public Integer weight;
    public T u, v;

    public Edge(Integer weight, T u, T v) {
        this.weight = weight;
        this.u = u;
        this.v = v;
    }

    @Override
    public int compareTo(Edge<T> o) {
        return this.weight.compareTo(o.weight);
    }

    @Override
    public String toString() {
        return String.format("(%s, %s, %d)", u, v, weight);
    }
}
