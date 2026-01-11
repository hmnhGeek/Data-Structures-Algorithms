// Problem link - https://www.geeksforgeeks.org/dsa/binary-search-tree-set-1-search-and-insertion/


package BinarySearchTrees.Problem1;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        BinarySearchTree<Integer> bst = getBst(6, 2, 8, 7, 9);
        Node<Integer> node = bst.getNode(bst.root, 7);
        System.out.println(node != null ? node.data : null);

        // Example 2
        BinarySearchTree<Integer> bst1 = getBst(16, 12, 18, 10, 17, 19);
        Node<Integer> node1 = bst.getNode(bst.root, 14);
        System.out.println(node1 != null ? node1.data : null);
    }

    public static <T extends Comparable<T>> BinarySearchTree<T> getBst(T...args) {
        BinarySearchTree<T> binarySearchTree = new BinarySearchTree<>();
        for (T arg : args) {
            binarySearchTree.insert(arg);
        }
        return binarySearchTree;
    }
}
