// Problem link - https://www.geeksforgeeks.org/dsa/reverse-a-stack/#approach-using-recusion


package StacksAndQueues.Problem14;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        for (Integer i : Arrays.asList(1, 2, 3, 4)) {
            stack.push(i);
        }
        System.out.println(stack);
        stack.reverse();
        System.out.println(stack);
    }
}
