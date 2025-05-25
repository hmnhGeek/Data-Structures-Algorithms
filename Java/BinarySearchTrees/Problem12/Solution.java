package BinarySearchTrees.Problem12;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (Integer i : Arrays.asList(2, 6, 8, 0, 9, 9, 7)) {
            bst.insert(i);
        }
        bst.show();
    }
}
