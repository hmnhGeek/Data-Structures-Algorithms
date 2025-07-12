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
    public static void main(String[] args) {
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n4 = new Node<>(4);
        Node<Integer> n5 = new Node<>(5);
        Node<Integer> n6 = new Node<>(6);
        Node<Integer> n7 = new Node<>(7);
        Node<Integer> n8 = new Node<>(8);
        n1.setLeft(n2);
        n2.setLeft(n4);
        n1.setRight(n3);
        n3.setRight(n6);
        n3.setLeft(n5);
        n5.setLeft(n7);
        n5.setRight(n8);
        System.out.println(getPostorderIteratively(n1));
        System.out.println(getPostorderRecursively(n1));
    }

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
        Stack<Node<T>> stack = new Stack<>();
        stack.push(root);
        List<T> result = new ArrayList<>();
        while (!stack.isEmpty()) {
            Node<T> node = stack.pop();
            result.add(node.getData());
            if (node.getLeft() != null) {
                stack.push(node.getLeft());
            }
            if (node.getRight() != null) {
                stack.push(node.getRight());
            }
        }
        List<T> reversed = result.reversed();
        return reversed;
    }
}
