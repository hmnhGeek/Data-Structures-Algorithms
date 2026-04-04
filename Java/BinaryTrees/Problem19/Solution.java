// Problem link - https://www.geeksforgeeks.org/problems/transform-to-sum-tree/1


package BinaryTrees.Problem19;

public class Solution {
    private Integer getNodeData(Node<Integer> node) {
        if (node == null) return 0;
        return node.data;
    }

    public Integer convertToSumTree(Node<Integer> root) {
        /*
            Time complexity is O(n) and space complexity is O(h).
         */
        if (root == null) {
            return 0;
        }
        Integer rootData = root.data;
        Integer leftVal = convertToSumTree(root.left);
        Integer rightVal = convertToSumTree(root.right);
        root.data = leftVal + rightVal;
        return rootData + root.data;
    }

    public void printTree(Node<Integer> root) {
        if (root != null) {
            printTree(root.left);
            System.out.println(root.data);
            printTree(root.right);
        }
    }

    public static void main(String[] args) {
        // Create nodes
        Node<Integer> n10 = new Node<>(10);
        Node<Integer> n_2 = new Node<>(-2);
        Node<Integer> n6 = new Node<>(6);
        Node<Integer> n8 = new Node<>(8);
        Node<Integer> n_4 = new Node<>(-4);
        Node<Integer> n7 = new Node<>(7);
        Node<Integer> n5 = new Node<>(5);

        // Connect nodes
        n10.left = n_2;
        n10.right = n6;

        n_2.left = n8;
        n_2.right = n_4;

        n6.left = n7;
        n6.right = n5;

        // Create solution object
        Solution sol = new Solution();

        // Print original tree (inorder)
        System.out.println("Original Tree:");
        sol.printTree(n10);

        // Convert to sum tree
        sol.convertToSumTree(n10);

        // Print transformed tree
        System.out.println("Sum Tree:");
        sol.printTree(n10);

        System.out.println();
        System.out.println();

        // Create nodes
        n5 = new Node<>(5);
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n_8 = new Node<>(-8);
        Node<Integer> n4 = new Node<>(4);
        n6 = new Node<>(6);

        // Connect nodes
        n5.right = n1;

        n1.left = n_8;
        n1.right = n4;

        n_8.left = n6;

        // Print original tree
        System.out.println("Original Tree:");
        sol.printTree(n5);

        // Convert to sum tree
        sol.convertToSumTree(n5);

        // Print sum tree
        System.out.println("Sum Tree:");
        sol.printTree(n5);

        System.out.println();
        System.out.println();

        // Create nodes
        Node<Integer> n1_root = new Node<>(1);
        n_2 = new Node<>(-2);
        Node<Integer> n1_right = new Node<>(1);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n1_leaf = new Node<>(1);

        // Connect nodes
        n1_root.left = n_2;
        n1_root.right = n1_right;

        n_2.left = n3;
        n_2.right = n1_leaf;

        // Print original tree
        System.out.println("Original Tree:");
        sol.printTree(n1_root);
        sol.convertToSumTree(n1_root);
        System.out.println("Sum Tree:");
        sol.printTree(n1_root);
    }
}
