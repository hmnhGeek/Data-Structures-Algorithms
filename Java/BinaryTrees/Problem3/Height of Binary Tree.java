// Problem link - https://www.geeksforgeeks.org/problems/height-of-binary-tree/1


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
        /*
            Time complexity is O(n) and space complexity is O(n).
         */

        // if a null node is found, return 0.
        if (root == null) {
            return 0;
        }
        // else apply the height formula recursively.
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

        // Example 2
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n4 = new Node<>(4);
        Node<Integer> n51 = new Node<>(5);
        Node<Integer> n6 = new Node<>(6);
        Node<Integer> n7 = new Node<>(7);
        n1.setLeft(n2);
        n2.setLeft(n4);
        n1.setRight(n3);
        n3.setRight(n5);
        n5.setLeft(n6);
        n5.setRight(n7);
        System.out.println(getHeight(n1));
    }
}