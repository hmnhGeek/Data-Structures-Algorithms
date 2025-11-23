// Problem link - https://www.geeksforgeeks.org/problems/is-binary-tree-heap/1
// Solution - https://www.youtube.com/watch?v=jX-UP7b2bkk


package Heap.Problem13;


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
    public static boolean isHeap(TreeNode<Integer> root) {
        // in O(n) time and O(n) space, count the number of nodes in the tree.
        Integer numNodes = getNumberOfNodesInTree(root);

        // if the tree is empty, it's a max heap already.
        if (root == null) return true;

        // otherwise, check if the tree is complete binary tree and also follows the max heap property.
        return isCompleteBinaryTree(root, 0, numNodes) && isMaxHeap(root);
    }

    /**
     *
     * @param root Node from the binary tree
     * @return True if the max heap property is satisfied, else returns false.
     */
    private static boolean isMaxHeap(TreeNode<Integer> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */

        // A null node is always following the max heap property.
        if (root == null) return true;

        // if either the left or the right child is greater than the root, return false.
        if (root.left != null && root.left.data > root.data) return false;
        if (root.right != null && root.right.data > root.data) return false;

        // return true if the left and right subtrees follow max heap property together.
        return isMaxHeap(root.left) && isMaxHeap(root.right);
    }

    /**
     *
     * @param root Root node of the binary tree.
     * @return The count of the nodes in the tree.
     */
    private static Integer getNumberOfNodesInTree(TreeNode<Integer> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        if (root == null) return 0;
        return 1 + getNumberOfNodesInTree(root.left) + getNumberOfNodesInTree(root.right);
    }

    /**
     *
     * @param root The root node of the binary tree.
     * @param i Corresponds to hypothetical index of the node in its level order traversal.
     * @param numNodes The total nodes in the overall binary tree.
     * @return True if the binary tree at root node is complete, else returns false.
     */
    private static boolean isCompleteBinaryTree(TreeNode<Integer> root, int i, Integer numNodes) {
        // A null node is always complete.
        if (root == null) return true;

        // at any point, if the index + 1 (the position of node in 1-based indexing, which will correspond to the
        // 1-based indexed count from the original tree) of the root node becomes larger than the total number of nodes
        // then it is an incomplete binary tree.
        if (i + 1 > numNodes) return false;

        // both left and right subtrees should be complete.
        return isCompleteBinaryTree(root.left, 2*i + 1, numNodes) && isCompleteBinaryTree(root.right, 2*i + 2, numNodes);
    }

    public static void main(String[] args) {
        // Example 1
        TreeNode<Integer> n10_e1 = new TreeNode<>(10);
        TreeNode<Integer> n20_e1 = new TreeNode<>(20);
        TreeNode<Integer> n30_e1 = new TreeNode<>(30);
        TreeNode<Integer> n40_e1 = new TreeNode<>(40);
        TreeNode<Integer> n60_e1 = new TreeNode<>(60);

        n10_e1.left = n20_e1;
        n10_e1.right = n30_e1;
        n20_e1.left = n40_e1;
        n20_e1.right = n60_e1;

        System.out.println(Solution.isHeap(n10_e1));


        // Example 2
        TreeNode<Integer> n5_e2 = new TreeNode<>(5);
        TreeNode<Integer> n2_e2 = new TreeNode<>(2);
        TreeNode<Integer> n3_e2 = new TreeNode<>(3);

        n5_e2.left = n2_e2;
        n5_e2.right = n3_e2;

        System.out.println(Solution.isHeap(n5_e2));


        // Example 3
        TreeNode<Integer> n40_e3 = new TreeNode<>(40);
        TreeNode<Integer> n36_e3 = new TreeNode<>(36);
        TreeNode<Integer> n23_e3 = new TreeNode<>(23);
        TreeNode<Integer> n10_e3 = new TreeNode<>(10);
        TreeNode<Integer> n23b_e3 = new TreeNode<>(23);
        TreeNode<Integer> n5_e3 = new TreeNode<>(5);
        TreeNode<Integer> n6_e3 = new TreeNode<>(6);
        TreeNode<Integer> n1_e3 = new TreeNode<>(1);
        TreeNode<Integer> n14_e3 = new TreeNode<>(14);

        n40_e3.left = n36_e3;
        n40_e3.right = n23_e3;
        n36_e3.left = n10_e3;
        n36_e3.right = n23b_e3;
        n23_e3.left = n5_e3;
        n23_e3.right = n6_e3;
        n10_e3.left = n1_e3;
        n10_e3.right = n14_e3;

        System.out.println(Solution.isHeap(n40_e3));


        // Example 4
        TreeNode<Integer> n40_e4 = new TreeNode<>(40);
        TreeNode<Integer> n36_e4 = new TreeNode<>(36);
        TreeNode<Integer> n23_e4 = new TreeNode<>(23);
        TreeNode<Integer> n10_e4 = new TreeNode<>(10);
        TreeNode<Integer> n5_e4 = new TreeNode<>(5);
        TreeNode<Integer> n6_e4 = new TreeNode<>(6);
        TreeNode<Integer> n1_e4 = new TreeNode<>(1);
        TreeNode<Integer> n14_e4 = new TreeNode<>(14);

        n40_e4.left = n36_e4;
        n40_e4.right = n23_e4;
        n36_e4.left = n10_e4;
        n23_e4.left = n5_e4;
        n23_e4.right = n6_e4;
        n10_e4.left = n1_e4;
        n5_e4.left = n14_e4;

        System.out.println(Solution.isHeap(n40_e4));


        // Example 5
        TreeNode<Integer> n15_e5 = new TreeNode<>(15);
        TreeNode<Integer> n14_e5 = new TreeNode<>(14);
        TreeNode<Integer> n10_e5 = new TreeNode<>(10);
        TreeNode<Integer> n4_e5 = new TreeNode<>(4);
        TreeNode<Integer> n5_e5 = new TreeNode<>(5);
        TreeNode<Integer> n11_e5 = new TreeNode<>(11);
        TreeNode<Integer> n5b_e5 = new TreeNode<>(5);
        TreeNode<Integer> n1_e5 = new TreeNode<>(1);
        TreeNode<Integer> n2_e5 = new TreeNode<>(2);

        n15_e5.left = n14_e5;
        n15_e5.right = n10_e5;
        n14_e5.left = n4_e5;
        n14_e5.right = n5_e5;
        n10_e5.left = n11_e5;
        n10_e5.right = n5b_e5;
        n4_e5.left = n1_e5;
        n4_e5.right = n2_e5;

        System.out.println(Solution.isHeap(n15_e5));

        // Example 6
        TreeNode<Integer> n97_img = new TreeNode<>(97);

        TreeNode<Integer> n46_img = new TreeNode<>(46);
        TreeNode<Integer> n37_img = new TreeNode<>(37);

        TreeNode<Integer> n12_img = new TreeNode<>(12);
        TreeNode<Integer> n3_img  = new TreeNode<>(3);
        TreeNode<Integer> n7_img  = new TreeNode<>(7);
        TreeNode<Integer> n31_img = new TreeNode<>(31);

        TreeNode<Integer> n6_img = new TreeNode<>(6);
        TreeNode<Integer> n9_img = new TreeNode<>(9);

        n97_img.left = n46_img;
        n97_img.right = n37_img;

        n46_img.left = n12_img;
        n46_img.right = n3_img;

        n37_img.left = n7_img;
        n37_img.right = n31_img;

        n12_img.left = n6_img;
        n12_img.right = n9_img;

        System.out.println(Solution.isHeap(n97_img));
    }
}
