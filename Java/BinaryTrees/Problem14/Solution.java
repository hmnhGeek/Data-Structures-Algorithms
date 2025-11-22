// # Video - https://www.youtube.com/watch?v=Yt50Jfbd8Po&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=16


package BinaryTrees.Problem14;


import java.util.Arrays;
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
    public static boolean isBalanced(TreeNode<Integer> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        List<Boolean> flag = Arrays.asList(true);
        solve(root, flag);
        return flag.getFirst();
    }

    private static Integer solve(TreeNode<Integer> root, List<Boolean> flag) {
        if (root == null) return 0;
        Integer leftHeight = solve(root.left, flag);
        Integer rightHeight = solve(root.right, flag);
        if (Math.abs(rightHeight - leftHeight) > 1) {
            flag.set(0, false);
        }
        return 1 + Math.max(leftHeight, rightHeight);
    }

    public static void main(String[] args) {

        // -------- Example 1 --------
        TreeNode<Integer> n3 = new TreeNode<>(3);
        TreeNode<Integer> n9 = new TreeNode<>(9);
        TreeNode<Integer> n20 = new TreeNode<>(20);
        TreeNode<Integer> n15 = new TreeNode<>(15);
        TreeNode<Integer> n7 = new TreeNode<>(7);

        n3.left = n9;
        n3.right = n20;
        n20.left = n15;
        n20.right = n7;

        System.out.println(Solution.isBalanced(n3));


        // -------- Example 2 --------
        TreeNode<Integer> e1 = new TreeNode<>(1);
        TreeNode<Integer> e2 = new TreeNode<>(2);
        TreeNode<Integer> e3 = new TreeNode<>(3);
        TreeNode<Integer> e4 = new TreeNode<>(4);
        TreeNode<Integer> e5 = new TreeNode<>(5);
        TreeNode<Integer> e6 = new TreeNode<>(6);
        TreeNode<Integer> e7 = new TreeNode<>(7);

        e1.left = e3;
        e3.left = e5;
        e3.right = e4;
        e5.left = e7;
        e5.right = e6;
        e1.right = e2;

        System.out.println(Solution.isBalanced(e1));


        // -------- Example 3 --------
        TreeNode<Integer> a1 = new TreeNode<>(1);
        TreeNode<Integer> a2 = new TreeNode<>(2);
        TreeNode<Integer> a3 = new TreeNode<>(3);
        TreeNode<Integer> a4 = new TreeNode<>(4);
        TreeNode<Integer> a5 = new TreeNode<>(5);

        a1.left = a2;
        a2.left = a4;
        a2.right = a5;
        a1.right = a3;

        System.out.println(Solution.isBalanced(a1));


        // -------- Example 4 --------
        TreeNode<Integer> b1 = new TreeNode<>(1);
        TreeNode<Integer> b2 = new TreeNode<>(2);
        TreeNode<Integer> b3 = new TreeNode<>(3);
        TreeNode<Integer> b4 = new TreeNode<>(4);
        TreeNode<Integer> b5 = new TreeNode<>(5);
        TreeNode<Integer> b6 = new TreeNode<>(6);
        TreeNode<Integer> b7 = new TreeNode<>(7);
        TreeNode<Integer> b8 = new TreeNode<>(8);
        TreeNode<Integer> b9 = new TreeNode<>(9);

        b1.left = b2;
        b2.left = b4;
        b2.right = b5;
        b5.left = b8;

        b1.right = b3;
        b3.left = b6;
        b3.right = b9;
        b6.right = b7;

        System.out.println(Solution.isBalanced(b1));
    }
}
