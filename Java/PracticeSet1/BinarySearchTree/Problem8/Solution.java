package PracticeSet1.BinarySearchTree.Problem8;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Integer> bst = getBst(Arrays.asList(40, 30, 35, 80, 100));
        bst.show();
    }

    public static <T extends Comparable<T>> BinarySearchTree<T> getBst(List<T> preorder) {
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        for (T data : preorder) {
            bst.insert(data);
        }
        return bst;
    }
}
