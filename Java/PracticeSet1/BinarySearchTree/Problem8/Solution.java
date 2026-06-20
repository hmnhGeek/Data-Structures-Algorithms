// Problem link - https://www.geeksforgeeks.org/dsa/construct-bst-from-given-preorder-traversa/#expected-approach-2-using-iterative-monotonic-stack-approach-on-time-oh-space


package PracticeSet1.BinarySearchTree.Problem8;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Integer> bst = getBst(Arrays.asList(40, 30, 35, 80, 100));
        bst.show();
        BinarySearchTree<Integer> bst2 = getBst(Arrays.asList(10, 5, 1, 7, 40, 50));
        bst2.show();
    }

    public static <T extends Comparable<T>> BinarySearchTree<T> getBst(List<T> preorder) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(log(n)).
         */
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        for (T data : preorder) {
            bst.insert(data);
        }
        return bst;
    }
}
