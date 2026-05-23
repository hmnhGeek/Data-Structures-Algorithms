// Problem link - https://www.geeksforgeeks.org/dsa/minimum-swap-required-convert-binary-tree-binary-search-tree/
// Solution - https://www.youtube.com/watch?v=SyIzeO39ZPk
// Solution - https://www.youtube.com/watch?v=-2_c4lG7k_M
// Solution - https://www.youtube.com/watch?v=1BxbBgNSwHo


package BinaryTrees.Problem21;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static Integer getMinSwapsToMakeBst(Node<Integer> root) {
        List<Integer> inorder = new ArrayList<>();
        getInorder(root, inorder);
        return getMinSwapsToSortArray(inorder);
    }

    private static Integer getMinSwapsToSortArray(List<Integer> inorder) {
        List<Point> vector = getVector(inorder);
        vector.sort(null);
        int swapCount = 0;
        for (int i = 0; i < vector.size(); i += 1) {
            Point point = vector.get(i);
            if (point.index == i) continue;
            else {
                swapCount += 1;
                Collections.swap(vector, i, point.index);
                i -= 1;
            }
        }
        return swapCount;
    }

    private static List<Point> getVector(List<Integer> inorder) {
        List<Point> vector = new ArrayList<>();
        for (int i = 0; i < inorder.size(); i += 1) {
            vector.add(new Point(inorder.get(i), i));
        }
        return vector;
    }

    private static void getInorder(Node<Integer> root, List<Integer> inorder) {
        if (root != null) {
            getInorder(root.left, inorder);
            inorder.add(root.data);
            getInorder(root.right, inorder);
        }
    }

    public static void main(String[] args) {
        // Example 1
        Node<Integer> root = new Node<>(5);
        root.left = new Node<>(6);
        root.right = new Node<>(7);
        root.left.left = new Node<>(8);
        root.left.right = new Node<>(9);
        root.right.left = new Node<>(10);
        root.right.right = new Node<>(11);
        System.out.println(getMinSwapsToMakeBst(root));

        // Example 2
        root = new Node<>(2);
        root.left = new Node<>(1);
        root.right = new Node<>(3);
        System.out.println(getMinSwapsToMakeBst(root));
    }
}
