// Problem link - https://www.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

package PracticeSet1.BinarySearchTree.Problem12;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        test(Arrays.asList(4, 2, 9), 2);
        test(Arrays.asList(10, 2, 11, 1, 5, 3, 6, 4), 7);
        test(Arrays.asList(2, 4, 8, 9, 3, 6, 9, 5), 5);
    }

    private static void test(List<Integer> elements, Integer k) {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (Integer i : elements) {
            bst.insert(i);
        }
        System.out.println(getKthLargest(bst, k));
    }

    public static Integer getKthLargest(BinarySearchTree<Integer> bst, Integer k) {
        /*
            Overall time complexity is O(n) and space complexity is O(log(n)).
         */
        if (k <= 0) return null;
        // This will take O(n) time and O(log(n)) space.
        int n = bst.getNumNodes();
        int position = n - k + 1;
        List<Integer> result = Arrays.asList(null, 0);
        // This will take O(n) time and O(log(n)) space.
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
