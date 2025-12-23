package Graphs.G27;

public class GraphElement<T> {
    public T adjNode;
    public Integer weight;

    public GraphElement(T adjNode, Integer weight) {
        this.adjNode = adjNode;
        this.weight = weight;
    }
}
