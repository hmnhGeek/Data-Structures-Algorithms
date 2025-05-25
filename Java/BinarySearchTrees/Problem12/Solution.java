// Problem link - https://www.geeksforgeeks.org/problems/kth-largest-element-in-bst/1


package BinarySearchTrees.Problem12;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        BinarySearchTree<Integer> binarySearchTree1 = buildBst(Arrays.asList(2, 4, 9));
        System.out.println(getKthLargest(binarySearchTree1, 3));
        System.out.println(getKthLargest(binarySearchTree1, 2));

        BinarySearchTree<Integer> binarySearchTree2 = buildBst(Arrays.asList(9, 10));
        System.out.println(getKthLargest(binarySearchTree2, 1));

        BinarySearchTree<Integer> binarySearchTree3 = buildBst(Arrays.asList(6, 2, 7, 3, 4, 9));
        System.out.println(getKthLargest(binarySearchTree3, 5));
    }

    private static List<Integer> getInorder(BinarySearchTree<Integer> binarySearchTree) {
        Node<Integer> root = binarySearchTree.getRoot();
        List<Integer> inorder = new ArrayList<>();
        getInorder(root, inorder);
        return inorder;
    }

    private static void getInorder(Node<Integer> root, List<Integer> inorder) {
        if (root != null) {
            getInorder(root.getLeft(), inorder);
            inorder.add(root.getData());
            getInorder(root.getRight(), inorder);
        }
    }

    public static Integer getKthLargest(BinarySearchTree<Integer> binarySearchTree, int k) {
        /*
            Time complexity is O(n) and space complexity is O(log(n)).
         */
        List<Integer> inorder = getInorder(binarySearchTree);
        return inorder.get(inorder.size() - k);
    }

    public static BinarySearchTree<Integer> buildBst(List<Integer> levelOrder) {
        BinarySearchTree<Integer> binarySearchTree = new BinarySearchTree<>();
        for (Integer i : levelOrder) {
            binarySearchTree.insert(i);
        }
        return binarySearchTree;
    }
}
