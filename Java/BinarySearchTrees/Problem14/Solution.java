package BinarySearchTrees.Problem14;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Integer> bst1 = buildTree(Arrays.asList(5, 3, 7, 2, 4, 6, 8));
        BinarySearchTree<Integer> bst2 = buildTree(Arrays.asList(10, 6, 15, 3, 8, 11, 18));
        System.out.println(countPairs(bst1, bst2, 16));
    }

    private static void updateCount(Node<Integer> start, BinarySearchTree<Integer> bst, List<Integer> counter, Integer x) {
        if (start != null) {
            updateCount(start.getLeft(), bst, counter, x);
            int a = start.getData();
            int b = x - a;
            if (bst.getNode(bst.getRoot(), b) != null) {
                counter.set(0, counter.getFirst() + 1);
            }
            updateCount(start.getRight(), bst, counter, x);
        }
    }

    public static Integer countPairs(BinarySearchTree<Integer> binarySearchTree1, BinarySearchTree<Integer> binarySearchTree2, Integer x) {
        List<Integer> counter = Arrays.asList(0);
        updateCount(binarySearchTree1.getRoot(), binarySearchTree2, counter, x);
        return counter.getFirst();
    }

    private static BinarySearchTree<Integer> buildTree(List<Integer> arr) {
        BinarySearchTree<Integer> result = new BinarySearchTree<>();
        for (Integer i : arr) {
            result.insert(i);
        }
        return result;
    }
}
