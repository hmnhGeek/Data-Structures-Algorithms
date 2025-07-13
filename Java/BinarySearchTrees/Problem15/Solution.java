package BinarySearchTrees.Problem15;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
    }

    private static <T extends Comparable<T>> BinarySearchTree<T> buildTree(List<T> arr) {
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        arr.forEach(bst::insert);
        return bst;
    }
}
