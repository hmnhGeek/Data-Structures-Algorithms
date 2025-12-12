package BinaryTrees.Problem15;


import com.sun.source.tree.Tree;

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

        // --------------------- Example 1 ---------------------
        TreeNode<Integer> n8 = new TreeNode<>(8);
        TreeNode<Integer> n3 = new TreeNode<>(3);
        TreeNode<Integer> n10 = new TreeNode<>(10);
        TreeNode<Integer> n1 = new TreeNode<>(1);
        TreeNode<Integer> n6 = new TreeNode<>(6);
        TreeNode<Integer> n14 = new TreeNode<>(14);
        TreeNode<Integer> n4 = new TreeNode<>(4);
        TreeNode<Integer> n7 = new TreeNode<>(7);
        TreeNode<Integer> n13 = new TreeNode<>(13);

        n8.left = n3;
        n8.right = n10;
        n3.left = n1;
        n3.right = n6;
        n10.right = n14;
        n6.left = n4;
        n6.right = n7;
        n14.left = n13;

        System.out.println("Example 1: " + Solution.diagonalTraversal(n8));


        // --------------------- Example 2 ---------------------
        TreeNode<Integer> e1 = new TreeNode<>(1);
        TreeNode<Integer> e2 = new TreeNode<>(2);
        TreeNode<Integer> e3 = new TreeNode<>(3);
        TreeNode<Integer> e4 = new TreeNode<>(4);
        TreeNode<Integer> e5 = new TreeNode<>(5);
        TreeNode<Integer> e6 = new TreeNode<>(6);
        TreeNode<Integer> e7 = new TreeNode<>(7);
        TreeNode<Integer> e8 = new TreeNode<>(8);
        TreeNode<Integer> e9 = new TreeNode<>(9);

        e1.left = e2;
        e1.right = e3;
        e2.left = e4;
        e2.right = e5;
        e3.right = e6;
        e4.left = e7;
        e4.right = e8;
        e6.left = e9;

        System.out.println("Example 2: " + Solution.diagonalTraversal(e1));


        // --------------------- Example 3 ---------------------
        TreeNode<Integer> f1 = new TreeNode<>(1);
        TreeNode<Integer> f2 = new TreeNode<>(2);
        TreeNode<Integer> f3 = new TreeNode<>(3);
        TreeNode<Integer> f4 = new TreeNode<>(4);
        TreeNode<Integer> f5 = new TreeNode<>(5);
        TreeNode<Integer> f6 = new TreeNode<>(6);

        f1.left = f2;
        f1.right = f3;
        f2.left = f4;
        f3.left = f5;
        f3.right = f6;

        System.out.println("Example 3: " + Solution.diagonalTraversal(f1));


        // --------------------- Example 4 ---------------------
        TreeNode<Integer> g1 = new TreeNode<>(1);
        TreeNode<Integer> g2 = new TreeNode<>(2);
        TreeNode<Integer> g3 = new TreeNode<>(3);
        TreeNode<Integer> g4 = new TreeNode<>(4);
        TreeNode<Integer> g5 = new TreeNode<>(5);
        TreeNode<Integer> g6 = new TreeNode<>(6);
        TreeNode<Integer> g7 = new TreeNode<>(7);

        g1.left = g2;
        g1.right = g3;
        g2.left = g4;
        g2.right = g5;
        g3.left = g6;
        g3.right = g7;

        System.out.println("Example 4: " + Solution.diagonalTraversal(g1));


        // --------------------- Example 5 ---------------------
        TreeNode<Integer> h1 = new TreeNode<>(1);
        TreeNode<Integer> h2 = new TreeNode<>(2);
        TreeNode<Integer> h3 = new TreeNode<>(3);
        TreeNode<Integer> h4 = new TreeNode<>(4);
        TreeNode<Integer> h5 = new TreeNode<>(5);

        h1.left = h2;
        h1.right = h3;
        h3.left = h4;
        h3.right = h5;

        System.out.println("Example 5: " + Solution.diagonalTraversal(h1));


        // --------------------- Example 6 ---------------------
        TreeNode<Integer> k1 = new TreeNode<>(1);
        TreeNode<Integer> k2 = new TreeNode<>(2);
        TreeNode<Integer> k3 = new TreeNode<>(3);
        TreeNode<Integer> k4 = new TreeNode<>(4);
        TreeNode<Integer> k5 = new TreeNode<>(5);
        TreeNode<Integer> k6 = new TreeNode<>(6);
        TreeNode<Integer> k7 = new TreeNode<>(7);
        TreeNode<Integer> k8 = new TreeNode<>(8);
        TreeNode<Integer> k9 = new TreeNode<>(9);
        TreeNode<Integer> k10 = new TreeNode<>(10);
        TreeNode<Integer> k11 = new TreeNode<>(11);

        k1.left = k2;
        k1.right = k7;
        k2.left = k3;
        k7.right = k8;
        k3.right = k4;
        k8.left = k9;
        k4.left = k5;
        k4.right = k6;
        k9.left = k10;
        k9.right = k11;

        System.out.println("Example 6: " + Solution.diagonalTraversal(k1));
    }

    public static <T> List<T> diagonalTraversal(TreeNode<T> root) {
        if (root == null) return new ArrayList<>();
        List<T> result = new ArrayList<>();
        Queue<TreeNode<T>> queue = new Queue<>();
        while (root != null) {
            queue.push(root);
            root = root.right;
        }
        while (!queue.isEmpty()) {
            TreeNode<T> node = queue.pop();
            result.add(node.data);
            TreeNode<T> nextNode = node.left;
            while (nextNode != null) {
                queue.push(nextNode);
                nextNode = nextNode.right;
            }
        }
        return result;
    }
}
