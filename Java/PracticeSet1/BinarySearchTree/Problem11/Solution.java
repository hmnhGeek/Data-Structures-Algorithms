package PracticeSet1.BinarySearchTree.Problem11;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
    }

    public static <T extends Comparable<T>> BinarySearchTree<T> mergeBSTs(BinarySearchTree<T> bst1, BinarySearchTree<T> bst2) {
        List<T> inorder1 = new ArrayList<>(), inorder2 = new ArrayList<>();
        getInorder(bst1.root, inorder1);
        getInorder(bst2.root, inorder2);
        List<T> inorder = merge(inorder1, inorder2);
        BinarySearchTree<T> balancedMergedTree = new BinarySearchTree<>();
        constructBalancedBst(balancedMergedTree, inorder, 0, inorder.size() - 1);
        return balancedMergedTree;
    }

    private static <T extends Comparable<T>> void constructBalancedBst(BinarySearchTree<T> balancedMergedTree, List<T> inorder, int low, int high) {
        if (low > high) return;
        int mid = (low + (high - low)/2);
        balancedMergedTree.insert(inorder.get(mid));
        constructBalancedBst(balancedMergedTree, inorder, low, mid - 1);
        constructBalancedBst(balancedMergedTree, inorder, mid + 1, high);
    }

    private static <T extends Comparable<T>> List<T> merge(List<T> inorder1, List<T> inorder2) {
        List<T> merged = new ArrayList<>();
        int i = 0, j = 0;
        while (i < inorder1.size() && j < inorder2.size()) {
            if (inorder1.get(i).compareTo(inorder2.get(j)) <= 0) {
                merged.add(inorder1.get(i));
                i += 1;
            } else {
                merged.add(inorder2.get(j));
                j += 1;
            }
        }
        while (i < inorder1.size()) {
            merged.add(inorder1.get(i));
            i += 1;
        }
        while (j < inorder2.size()) {
            merged.add(inorder2.get(j));
            j += 1;
        }
        return merged;
    }

    private static <T extends Comparable<T>> void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.left, inorder);
            inorder.add(root.data);
            getInorder(root.right, inorder);
        }
    }
}
