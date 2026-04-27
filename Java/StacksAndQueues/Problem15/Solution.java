package StacksAndQueues.Problem15;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        test(41, 3, 32, 2, 11);

        // Example 2
        test(3, 2, 1);
    }

    private static void test(Integer...args) {
        Stack<Integer> s1 = new Stack<>();
        for (Integer i : Arrays.asList(args)) {
            s1.push(i);
        }
        s1 = Utils.sort(s1);
        while (!s1.isEmpty()) {
            System.out.print(s1.pop() + " ");
        }
        System.out.println();
    }
}
