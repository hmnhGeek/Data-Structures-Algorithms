package BinarySearchTrees.Problem13;

import java.util.ArrayList;
import java.util.List;

public class Utility {
    public static <T extends Comparable<T>> T getKthSmallest(BinarySearchTree<T> binarySearchTree, Integer k) {
        List<T> inorder = new ArrayList<>();
        populateInorder(binarySearchTree.getRoot(), inorder);
        if (0 <= k - 1 && k - 1 < inorder.size()) {
            return inorder.get(k - 1);
        }
        return null;
    }

    private static <T extends Comparable<T>> void populateInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            populateInorder(root.getLeft(), inorder);
            inorder.add(root.getData());
            populateInorder(root.getRight(), inorder);
        }
    }
}
