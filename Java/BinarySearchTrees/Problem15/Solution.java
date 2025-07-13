package BinarySearchTrees.Problem15;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Integer> bst1 = buildTree(Arrays.asList(6, 3, 8, 1, 4, 7, 9));
        System.out.println(getMedian(bst1));
    }

    private static <T extends Comparable<T>> BinarySearchTree<T> buildTree(List<T> arr) {
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        arr.forEach(bst::insert);
        return bst;
    }

    public static Integer getMedian(BinarySearchTree<Integer> binarySearchTree) {
        List<Integer> inorder = new ArrayList<>();
        getInorder(binarySearchTree.getRoot(), inorder);
        int n = inorder.size();
        if (n % 2 == 0) {
            return (inorder.get(n/2 - 1) + inorder.get(n/2))/2;
        }
        return inorder.get(n/2);
    }

    private static <T extends Comparable<T>> void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.getLeft(), inorder);
            inorder.add(root.getData());
            getInorder(root.getRight(), inorder);
        }
    }
}
