// Problem link - https://www.geeksforgeeks.org/create-a-mirror-tree-from-the-given-binary-tree/


package BinaryTrees.Problem5;

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
    public static <T> Node<T> getMirror(Node<T> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        if (root == null) {
            return null;
        }
        Node<T> leftNode = getMirror(root.getLeft());
        Node<T> rightNode = getMirror(root.getRight());
        Node<T> newRoot = new Node<>(root.getData());
        newRoot.setLeft(rightNode);
        newRoot.setRight(leftNode);
        return newRoot;
    }

    private static <T> void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.getLeft(), inorder);
            inorder.add(root.getData());
            getInorder(root.getRight(), inorder);
        }
    }

    public static <T> List<T> getInorder(Node<T> root) {
        List<T> inorder = new ArrayList<>();
        getInorder(root, inorder);
        return inorder;
    }

    public static void main(String[] args) {
        // Example 1
        Node<Integer> n5 = new Node<>(5);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n6 = new Node<>(6);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n4 = new Node<>(4);
        n5.setLeft(n3);
        n5.setRight(n6);
        n3.setLeft(n2);
        n3.setRight(n4);
        System.out.println(getInorder(n5));
        Node<Integer> mirror = getMirror(n5);
        System.out.println(getInorder(mirror));

        // Example 2
        Node<Integer> n21 = new Node<>(2);
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n8 = new Node<>(8);
        Node<Integer> n12 = new Node<>(12);
        Node<Integer> n9 = new Node<>(9);
        n21.setLeft(n1);
        n21.setRight(n8);
        n1.setLeft(n12);
        n8.setRight(n9);
        System.out.println(getInorder(n21));
        Node<Integer> mirror2 = getMirror(n21);
        System.out.println(getInorder(mirror2));

        // Example 3
        Node<Integer> five = new Node<>(5);
        Node<Integer> three = new Node<>(3);
        Node<Integer> six = new Node<>(6);
        Node<Integer> two = new Node<>(2);
        Node<Integer> four = new Node<>(4);
        Node<Integer> eight = new Node<>(8);
        Node<Integer> ten = new Node<>(10);
        Node<Integer> eleven = new Node<>(11);
        Node<Integer> twelve = new Node<>(12);
        Node<Integer> thirteen = new Node<>(13);
        five.setLeft(three);
        five.setRight(six);
        three.setLeft(two);
        three.setRight(four);
        six.setLeft(eight);
        six.setRight(ten);
        eight.setLeft(eleven);
        eight.setRight(twelve);
        twelve.setLeft(thirteen);
        System.out.println(Solution.getInorder(five));
        Node<Integer> mirror3 = Solution.getMirror(five);
        System.out.println(Solution.getInorder(mirror3));
    }
}
