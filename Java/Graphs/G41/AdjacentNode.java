package Graphs.G41;

public class AdjacentNode<T> {
    public T node;
    public Integer edgeWeight;

    public AdjacentNode(T node, Integer edgeWeight) {
        this.node = node;
        this.edgeWeight = edgeWeight;
    }
}