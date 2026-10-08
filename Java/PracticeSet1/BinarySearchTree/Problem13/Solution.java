package PracticeSet1.BinarySearchTree.Problem13;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        test(Arrays.asList(20, 8, 22, 4, 12, 10, 14), 3);
    }

    private static <T extends Comparable<T>> void test(List<T> arr, int k) {
        BinarySearchTree<T> binarySearchTree = new BinarySearchTree<>();
        for (T x : arr) {
            binarySearchTree.insert(x);
        }
        System.out.println(getKthSmallest(binarySearchTree, k));
    }

    public static <T extends Comparable<T>> T getKthSmallest(BinarySearchTree<T> bst, Integer k) {
        List<T> inorder = new ArrayList<>();
        getInorder(bst.root, inorder);
        return inorder.get(k - 1);
    }

    private static <T extends Comparable<T>> void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.left, inorder);
            inorder.add(root.data);
            getInorder(root.right, inorder);
        }
    }
}
