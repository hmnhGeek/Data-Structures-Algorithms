// Problem link - https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1


package BinarySearchTrees.Problem3;

public class Solution {
    public static void main(String[] args) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        test(5, 4, 6, 3, 7, 1);
        test(10, 5, 20, 2);
        test(10, 10, 11);
    }

    private static <T extends Comparable<T>> void test(T...args) {
        BinarySearchTree<T> bst = getBst(args);
        BinarySearchTree<T> maxMin = getMaxAndMin(bst);
        System.out.println(String.format("Min = %s, Max = %s", maxMin.root.data, maxMin.root.right.data));
    }

    private static <T extends Comparable<T>> BinarySearchTree<T> getBst(T...args) {
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        for (T x : args) {
            bst.insert(x);
        }
        return bst;
    }

    public static <T extends Comparable<T>> BinarySearchTree<T> getMaxAndMin(BinarySearchTree<T> bst) {
        Node<T> leftmost = bst.getLeftmostLeaf(bst.root);
        Node<T> rightmost = bst.getRightmostLeaf(bst.root);
        BinarySearchTree<T> result = new BinarySearchTree<>();
        result.insert(leftmost.data);
        result.insert(rightmost.data);
        return result;
    }
}
