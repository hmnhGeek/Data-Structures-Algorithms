// Problem link - https://www.geeksforgeeks.org/dsa/convert-bst-min-heap/


package PracticeSet1.Heap.Problem15;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        BinarySearchTree<Integer> bst1 = getBst(4, 2, 6, 1, 3, 5, 7);
        convertBstToMinHeap(bst1);
        bst1.show();
    }

    private static <T extends Comparable<T>> BinarySearchTree<T> getBst(T...args) {
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        for (T arg : args) {
            bst.insert(arg);
        }
        return bst;
    }

    public static <T extends Comparable<T>> void convertBstToMinHeap(BinarySearchTree<T> binarySearchTree) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        List<Node<T>> preorder = new ArrayList<>();
        getPreorder(binarySearchTree.root, preorder);

        List<T> inorder = new ArrayList<>();
        getInorder(binarySearchTree.root, inorder);

        int i = 0;
        while (i < preorder.size()) {
            preorder.get(i).data = inorder.get(i);
            i += 1;
        }
    }

    private static <T extends Comparable<T>> void getInorder(Node<T> root, List<T> inorder) {
        if (root != null) {
            getInorder(root.left, inorder);
            inorder.add(root.data);
            getInorder(root.right, inorder);
        }
    }

    private static <T extends Comparable<T>> void getPreorder(Node<T> root, List<Node<T>> preorder) {
        if (root != null) {
            preorder.add(root);
            getPreorder(root.left, preorder);
            getPreorder(root.right, preorder);
        }
    }
}
