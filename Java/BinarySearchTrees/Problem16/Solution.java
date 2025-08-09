// Problem link - https://www.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1


package BinarySearchTrees.Problem16;

public class Solution {
    public static Integer getCountOfNodesInRange(Node root, Integer low, Integer high) {
        /*
            Time complexity is O(n) and space complexity is O(log(n)).
         */

        if (root == null) return 0;
        Integer leftCount = getCountOfNodesInRange(root.getLeft(), low, Math.min(root.getData(), high));
        Integer rightCount = getCountOfNodesInRange(root.getRight(), Math.max(root.getData(), low), high);
        if (root.getData() <= high && root.getData() >= low) {
            return 1 + leftCount + rightCount;
        }
        return leftCount + rightCount;
    }

    public static void main(String[] args) {
        // Example 1
        Node root = new Node(10);
        Node n5 = new Node(5);
        Node n50 = new Node(50);
        Node n1 = new Node(1);
        Node n40 = new Node(40);
        Node n100 = new Node(100);
        root.setLeft(n5);
        root.setRight(n50);
        n5.setLeft(n1);
        n50.setLeft(n40);
        n50.setRight(n100);
        System.out.println(getCountOfNodesInRange(root, 5, 45));
        System.out.println(getCountOfNodesInRange(root, 10, 100));

        // Example 2
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        node1.setLeft(node2);
        node1.setRight(node3);
        System.out.println(getCountOfNodesInRange(node1, 23, 95));
    }
}
