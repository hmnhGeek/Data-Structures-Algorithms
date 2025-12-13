// Problem link - https://www.geeksforgeeks.org/dsa/flatten-bst-to-sorted-list-increasing-order/


package BinarySearchTrees.Problem22;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        run(5, 3, 7, 2, 4, 6, 8);
        run(2, 3, 4, 5, 6, 7, 8);
    }

    public static void run(Integer...args) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (Integer i : Arrays.asList(args)) {
            bst.insert(i);
        }
        Node<Integer> node = flattenBst(bst.root);
        Node<Integer> curr = node;
        while (curr != null) {
            System.out.printf(curr.data + " ");
            curr = curr.right;
        }
        System.out.println();
    }

    public static <T extends Comparable<T>> Node<T> flattenBst(Node<T> root) {
        if (root == null) return null;
        List<Node<T>> inorder = new ArrayList<>();
        getInorder(root, inorder);
        for (int i = 0; i < inorder.size() - 1; i += 1) {
            Node<T> node = inorder.get(i);
            node.left = null;
            node.right = inorder.get(i + 1);
        }
        inorder.getLast().left = null;
        inorder.getLast().right = null;
        return inorder.getFirst();
    }

    private static <T extends Comparable<T>> void getInorder(Node<T> root, List<Node<T>> inorder) {
        if (root != null) {
            getInorder(root.left, inorder);
            inorder.add(root);
            getInorder(root.right, inorder);
        }
    }
}
