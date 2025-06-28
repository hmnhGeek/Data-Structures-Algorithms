// Problem link - https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/

package BinaryTrees.Problem7;

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
        // Example 1
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
        System.out.println(getPreorderRecursively(n1));
        System.out.println(getPreorderIteratively(n1));
    }

    public static <T> List<T> getPreorderRecursively(Node<T> root) {
        List<T> preorder = new ArrayList<>();
        getPreorderRecursively(root, preorder);
        return preorder;
    }

    private static <T> void getPreorderRecursively(Node<T> start, List<T> preorder) {
        if (start != null) {
            preorder.add(start.getData());
            getPreorderRecursively(start.getLeft(), preorder);
            getPreorderRecursively(start.getRight(), preorder);
        }
    }

    public static <T> List<T> getPreorderIteratively(Node<T> root) {
        if (root == null) return new ArrayList<>();
        Stack<Node<T>> stack = new Stack<>();
        stack.push(root);
        List<T> result = new ArrayList<>();
        while (!stack.isEmpty()) {
            Node<T> node = stack.pop();
            result.add(node.getData());
            if (node.getRight() != null) {
                stack.push(node.getRight());
            }
            if (node.getLeft() != null) {
                stack.push(node.getLeft());
            }
        }
        return result;
    }
}
