package BinaryTrees.Problem19;

public class Solution {
    private Integer getNodeData(Node<Integer> node) {
        if (node == null) return 0;
        return node.data;
    }

    public Integer convertToSumTree(Node<Integer> root) {
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
    }
}
