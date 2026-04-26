// Problem link - https://www.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1


package PracticeSet1.BinarySearchTree.Problem6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getInorderSuccessors(List<Integer> nodes) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (Integer x : nodes) {
            bst.insert(x);
        }
        List<Integer> successors = new ArrayList<>();
        solve(bst.root, successors, bst);
        return successors;
    }

    private static void solve(Node<Integer> root, List<Integer> successors, BinarySearchTree<Integer> bst) {
        if (root != null) {
            solve(root.left, successors, bst);
            Node<Integer> succ = bst.getSuccessor(root);
            if (succ == null) {
                successors.add(null);
            } else {
                successors.add(succ.data);
            }
            solve(root.right, successors, bst);
        }
    }

    public static void main(String[] args) {
        List<Integer> successors1 = getInorderSuccessors(Arrays.asList(10, 8, 12, 3));
        System.out.println(successors1);

        List<Integer> successors2 = getInorderSuccessors(Arrays.asList(1, 2, 3));
        System.out.println(successors2);
    }
}
