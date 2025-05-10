package BinaryTrees.Problem4;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static <T> Integer getHeight(Node<T> root, List<Integer> diameter) {
        if (root == null) {
            return 0;
        }
        Integer leftHeight = getHeight(root.getLeft(), diameter);
        Integer rightHeight = getHeight(root.getRight(), diameter);

        // update the diameter
        diameter.set(0, Math.max(diameter.getFirst(), 1 + leftHeight + rightHeight));

        // return the height
        return 1 + Math.max(leftHeight, rightHeight);
    }

    public static <T> Integer getDiameter(Node<T> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */

        // Store the maximum length path in an array of size 1.
        List<Integer> diameter = Arrays.asList(0);

        // update the maximum length path, which would be the diameter.
        getHeight(root, diameter);

        // return the diameter.
        return diameter.getFirst();
    }

    public static void main(String[] args) {
        // Example 1
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        n1.setLeft(n2);
        n1.setRight(n3);
        System.out.println(getDiameter(n1));

        // Example 2
        Node<Integer> n5 = new Node<>(5);
        Node<Integer> n6 = new Node<>(6);
        Node<Integer> n8 = new Node<>(8);
        Node<Integer> n_3 = new Node<>(3);
        Node<Integer> n7 = new Node<>(7);
        Node<Integer> n9 = new Node<>(9);
        n5.setLeft(n8);
        n5.setRight(n6);
        n8.setLeft(n_3);
        n8.setRight(n7);
        n6.setLeft(n9);
        System.out.println(getDiameter(n5));

        // Example 3
        Node<Integer> node1 = new Node<>(1);
        Node<Integer> node2 = new Node<>(2);
        Node<Integer> node3 = new Node<>(3);
        Node<Integer> node4 = new Node<>(4);
        Node<Integer> node5 = new Node<>(5);
        Node<Integer> node6 = new Node<>(6);
        Node<Integer> node7 = new Node<>(7);
        Node<Integer> node8 = new Node<>(8);
        Node<Integer> node9 = new Node<>(9);
        node1.setLeft(node2);
        node1.setRight(node3);
        node3.setLeft(node4);
        node3.setRight(node7);
        node4.setLeft(node5);
        node7.setRight(node8);
        node5.setLeft(node6);
        node8.setRight(node9);
        System.out.println(getDiameter(node1));
    }
}
