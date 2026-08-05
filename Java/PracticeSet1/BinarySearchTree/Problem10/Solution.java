// Problem link - https://www.geeksforgeeks.org/convert-normal-bst-balanced-bst/


package PracticeSet1.BinarySearchTree.Problem10;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static <T extends Comparable<T>> BinarySearchTree<T> getBalancedBst(BinarySearchTree<T> bst) {
        /*
            Time complexity is O(n) and space complexity is O(n + log(n)) where log(n) comes from recursion.
         */
        List<T> inorder = new ArrayList<>();
        getInorder(bst.root, inorder);
        BinarySearchTree<T> balancedBst = new BinarySearchTree<>();
        populateBalancedBst(balancedBst, inorder, 0, inorder.size() - 1);
        return balancedBst;
    }

    private static <T extends Comparable<T>> void populateBalancedBst(BinarySearchTree<T> balancedBst, List<T> inorder, int low, int high) {
        if (low > high) return;
        int mid = (low + (high - low)/2);
        T midData = inorder.get(mid);
        balancedBst.insert(midData);
        populateBalancedBst(balancedBst, inorder, low, mid - 1);
        populateBalancedBst(balancedBst, inorder, mid + 1, high);
    }

    private static <T extends Comparable<T>> void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.left, inorder);
            inorder.add(root.data);
            getInorder(root.right, inorder);
        }
    }

    private static void test(Integer...args) {
        BinarySearchTree<Integer> originalBst = new BinarySearchTree<>();
        for (Integer x : args) {
            originalBst.insert(x);
        }
        originalBst.show();
        BinarySearchTree<Integer> balancedBst = getBalancedBst(originalBst);
        balancedBst.show();
    }

    public static void main(String[] args) {
        // Example 1
        test(30, 20, 10);

        // Example 2
        test(4, 3, 5, 2, 6, 1, 7);
    }
}
