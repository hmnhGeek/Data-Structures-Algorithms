package BinaryTrees.Problem3;


class Node<T> {
    private T data;
    private Node<T> left;
    private Node<T> right;

    public Node(T data) {
        this.data = data;
        this.left = this.right = null;
    }

    public Node<T> getRight() {
        return right;
    }

    public Node<T> getLeft() {
        return left;
    }

    public T getData() {
        return data;
    }

    public void setRight(Node<T> right) {
        this.right = right;
    }

    public void setLeft(Node<T> left) {
        this.left = left;
    }
}


class Solution {
    public static <T> Integer getHeight(Node<T> root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(getHeight(root.getLeft()), getHeight(root.getRight()));
    }

    public static void main(String[] args) {
        // Example 1
        Node<Integer> n12 = new Node<>(12);
        Node<Integer> n8 = new Node<>(8);
        Node<Integer> n18 = new Node<>(18);
        Node<Integer> n5 = new Node<>(5);
        Node<Integer> n11 = new Node<>(11);
        n12.setLeft(n8);
        n12.setRight(n18);
        n8.setLeft(n5);
        n8.setRight(n11);
        System.out.println(getHeight(n12));
    }
}