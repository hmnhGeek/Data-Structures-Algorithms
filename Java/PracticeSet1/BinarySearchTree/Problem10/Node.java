package PracticeSet1.BinarySearchTree.Problem10;

public class Node<T extends Comparable<T>> {
    public T data;
    public Integer height, size, diameter;
    public Node<T> left, right, parent;

    public Node(T data) {
        this.data = data;
        this.height = this.size = this.diameter = 1;
        this.left = this.right = this.parent = null;
    }
}
