package BinaryTrees.Problem12;


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
    public T data;
    public Integer level;

    public Element(T data, Integer level) {
        this.data = data;
        this.level = level;
    }
}


public class Solution {
    public static <T> List<T> getBottomView(TreeNode<T> root) {
        Stack<Element<TreeNode<T>>> stack = new Stack<>();
        stack.push(new Element<>(root, 0));
        List<T> result = new ArrayList<>();
        int mini = Integer.MAX_VALUE, maxi = Integer.MIN_VALUE;
        Map<Integer, T> d = new HashMap<>();

        while (!stack.isEmpty()) {
            Element<TreeNode<T>> element = stack.pop();
            mini = Math.min(mini, element.level);
            maxi = Math.max(maxi, element.level);
            d.put(element.level, element.data.data);

            if (element.data.left != null) {
                stack.push(new Element<>(element.data.left, element.level - 1));
            }

            if (element.data.right != null) {
                stack.push(new Element<>(element.data.right, element.level + 1));
            }
        }

        for (int i = mini; i <= maxi; i += 1) {
            result.add(d.get(i));
        }
        return result;
    }

    public static void main(String[] args) {
        // Example 1
        TreeNode<Integer> ex1n20 = new TreeNode<>(20);
        TreeNode<Integer> ex1n8 = new TreeNode<>(8);
        TreeNode<Integer> ex1n22 = new TreeNode<>(22);
        TreeNode<Integer> ex1n5 = new TreeNode<>(5);
        TreeNode<Integer> ex1n3 = new TreeNode<>(3);
        TreeNode<Integer> ex1n4 = new TreeNode<>(4);
        TreeNode<Integer> ex1n25 = new TreeNode<>(25);
        TreeNode<Integer> ex1n10 = new TreeNode<>(10);
        TreeNode<Integer> ex1n14 = new TreeNode<>(14);

        ex1n20.left = ex1n8;
        ex1n20.right = ex1n22;
        ex1n8.left = ex1n5;
        ex1n8.right = ex1n3;
        ex1n3.left = ex1n10;
        ex1n22.left = ex1n4;
        ex1n22.right = ex1n25;
        ex1n4.right = ex1n14;

        System.out.println(Solution.getBottomView(ex1n20));


        // Example 2
        TreeNode<Integer> ex2n1 = new TreeNode<>(1);
        TreeNode<Integer> ex2n2 = new TreeNode<>(2);
        TreeNode<Integer> ex2n3 = new TreeNode<>(3);

        ex2n1.left = ex2n2;
        ex2n1.right = ex2n3;

        System.out.println(Solution.getBottomView(ex2n1));


        // Example 3
        TreeNode<Integer> ex3n10 = new TreeNode<>(10);
        TreeNode<Integer> ex3n20 = new TreeNode<>(20);
        TreeNode<Integer> ex3n30 = new TreeNode<>(30);
        TreeNode<Integer> ex3n40 = new TreeNode<>(40);
        TreeNode<Integer> ex3n60 = new TreeNode<>(60);

        ex3n10.left = ex3n20;
        ex3n10.right = ex3n30;
        ex3n20.left = ex3n40;
        ex3n20.right = ex3n60;

        System.out.println(Solution.getBottomView(ex3n10));


        // Example 4
        TreeNode<Integer> ex4n1 = new TreeNode<>(1);
        TreeNode<Integer> ex4n2 = new TreeNode<>(2);

        ex4n1.left = ex4n2;

        System.out.println(Solution.getBottomView(ex4n1));


        // Example 5
        TreeNode<Integer> ex5n1 = new TreeNode<>(1);
        TreeNode<Integer> ex5n2 = new TreeNode<>(2);
        TreeNode<Integer> ex5n3 = new TreeNode<>(3);
        TreeNode<Integer> ex5n4 = new TreeNode<>(4);
        TreeNode<Integer> ex5n5 = new TreeNode<>(5);
        TreeNode<Integer> ex5n6 = new TreeNode<>(6);

        ex5n1.left = ex5n2;
        ex5n1.right = ex5n3;
        ex5n2.left = ex5n4;
        ex5n2.right = ex5n5;
        ex5n3.right = ex5n6;

        System.out.println(Solution.getBottomView(ex5n1));


        // Example 6
        TreeNode<Integer> ex6n1 = new TreeNode<>(1);
        TreeNode<Integer> ex6n2 = new TreeNode<>(2);
        TreeNode<Integer> ex6n3 = new TreeNode<>(3);
        TreeNode<Integer> ex6n4 = new TreeNode<>(4);
        TreeNode<Integer> ex6n5 = new TreeNode<>(5);
        TreeNode<Integer> ex6n6 = new TreeNode<>(6);
        TreeNode<Integer> ex6n9 = new TreeNode<>(9);
        TreeNode<Integer> ex6n10 = new TreeNode<>(10);
        TreeNode<Integer> ex6n11 = new TreeNode<>(11);

        ex6n1.left = ex6n2;
        ex6n1.right = ex6n3;
        ex6n2.left = ex6n4;
        ex6n2.right = ex6n10;
        ex6n4.right = ex6n5;
        ex6n5.right = ex6n6;
        ex6n3.left = ex6n9;
        ex6n3.right = ex6n11;

        System.out.println(Solution.getBottomView(ex6n1));


        // Example 7
        TreeNode<Integer> ex7n2 = new TreeNode<>(2);
        TreeNode<Integer> ex7n7 = new TreeNode<>(7);
        TreeNode<Integer> ex7n5 = new TreeNode<>(5);
        TreeNode<Integer> ex7n21 = new TreeNode<>(2);
        TreeNode<Integer> ex7n6 = new TreeNode<>(6);
        TreeNode<Integer> ex7n9 = new TreeNode<>(9);
        TreeNode<Integer> ex7n11 = new TreeNode<>(11);
        TreeNode<Integer> ex7n4 = new TreeNode<>(4);
        TreeNode<Integer> ex7n51 = new TreeNode<>(5);

        ex7n2.left = ex7n7;
        ex7n2.right = ex7n5;
        ex7n7.left = ex7n21;
        ex7n7.right = ex7n6;
        ex7n6.left = ex7n51;
        ex7n6.right = ex7n11;
        ex7n5.right = ex7n9;
        ex7n9.left = ex7n4;

        System.out.println(Solution.getBottomView(ex7n2));
    }
}
