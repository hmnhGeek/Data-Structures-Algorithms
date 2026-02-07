package BinarySearchTrees.Problem3;

public class Solution {
    public static void main(String[] args) {

    }

    private static <T extends Comparable<T>> BinarySearchTree<T> getBst(T...args) {
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        for (T x : args) {
            bst.insert(x);
        }
        return bst;
    }
}
