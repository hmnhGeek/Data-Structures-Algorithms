package PracticeSet1.BinarySearchTree.Problem9;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
    }

    public static <T extends Comparable<T>> void convertToBst(Node<T> root) {
        List<T> inorder = new ArrayList<>();
        List<Node<T>> nodeInorder = new ArrayList<>();
        populateInorder(root, inorder, nodeInorder);
        QuickSort.sort(inorder);
        for (int i = 0; i < inorder.size(); i += 1) {
            nodeInorder.get(i).data = inorder.get(i);
        }
    }

    private static <T extends Comparable<T>> void populateInorder(Node<T> root, List<T> inorder, List<Node<T>> nodeInorder) {
        if (root != null)  {
            populateInorder(root.left, inorder, nodeInorder);
            inorder.add(root.data);
            nodeInorder.add(root);
            populateInorder(root.right, inorder, nodeInorder);
        }
    }
}
