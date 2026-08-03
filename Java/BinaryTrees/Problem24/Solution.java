// Problem link - # Problem link - https://www.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1
// Solution - https://www.youtube.com/watch?v=m0dG99f5ct4


package BinaryTrees.Problem24;

import java.util.*;

public class Solution {
    public static Set<String> getDuplicates(Node<Integer> root) {
        /*
            Time complexity is O(N^2) because we are visiting every node again and again for each subtree
            Space complexity is O(N).
         */
        Map<String, Integer> mp = new HashMap<>();
        Set<String> result = new HashSet<>();
        solve(root, mp, result);
        return result;
    }

    private static String solve(Node<Integer> root, Map<String, Integer> mp, Set<String> result) {
        if (root == null) {
            return "N";
        }
        String s = root.data.toString() + "," + solve(root.left, mp, result) + "," + solve(root.right, mp, result);
        if (mp.containsKey(s)) {
            result.add(s);
        }
        mp.put(s, mp.getOrDefault(s, 0));
        return s;
    }

    public static void main(String[] args) {

        // Example 1
        Node<Integer> one = new Node<>(1);
        Node<Integer> two = new Node<>(2);
        Node<Integer> three = new Node<>(3);
        Node<Integer> four = new Node<>(4);
        Node<Integer> two1 = new Node<>(2);
        Node<Integer> four2 = new Node<>(4);
        Node<Integer> four3 = new Node<>(4);

        one.left = two;
        two.left = four;
        three.left = two1;
        two1.left = four3;
        one.right = three;
        three.right = four2;

        System.out.println(getDuplicates(one));
        System.out.println();

        // Example 2
        Node<Integer> five = new Node<>(5);
        Node<Integer> fourA = new Node<>(4);
        Node<Integer> six = new Node<>(6);
        Node<Integer> threeA = new Node<>(3);
        Node<Integer> fourB = new Node<>(4);
        Node<Integer> threeB = new Node<>(3);
        Node<Integer> sixB = new Node<>(6);

        five.left = fourA;
        fourA.left = threeA;
        fourB.left = threeB;
        five.right = six;
        fourA.right = fourB;
        fourB.right = sixB;

        System.out.println(getDuplicates(five));
    }
}
