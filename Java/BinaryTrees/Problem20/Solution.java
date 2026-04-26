// Problem link - https://www.geeksforgeeks.org/problems/construct-tree-1/1
// Solution - https://www.youtube.com/watch?v=aZNaLrVebKQ


package BinaryTrees.Problem20;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static Node<Integer> getTree(List<Integer> inorder, List<Integer> preorder) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.size(); i += 1) {
            map.put(inorder.get(i), i);
        }
        return solve(inorder, 0, inorder.size() - 1, preorder, 0, preorder.size(), map);
    }

    private static Node<Integer> solve(
            List<Integer> inorder, int inStart, int inEnd,
            List<Integer> preorder, int preStart, int preEnd,
            Map<Integer, Integer> map
    ) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        if (inStart > inEnd || preStart > preEnd) return null;
        Node<Integer> root = new Node<>(preorder.get(preStart));
        Integer inRoot = map.get(root.data);
        int left = inRoot - inStart;
        root.left = solve(inorder, inStart, inRoot - 1, preorder, preStart + 1, preStart + left, map);
        root.right = solve(inorder, inRoot + 1, inEnd, preorder, preStart + left + 1, preEnd, map);
        return root;
    }

    public static void getPostorder(Node<Integer> root) {
        if (root != null) {
            getPostorder(root.left);
            getPostorder(root.right);
            System.out.println(root.data);
        }
    }

    public static void main(String[] args) {
        Node<Integer> t1 = Solution.getTree(Arrays.asList(1, 6, 8, 7), Arrays.asList(1, 6, 7, 8));
        Solution.getPostorder(t1);
        System.out.println();

        Node<Integer> t2 = Solution.getTree(Arrays.asList(3, 1, 4, 0, 5, 2), Arrays.asList(0, 1, 3, 4, 2, 5));
        Solution.getPostorder(t2);
        System.out.println();

        Node<Integer> t3 = Solution.getTree(Arrays.asList(2, 5, 4, 1, 3), Arrays.asList(1, 4, 5, 2, 3));
        Solution.getPostorder(t3);
        System.out.println();
    }
}
