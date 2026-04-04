package BinarySearchTrees.Problem5;

public class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left, right;

    public Node(T data) {
        this.data = data;
        this.left = this.right = null;
    }
}
