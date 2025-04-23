package BinarySearchTrees.Problem10;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class CustomBinarySearchTree<T extends Comparable<T>> extends BinarySearchTree<T> {
    public CustomBinarySearchTree() {
        super();
    }

    private void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.getLeft(), inorder);
            inorder.add(root.getData());
            getInorder(root.getRight(), inorder);
        }
    }

    public List<T> getInorder() {
        List<T> inorder = new ArrayList<>();
        getInorder(getRoot(), inorder);
        return inorder;
    }
}

public class Solution {
    private static <T extends Comparable<T>> void balancedInsert(CustomBinarySearchTree<T> bst, List<T> inorder, int low, int high) {
        if (low > high) return;
        int mid = (low + (high - low)/2);
        T data = inorder.get(mid);
        bst.insert(data);
        balancedInsert(bst, inorder, low, mid - 1);
        balancedInsert(bst, inorder, mid + 1, high);
    }

    public static <T extends Comparable<T>> CustomBinarySearchTree<T> getBalancedBst(CustomBinarySearchTree<T> bst) {
        List<T> inorder = bst.getInorder();
        CustomBinarySearchTree<T> balancedBst = new CustomBinarySearchTree<>();
        balancedInsert(balancedBst, inorder, 0, inorder.size() - 1);
        return balancedBst;
    }

    private static <T extends Comparable<T>> CustomBinarySearchTree<T> constructBst(List<T> nodes) {
        CustomBinarySearchTree<T> bst = new CustomBinarySearchTree<>();
        nodes.forEach(bst::insert);
        return bst;
    }

    public static void main(String[] args) {
        // Example 1
        CustomBinarySearchTree<Integer> bst1 = constructBst(Arrays.asList(30, 20, 10));
        bst1.show();
        CustomBinarySearchTree<Integer> balancedBst1 = getBalancedBst(bst1);
        balancedBst1.show();
    }
}
