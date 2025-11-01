// Problem link - https://www.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1
// Solution - https://www.youtube.com/watch?v=eZMCRBrMznA


package BinarySearchTrees.Problem20;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        BinarySearchTree<Integer> binarySearchTree = getBst(8, 5, 9, 2, 7, 1);
        System.out.println(hasDeadEnd(binarySearchTree));

        // Example 2
        BinarySearchTree<Integer> binarySearchTree2 = getBst(8, 7, 10, 2, 9, 13);
        System.out.println(hasDeadEnd(binarySearchTree2));

        // Example 3
        BinarySearchTree<Integer> binarySearchTree3 = getBst(10, 6, 12, 2, 8, 11, 15);
        System.out.println(hasDeadEnd(binarySearchTree3));

        // Example 4
        BinarySearchTree<Integer> binarySearchTree4 = getBst(7, 4, 8);
        System.out.println(hasDeadEnd(binarySearchTree4));
    }

    public static <T extends Comparable<T>> BinarySearchTree<T> getBst(T...args) {
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        for (T i : args) {
            bst.insert(i);
        }
        return bst;
    }

    public static Boolean hasDeadEnd(BinarySearchTree<Integer> binarySearchTree) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        return checkForDeadEnds(binarySearchTree.root, 1, Integer.MAX_VALUE);
    }

    private static Boolean checkForDeadEnds(Node<Integer> root, int minValue, int maxValue) {
        if (root == null) return false;
        if (maxValue == minValue && minValue == root.data) return true;
        Boolean left = checkForDeadEnds(root.left, minValue, root.data - 1);
        Boolean right = checkForDeadEnds(root.right, root.data + 1, maxValue);
        return left || right;
    }
}
