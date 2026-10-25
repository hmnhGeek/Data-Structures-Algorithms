package PracticeSet1.BinarySearchTree.Problem14;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        test(
                Arrays.asList(2, 1, 3),
                Arrays.asList(5, 4, 6),
                6
        );
        test(
                Arrays.asList(7, 5, 10, 1),
                Arrays.asList(2, 6),
                9
        );
    }

    private static void test(List<Integer> arr1, List<Integer> arr2, Integer k) {
        BinarySearchTree<Integer> bst1 = getBstFromArray(arr1);
        BinarySearchTree<Integer> bst2 = getBstFromArray(arr2);
        int count = getCountOfPairs(bst1, bst2, k);
        System.out.println(count);
    }

    private static BinarySearchTree<Integer> getBstFromArray(List<Integer> arr) {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (Integer i : arr) {
            bst.insert(i);
        }
        return bst;
    }

    public static Integer getCountOfPairs(BinarySearchTree<Integer> bst1, BinarySearchTree<Integer> bst2, Integer k) {
        List<Integer> inorder1 = new ArrayList<>();
        getInorder(bst1.root, inorder1);
        List<Integer> inorder2 = new ArrayList<>();
        getInorder(bst2.root, inorder2);
        List<Integer> counter = Arrays.asList(0);
        getCount(inorder1, inorder2, counter, k);
        return counter.getFirst();
    }

    private static void getCount(List<Integer> inorder1, List<Integer> inorder2, List<Integer> counter, Integer k) {
        int i = inorder1.size() - 1;
        int j = 0;
        while (i >= 0 && j < inorder2.size()) {
            int _sum = inorder1.get(i) + inorder2.get(j);
            if (_sum > k) {
                i -= 1;
            } else if (_sum < k) {
                j += 1;
            } else {
                counter.set(0, counter.getFirst() + 1);
                i -= 1;
                j += 1;
            }
        }
    }

    private static void getInorder(Node<Integer> root, List<Integer> inorder) {
        if (root != null) {
            getInorder(root.left, inorder);
            inorder.add(root.data);
            getInorder(root.right, inorder);
        }
    }
}
