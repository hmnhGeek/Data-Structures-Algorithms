// Problem link - https://www.geeksforgeeks.org/problems/preorder-to-postorder4423/1


package BinarySearchTrees.Problem19;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Integer> bst = getBstFromPreorder(Arrays.asList(40, 30, 35, 80, 100));
        bst.show();

        BinarySearchTree<Integer> bst2 = getBstFromPreorder(Arrays.asList(40,30,32,35,80,90,100,120));
        bst2.show();
    }

    public static <T extends Comparable<T>> BinarySearchTree<T> getBstFromPreorder(List<T> preorder) {
        /*
            Overall time complexity is O(n * log(n)) and space complexity is O(n).
         */
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        preorder.forEach(bst::insert);
        return bst;
    }
}
