package PracticeSet1.BinarySearchTree.Problem15;

public class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left, right, parent;
    public Integer size, diameter, height;

    public Node(T data) {
        this.data = data;
        this.left = this.right = this.parent = null;
        this.size = this.diameter = this.height = 1;
    }
}
