// Problem link - https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
// Solution - https://www.youtube.com/watch?v=Et9OCDNvJ78&t=206s

package BinaryTrees.Problem11;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        // First tree
        TreeNode<Integer> n1 = new TreeNode<>(1);
        TreeNode<Integer> n2 = new TreeNode<>(2);
        TreeNode<Integer> n3 = new TreeNode<>(3);
        TreeNode<Integer> n4 = new TreeNode<>(4);
        TreeNode<Integer> n5 = new TreeNode<>(5);
        TreeNode<Integer> n6 = new TreeNode<>(6);
        TreeNode<Integer> n7 = new TreeNode<>(7);

        n1.left = n2;
        n1.right = n3;
        n2.left = n4;
        n2.right = n5;
        n5.left = n6;
        n3.right = n7;
        Solution.getTopView(n1);

        // Second tree
        TreeNode<Integer> n10 = new TreeNode<>(10);
        TreeNode<Integer> n20 = new TreeNode<>(20);
        TreeNode<Integer> n30 = new TreeNode<>(30);
        TreeNode<Integer> n40 = new TreeNode<>(40);
        TreeNode<Integer> n60 = new TreeNode<>(60);
        TreeNode<Integer> n90 = new TreeNode<>(90);
        TreeNode<Integer> n100 = new TreeNode<>(100);

        n10.left = n20;
        n10.right = n30;
        n20.left = n40;
        n20.right = n60;
        n30.left = n90;
        n30.right = n100;
        Solution.getTopView(n10);

        // Third tree
        TreeNode<Integer> t1 = new TreeNode<>(1);
        TreeNode<Integer> t2 = new TreeNode<>(2);
        TreeNode<Integer> t3 = new TreeNode<>(3);
        TreeNode<Integer> t4 = new TreeNode<>(4);
        TreeNode<Integer> t5 = new TreeNode<>(5);
        TreeNode<Integer> t6 = new TreeNode<>(6);

        t1.left = t2;
        t1.right = t3;
        t2.right = t4;
        t4.right = t5;
        t5.right = t6;
        Solution.getTopView(t1);

        // Fourth tree
        TreeNode<Integer> f1 = new TreeNode<>(1);
        TreeNode<Integer> f2 = new TreeNode<>(2);
        TreeNode<Integer> f3 = new TreeNode<>(3);
        TreeNode<Integer> f4 = new TreeNode<>(4);
        TreeNode<Integer> f5 = new TreeNode<>(5);
        TreeNode<Integer> f6 = new TreeNode<>(6);
        TreeNode<Integer> f9 = new TreeNode<>(9);
        TreeNode<Integer> f10 = new TreeNode<>(10);
        TreeNode<Integer> f11 = new TreeNode<>(11);

        f1.left = f2;
        f1.right = f3;
        f2.left = f4;
        f2.right = f10;
        f4.right = f5;
        f5.right = f6;
        f3.left = f9;
        f3.right = f11;
        Solution.getTopView(f1);
    }

    public static <T> void getTopView(TreeNode<T> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Map<Integer, T> d = new HashMap<>();
        Integer leftMostLevel = Integer.MAX_VALUE, rightMostLevel = Integer.MIN_VALUE;
        Queue<Element<TreeNode<T>>> queue = new Queue<>();
        queue.push(new Element<>(root, 0));
        while (!queue.isEmpty()) {
            Element<TreeNode<T>> element = queue.pop();
            TreeNode<T> node = element.data;
            Integer level = element.level;
            if (!d.containsKey(level)) {
                d.put(level, node.data);
            }
            leftMostLevel = Math.min(level, leftMostLevel);
            rightMostLevel = Math.max(level, rightMostLevel);
            if (node.left != null) {
                queue.push(new Element<>(node.left, level - 1));
            }
            if (node.right != null) {
                queue.push(new Element<>(node.right, level + 1));
            }
        }
        List<T> result = new ArrayList<>();
        for (int i = leftMostLevel; i <= rightMostLevel; i += 1) {
            result.add(d.get(i));
        }
        System.out.println(result);
        System.out.println();
    }
}
