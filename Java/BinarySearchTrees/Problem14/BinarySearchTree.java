package BinarySearchTrees.Problem14;

class Node<T> {
    private T data;
    private Node<T> left;
    private Node<T> right;
    private Node<T> parent;
    private Integer size;
    private Integer height;
    private Integer diameter;

    public Node(T data) {
        this.data = data;
        this.diameter = this.size = this.height = 1;
        this.left = this.right = this.left = null;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getLeft() {
        return left;
    }

    public void setLeft(Node<T> left) {
        this.left = left;
    }

    public Node<T> getRight() {
        return right;
    }

    public void setRight(Node<T> right) {
        this.right = right;
    }

    public Node<T> getParent() {
        return parent;
    }

    public void setParent(Node<T> parent) {
        this.parent = parent;
    }

    public Integer getSize() {
        return size;
    }

    public void setSize(Integer size) {
        this.size = size;
    }

    public Integer getHeight() {
        return height;
    }

    public void setHeight(Integer height) {
        this.height = height;
    }

    public Integer getDiameter() {
        return diameter;
    }

    public void setDiameter(Integer diameter) {
        this.diameter = diameter;
    }
}

public class BinarySearchTree<T> {
}
