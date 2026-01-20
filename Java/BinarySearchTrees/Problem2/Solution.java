// Problem link - https://leetcode.com/problems/delete-node-in-a-bst/description/


package BinarySearchTrees.Problem2;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        test(3, 5, 3, 6, 2, 4, 7);

        // Example 2
        test(0, 5, 2, 6, 4, 7);
    }

    private static void test(Integer x, Integer...args) {
        BinarySearchTree<Integer> bst = getBst(args);
        bst.show();
        bst.delete(x);
        System.out.println();
        bst.show();
        System.out.println();
    }

    private static <T extends Comparable<T>> BinarySearchTree<T> getBst(T...args) {
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        for (T arg : args) {
            bst.insert(arg);
        }
        return bst;
    }
}
