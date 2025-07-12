package BinaryTrees.Problem8;


import java.util.ArrayList;
import java.util.List;

class Node<T> {
    private T data;
    private Node<T> left;
    private Node<T> right;

    public Node(T data) {
        this.data = data;
        this.left = this.right = null;
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
}


public class Solution {
    public static <T> List<T> getPostorderRecursively(Node<T> root) {
        List<T> postorder = new ArrayList<>();
        getPostorderRecursively(root, postorder);
        return postorder;
    }

    private static <T> void getPostorderRecursively(Node<T> root, List<T> postorder) {
        if (root != null) {
            getPostorderRecursively(root.getLeft(), postorder);
            getPostorderRecursively(root.getRight(), postorder);
            postorder.add(root.getData());
        }
    }

    public static <T> List<T> getPostorderIteratively(Node<T> root) {

    }
}
