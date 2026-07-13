// Problem link - https://www.geeksforgeeks.org/problems/binary-tree-to-bst/1


package PracticeSet1.BinarySearchTree.Problem9;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        n1.left = n2;
        n1.right = n3;
        convertToBst(n1);
        show(n1);
        System.out.println();

        // Example 2
        Node<Integer> a1 = new Node<>(1);
        Node<Integer> a2 = new Node<>(2);
        Node<Integer> a3 = new Node<>(3);
        Node<Integer> a4 = new Node<>(4);
        a1.left = a2;
        a2.left = a4;
        a1.right = a3;
        convertToBst(a1);
        show(a1);
        System.out.println();

        // Example 3
        Node<Integer> b10 = new Node<>(10);
        Node<Integer> b2 = new Node<>(2);
        Node<Integer> b7 = new Node<>(7);
        Node<Integer> b8 = new Node<>(8);
        Node<Integer> b4 = new Node<>(4);
        b10.left = b2;
        b10.right = b7;
        b2.left = b8;
        b2.right = b4;
        convertToBst(b10);
        show(b10);
        System.out.println();
    }

    public static <T extends Comparable<T>> void convertToBst(Node<T> root) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        List<T> inorder = new ArrayList<>();
        List<Node<T>> nodeInorder = new ArrayList<>();
        populateInorder(root, inorder, nodeInorder);
        QuickSort.sort(inorder);
        for (int i = 0; i < inorder.size(); i += 1) {
            nodeInorder.get(i).data = inorder.get(i);
        }
    }

    private static <T extends Comparable<T>> void populateInorder(Node<T> root, List<T> inorder, List<Node<T>> nodeInorder) {
        if (root != null)  {
            populateInorder(root.left, inorder, nodeInorder);
            inorder.add(root.data);
            nodeInorder.add(root);
            populateInorder(root.right, inorder, nodeInorder);
        }
    }

    public static <T> void show(Node<T> root) {
        if (root != null) {
            show(root.left);
            System.out.println(root.data);
            show(root.right);
        }
    }
}
