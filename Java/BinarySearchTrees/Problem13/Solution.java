// Problem link - https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1

package BinarySearchTrees.Problem13;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        System.out.println(Utility.getKthSmallest(getBstFromArray(Arrays.asList(2, 1, 3)), 2));
        System.out.println(Utility.getKthSmallest(getBstFromArray(Arrays.asList(2, 1, 3)), 5));
        System.out.println(Utility.getKthSmallest(getBstFromArray(Arrays.asList(20, 8, 22, 4, 12, 10, 14)), 3));
    }

    private static BinarySearchTree<Integer> getBstFromArray(List<Integer> arr) {
        BinarySearchTree<Integer> binarySearchTree = new BinarySearchTree<>();
        arr.forEach(binarySearchTree::insert);
        return binarySearchTree;
    }
}
