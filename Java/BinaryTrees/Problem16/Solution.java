// Problem link - https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
// Solution - https://www.youtube.com/watch?v=0ca1nvR0be4


package BinaryTrees.Problem16;


import java.util.ArrayList;
import java.util.List;

class TreeNode<T> {
    public T data;
    public TreeNode<T> left;
    public TreeNode<T> right;

    public TreeNode(T data) {
        this.data = data;
        this.left = this.right = null;
    }
}


public class Solution {
    public static void main(String[] args) {
        TreeNode<Integer> n1 = new TreeNode<>(1);
        TreeNode<Integer> n2 = new TreeNode<>(2);
        TreeNode<Integer> n3 = new TreeNode<>(3);
        TreeNode<Integer> n4 = new TreeNode<>(4);
        TreeNode<Integer> n5 = new TreeNode<>(5);
        TreeNode<Integer> n6 = new TreeNode<>(6);
        TreeNode<Integer> n7 = new TreeNode<>(7);
        TreeNode<Integer> n8 = new TreeNode<>(8);
        TreeNode<Integer> n9 = new TreeNode<>(9);
        n1.left = n2;
        n1.right = n3;
        n2.left = n4;
        n2.right = n5;
        n3.left = n6;
        n3.right = n7;
        n5.left = n8;
        n5.right = n9;
        System.out.println(getBoundaryTraversal(n1));

        n1 = new TreeNode<>(1);
        n2 = new TreeNode<>(2);
        n3 = new TreeNode<>(3);
        n4 = new TreeNode<>(4);
        n5 = new TreeNode<>(5);
        n6 = new TreeNode<>(6);
        n7 = new TreeNode<>(7);
        n8 = new TreeNode<>(8);
        n9 = new TreeNode<>(9);
        n1.left = n2;
        n2.left = n4;
        n2.right = n9;
        n4.left = n6;
        n4.right = n5;
        n9.right = n3;
        n3.left = n7;
        n3.right = n8;
        System.out.println(getBoundaryTraversal(n1));

        n1 = new TreeNode<>(1);
        n2 = new TreeNode<>(2);
        n3 = new TreeNode<>(3);
        n4 = new TreeNode<>(4);
        n1.right = n2;
        n2.right = n3;
        n3.right = n4;
        System.out.println(getBoundaryTraversal(n1));

        n1 = new TreeNode<>(1);
        n2 = new TreeNode<>(2);
        n3 = new TreeNode<>(3);
        n4 = new TreeNode<>(4);
        n5 = new TreeNode<>(5);
        n6 = new TreeNode<>(6);
        n7 = new TreeNode<>(7);
        n8 = new TreeNode<>(8);
        n9 = new TreeNode<>(9);
        TreeNode<Integer> n10 = new TreeNode<>(10);
        TreeNode<Integer> n11 = new TreeNode<>(11);
        TreeNode<Integer> n12 = new TreeNode<>(12);
        TreeNode<Integer> n13 = new TreeNode<>(13);
        n1.left = n2;
        n2.left = n4;
        n4.left = n7;
        n5.left = n8;
        n10.left = n12;
        n1.right = n3;
        n3.right = n6;
        n6.right = n10;
        n2.right = n5;
        n5.right = n9;
        n7.right = n11;
        n11.right = n13;
        System.out.println(getBoundaryTraversal(n1));
    }

    public static <T> List<T> getBoundaryTraversal(TreeNode<T> root) {
        /*
            Time complexity is O(n) and space complexity is O(h).
         */
        if (root == null) return new ArrayList<>();
        List<T> traversal = new ArrayList<>();
        traversal.add(root.data);
        traverseLeftBoundary(root.left, traversal);
        traverseLeaves(root, traversal);
        traverseRightBoundary(root.right, traversal);
        return traversal;
    }

    private static <T> void traverseLeftBoundary(TreeNode<T> node, List<T> traversal) {
        if (node == null) return;
        while (node != null) {
            if (node.left == null && node.right == null) return;
            traversal.add(node.data);
            if (node.left != null) {
                node = node.left;
            } else {
                node = node.right;
            }
        }
    }

    private static <T> void traverseLeaves(TreeNode<T> node, List<T> traversal) {
        if (node != null) {
            traverseLeaves(node.left, traversal);
            if (node.left == null && node.right == null) {
                traversal.add(node.data);
            }
            traverseLeaves(node.right, traversal);
        }
    }

    private static <T> void traverseRightBoundary(TreeNode<T> node, List<T> traversal) {
        if (node == null) return;
        Stack<T> stack = new Stack<>();
        while (node != null) {
            if (node.left == null && node.right == null) break;
            stack.push(node.data);
            if (node.right != null) {
                node = node.right;
            } else {
                node = node.left;
            }
        }
        while (!stack.isEmpty()) {
            traversal.add(stack.pop());
        }
    }

}
