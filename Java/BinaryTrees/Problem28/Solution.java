// Problem link - https://www.geeksforgeeks.org/dsa/find-largest-subtree-sum-tree/
// Solution - https://www.youtube.com/watch?v=zm5CykXlxaA


package BinaryTrees.Problem28;


import java.util.Arrays;
import java.util.List;

class Node<T> {
    public T data;
    public Node<T> left, right;

    public Node(T data) {
        this.data = data;
        this.left = this.right = null;
    }
}


public class Solution {
    public static Integer getMaxSum(Node<Integer> root) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        List<Integer> maxSum = Arrays.asList(0);
        solve(root, maxSum);
        return maxSum.getFirst();
    }

    private static Integer solve(Node<Integer> root, List<Integer> maxSum) {
        if (root == null) {
            return 0;
        }
        Integer leftSubtreeSum = solve(root.left, maxSum);
        Integer rightSubtreeSum = solve(root.right, maxSum);
        Integer currSubtreeSum = root.data + leftSubtreeSum + rightSubtreeSum;
        maxSum.set(0, Math.max(maxSum.getFirst(), currSubtreeSum));
        return currSubtreeSum;
    }

    public static void main(String[] args) {

        // Example 1
        Node<Integer> n10 = new Node<>(10);
        Node<Integer> n8 = new Node<>(8);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        Node<Integer> n5 = new Node<>(5);

        n10.left = n8;
        n10.right = n2;
        n8.left = n3;
        n8.right = n5;

        System.out.println(Solution.getMaxSum(n10)); // Output: 28

        // Example 2
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> nm2 = new Node<>(-2);
        Node<Integer> n3b = new Node<>(3);
        Node<Integer> n4 = new Node<>(4);
        Node<Integer> n5b = new Node<>(5);
        Node<Integer> nm6 = new Node<>(-6);
        Node<Integer> n2b = new Node<>(2);

        n1.left = nm2;
        n1.right = n3b;
        nm2.left = n4;
        nm2.right = n5b;
        n3b.left = nm6;
        n3b.right = n2b;

        System.out.println(Solution.getMaxSum(n1)); // Output: 13
    }
}
