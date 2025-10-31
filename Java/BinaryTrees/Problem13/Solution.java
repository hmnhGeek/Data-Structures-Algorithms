package BinaryTrees.Problem13;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class TreeNode<T> {
    public T data;
    public TreeNode<T> left;
    public TreeNode<T> right;

    public TreeNode(T data) {
        this.data = data;
        this.left = this.right = null;
    }
}


class Element<T> {
    public TreeNode<T> treeNode;
    public Integer level;

    public Element(TreeNode<T> treeNode, Integer level) {
        this.treeNode = treeNode;
        this.level = level;
    }
}


public class Solution {
    public static void main(String[] args) {
        // Example 1
        TreeNode<Integer> ex1_n5 = new TreeNode<>(5);
        TreeNode<Integer> ex1_n1 = new TreeNode<>(1);
        TreeNode<Integer> ex1_n9 = new TreeNode<>(9);
        TreeNode<Integer> ex1_n3 = new TreeNode<>(3);
        TreeNode<Integer> ex1_n2 = new TreeNode<>(2);
        TreeNode<Integer> ex1_n8 = new TreeNode<>(8);
        TreeNode<Integer> ex1_n4 = new TreeNode<>(4);

        ex1_n5.left = ex1_n1;
        ex1_n5.right = ex1_n9;
        ex1_n1.left = ex1_n3;
        ex1_n1.right = ex1_n2;
        ex1_n9.left = ex1_n8;
        ex1_n9.right = ex1_n4;

        System.out.println("Example 1 Zig-Zag Traversal: " + zigZagTraversal(ex1_n5));


        // Example 2
        TreeNode<Integer> ex2_n7 = new TreeNode<>(7);
        TreeNode<Integer> ex2_n9 = new TreeNode<>(9);
        TreeNode<Integer> ex2_n71 = new TreeNode<>(7);
        TreeNode<Integer> ex2_n8 = new TreeNode<>(8);
        TreeNode<Integer> ex2_n81 = new TreeNode<>(8);
        TreeNode<Integer> ex2_n6 = new TreeNode<>(6);
        TreeNode<Integer> ex2_n10 = new TreeNode<>(10);
        TreeNode<Integer> ex2_n91 = new TreeNode<>(9);

        ex2_n7.left = ex2_n9;
        ex2_n7.right = ex2_n71;
        ex2_n9.left = ex2_n8;
        ex2_n9.right = ex2_n81;
        ex2_n71.left = ex2_n6;
        ex2_n8.left = ex2_n10;
        ex2_n8.right = ex2_n91;

        System.out.println("Example 2 Zig-Zag Traversal: " + zigZagTraversal(ex2_n7));


        // Example 3
        TreeNode<Integer> ex3_n1 = new TreeNode<>(1);
        TreeNode<Integer> ex3_n2 = new TreeNode<>(2);
        TreeNode<Integer> ex3_n3 = new TreeNode<>(3);
        TreeNode<Integer> ex3_n4 = new TreeNode<>(4);
        TreeNode<Integer> ex3_n5 = new TreeNode<>(5);
        TreeNode<Integer> ex3_n6 = new TreeNode<>(6);
        TreeNode<Integer> ex3_n7 = new TreeNode<>(7);

        ex3_n1.left = ex3_n2;
        ex3_n1.right = ex3_n3;
        ex3_n2.left = ex3_n4;
        ex3_n2.right = ex3_n5;
        ex3_n3.left = ex3_n6;
        ex3_n3.right = ex3_n7;

        System.out.println("Example 3 Zig-Zag Traversal: " + zigZagTraversal(ex3_n1));
    }

    public static <T> List<T> zigZagTraversal(TreeNode<T> root) {
        Map<Integer, List<T>> levels = new HashMap<>();
        Queue<Element<T>> queue = new Queue<>();
        queue.push(new Element<>(root, 0));
        while (!queue.isEmpty()) {
            Element<T> element = queue.pop();
            TreeNode<T> node = element.treeNode;
            Integer level = element.level;
            levels.putIfAbsent(level, new ArrayList<>());
            levels.get(level).add(node.data);
            if (node.left != null) {
                queue.push(new Element<>(node.left, level + 1));
            }
            if (node.right != null) {
                queue.push(new Element<>(node.right, level + 1));
            }
        }
        boolean leftToRight = true;
        int i = 0;
        List<T> result = new ArrayList<>();
        List<T> tempList;
        while (levels.containsKey(i)) {
            tempList = levels.get(i);
            if (!leftToRight) {
                tempList = tempList.reversed();
            }
            result.addAll(tempList);
            i += 1;
            leftToRight = !leftToRight;
        }
        return result;
    }
}
