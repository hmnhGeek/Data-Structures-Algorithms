package BinarySearchTrees.Problem9;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Node<T extends Comparable<T>> {
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


class Solution {
    public static void main(String[] args) {
        // Example 1
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n4 = new Node<>(4);
        n1.setLeft(n2);
        n2.setLeft(n4);
        n1.setRight(n3);
        System.out.println(getInorder(n1));
        convertToBst(n1);
        System.out.println(getInorder(n1));
    }

    public static <T extends Comparable<T>> void convertToBst(Node<T> root) {
        /**
         * Time complexity is O(n * log(n)) and space complexity is O(n).
         */

        // get the inorder of this binary tree in O(n) time and O(n) space.
        List<T> inorder = getInorder(root);

        // sort the inorder list in O(n * log(n)) time.
        inorder.sort(Comparator.naturalOrder());

        // begin the BST construction in O(n) time and O(n) space.
        finalizeConstruction(root, inorder, Arrays.asList(0));
    }

    private static <T extends Comparable<T>> void finalizeConstruction(Node<T> root, List<T> sortedInorder, List<Integer> i) {
        if (root != null) {
            finalizeConstruction(root.getLeft(), sortedInorder, i);

            // update the root's data with ith pointer in sorted inorder list.
            root.setData(sortedInorder.get(i.getFirst()));
            i.set(0, i.getFirst() + 1);

            finalizeConstruction(root.getRight(), sortedInorder, i);
        }
    }

    private static <T extends Comparable<T>> List<T> getInorder(Node<T> root) {
        List<T> inorder = new ArrayList<>();
        getInorderHelper(root, inorder);
        return inorder;
    }

    private static <T extends Comparable<T>> void getInorderHelper(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorderHelper(root.getLeft(), inorder);
            inorder.add(root.getData());
            getInorderHelper(root.getRight(), inorder);
        }
    }
}