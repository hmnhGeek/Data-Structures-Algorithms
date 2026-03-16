// Problem link - https://stackoverflow.com/questions/45130465/inserting-at-the-end-of-stack


package StacksAndQueues.Problem13;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        for (Integer i : Arrays.asList(1, 2, 3, 4)) {
            stack.push(i);
        }
        stack.insertAtBottom(10);
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
        }
    }
}
