package PracticeSet1.BinarySearchTree.Problem12;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (Integer i : Arrays.asList(4, 2, 9)) {
            bst.insert(i);
        }
        System.out.println(getKthLargest(bst, 2));
    }

    public static Integer getKthLargest(BinarySearchTree<Integer> bst, Integer k) {
        if (k <= 0) return null;
        int n = bst.getNumNodes();
        int position = n - k + 1;
        List<Integer> result = Arrays.asList(null, 0);
        findKthLargest(bst.root, result, position);
        return result.getFirst();
    }

    private static void findKthLargest(Node<Integer> start, List<Integer> result, int position) {
        if (start != null) {
            findKthLargest(start.left, result, position);
            result.set(1, result.getLast() + 1);
            if (result.getLast().equals(position)) {
                result.set(0, start.data);
            }
            findKthLargest(start.right, result, position);
        }
    }
}
