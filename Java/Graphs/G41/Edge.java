package Graphs.G41;

public class Edge<T> {
    public T source, destination;
    public Integer edgeWeight;

    public Edge(T source, T destination, Integer edgeWeight) {
        this.source = source;
        this.destination = destination;
        this.edgeWeight = edgeWeight;
    }
}
