package BinarySearchTrees.Problem21;


class Element {
    public Integer minValue;
    public Integer maxValue;
    public Integer size;

    public Element(Integer minValue, Integer maxValue, Integer size) {
        this.minValue = minValue;
        this.maxValue = maxValue;
        this.size = size;
    }
}


public class Solution {
    public static Integer getLargestBst(TreeNode<Integer> root) {
        return solve(root).size;
    }

    private static Element solve(TreeNode<Integer> root) {
        if (root == null) {
            return new Element(Integer.MAX_VALUE, Integer.MIN_VALUE, 0);
        }
        Element left = solve(root.left);
        Element right = solve(root.right);
        if (left.maxValue <= root.data && root.data <= right.minValue) {
            return new Element(
                    Math.min(left.minValue, root.data),
                    Math.max(right.maxValue, root.data),
                    left.size + right.size + 1
            );
        }
        return new Element(Integer.MIN_VALUE, Integer.MAX_VALUE, Math.max(left.size, right.size));
    }

    public static void main(String[] args) {
        TreeNode<Integer> n20 = new TreeNode<>(20);
        TreeNode<Integer> n15 = new TreeNode<>(15);
        TreeNode<Integer> n40 = new TreeNode<>(40);
        TreeNode<Integer> n14 = new TreeNode<>(14);
        TreeNode<Integer> n18 = new TreeNode<>(18);
        TreeNode<Integer> n30 = new TreeNode<>(30);
        TreeNode<Integer> n60 = new TreeNode<>(60);
        TreeNode<Integer> n17 = new TreeNode<>(17);
        TreeNode<Integer> n16 = new TreeNode<>(16);
        TreeNode<Integer> n19 = new TreeNode<>(19);
        TreeNode<Integer> n50 = new TreeNode<>(50);

        n20.left = n15;
        n15.left = n14;
        n18.left = n16;
        n40.left = n30;
        n60.left = n50;

        n20.right = n40;
        n40.right = n60;
        n15.right = n18;
        n18.right = n19;
        n14.right = n17;

        System.out.println(Solution.getLargestBst(n20));


        TreeNode<Integer> n10 = new TreeNode<>(10);
        TreeNode<Integer> n5 = new TreeNode<>(5);
        TreeNode<Integer> n_15 = new TreeNode<>(15);
        TreeNode<Integer> n1 = new TreeNode<>(1);
        TreeNode<Integer> n8 = new TreeNode<>(8);
        TreeNode<Integer> n7 = new TreeNode<>(7);

        n10.left = n5;
        n5.left = n1;
        n5.right = n8;

        n10.right = n_15;
        n_15.right = n7;

        System.out.println(Solution.getLargestBst(n10));
    }
}
