// Problem link - https://www.tutorialspoint.com/javaexamples/data_stack.htm

package StacksAndQueues.Problem1;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<Integer> arr = Arrays.asList(24,79,23,75,0);
        Stack<Integer> stack = new Stack<>();
        arr.forEach(stack::push);
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
        }
    }
}
