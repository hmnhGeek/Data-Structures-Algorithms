package PracticeSet1.BinarySearchTree.Problem7;

public class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left, right, parent;
    public Integer height, diameter, size;

    public Node(T data) {
        this.data = data;
        this.height = this.size = this.diameter = 1;
        this.left = this.right = this.parent = null;
    }
}
