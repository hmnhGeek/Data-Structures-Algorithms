package BinarySearchTrees.Problem2;

public class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left, right, parent;
    public Integer size, height, diameter;

    public Node(T data) {
        this.data = data;
        this.left = this.right = this.parent = null;
        this.size = this.height = this.diameter = 0;
    }
}
