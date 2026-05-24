package PracticeSet1.BinarySearchTree.Problem7;

import java.util.Objects;

public class Solution {
    public static void main(String[] args) {
        System.out.println(run(7, 8, 5, 4, 6, 3, 7, 8));
        System.out.println(run(8, 14, 20, 8, 22, 4, 12, 10, 14));
        System.out.println(run(1, 3, 2, 1, 3));
    }

    public static Integer run(Integer n1, Integer n2, Integer ... args) {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (Integer i : args) {
            bst.insert(i);
        }
        return getLca(bst, n1, n2);
    }

    public static Integer getLca(BinarySearchTree<Integer> bst, Integer n1, Integer n2) {
        return getLca(bst.root, n1, n2);
    }

    private static Integer getLca(Node<Integer> root, Integer n1, Integer n2) {
        if (root == null) {
            return null;
        }
        if (Objects.equals(root.data, n1) || Objects.equals(root.data, n2)) {
            return root.data;
        }
        Integer left = getLca(root.left, n1, n2);
        Integer right = getLca(root.right, n1, n2);
        if (left == null && right == null) {
            return null;
        }
        if (left == null) return right;
        if (right == null) return left;
        return root.data;
    }
}
