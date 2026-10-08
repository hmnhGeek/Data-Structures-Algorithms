// Problem link - https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1


package PracticeSet1.BinarySearchTree.Problem13;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        test(Arrays.asList(20, 8, 22, 4, 12, 10, 14), 3);
        test(Arrays.asList(2, 1, 3), 5);
    }

    private static <T extends Comparable<T>> void test(List<T> arr, int k) {
        BinarySearchTree<T> binarySearchTree = new BinarySearchTree<>();
        for (T x : arr) {
            binarySearchTree.insert(x);
        }
        System.out.println(getKthSmallest(binarySearchTree, k));
    }

    public static <T extends Comparable<T>> T getKthSmallest(BinarySearchTree<T> bst, Integer k) {
        /*
            Time complexity is O(n) and space complexity is O(log(n)).
         */
        List<T> inorder = new ArrayList<>();
        getInorder(bst.root, inorder);
        try {
            return inorder.get(k - 1);
        } catch (IndexOutOfBoundsException ex) {
            return null;
        }
    }

    private static <T extends Comparable<T>> void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.left, inorder);
            inorder.add(root.data);
            getInorder(root.right, inorder);
        }
    }
}
