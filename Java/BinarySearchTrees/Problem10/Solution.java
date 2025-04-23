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
    public static void main(String[] args) {
        CustomBinarySearchTree<Integer> bst = new CustomBinarySearchTree<>();
        for (Integer i : Arrays.asList(6,8,4,6,3,8,9,2)) {
            bst.insert(i);
        };
        System.out.println(bst.getInorder());
    }
}
