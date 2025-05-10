package BinarySearchTrees.Problem11;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        BinarySearchTree<Integer> bst1 = new BinarySearchTree<>();
        for (Integer i : Arrays.asList(100, 50, 300, 20, 70)) {
            bst1.insert(i);
        }
        BinarySearchTree<Integer> bst2 = new BinarySearchTree<>();
        for (Integer i : Arrays.asList(80, 40, 120)) {
            bst2.insert(i);
        }
        BinarySearchTree<Integer> bst = mergeBSTs(bst1, bst2);
        bst.show();
    }

    public static <T extends Comparable<T>> BinarySearchTree<T> mergeBSTs(BinarySearchTree<T> bst1, BinarySearchTree<T> bst2) {
        List<T> inorder1 = getInorder(bst1);
        List<T> inorder2 = getInorder(bst2);
        List<T> inorder = mergeSortedArrays(inorder1, inorder2);
        BinarySearchTree<T> result = new BinarySearchTree<>();
        balancedInsert(result, inorder, 0, inorder.size() - 1);
        return result;
    }

    private static <T extends Comparable<T>> List<T> getInorder(BinarySearchTree<T> bst) {
        Node<T> root = bst.getRoot();
        List<T> inorder = new ArrayList<>();
        getInorder(root, inorder);
        return inorder;
    }

    private static <T extends Comparable<T>> void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.getLeft(), inorder);
            inorder.add(root.getData());
            getInorder(root.getRight(), inorder);
        }
    }

    private static <T extends Comparable<T>> List<T> mergeSortedArrays(List<T> a, List<T> b) {
        int i = 0, j = 0;
        List<T> merged = new ArrayList<>();
        while (i < a.size() && j < b.size()) {
            if (a.get(i).compareTo(b.get(j)) <= 0) {
                merged.add(a.get(i));
                i += 1;
            } else {
                merged.add(b.get(j));
                j += 1;
            }
        }
        while (i < a.size()) {
            merged.add(a.get(i));
            i += 1;
        }
        while (j < b.size()) {
            merged.add(b.get(j));
            j += 1;
        }
        return merged;
    }

    private static <T extends Comparable<T>> void balancedInsert(BinarySearchTree<T> bst, List<T> inorder, Integer low, Integer high) {
        if (low > high) {
            return;
        }
        Integer mid = (low + (high - low)/2);
        bst.insert(inorder.get(mid));
        balancedInsert(bst, inorder, low, mid - 1);
        balancedInsert(bst, inorder, mid + 1, high);
    }
}
