// Problem link - https://www.geeksforgeeks.org/dsa/implement-stack-queue-using-deque/


package StacksAndQueues.Problem21;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 2, 3, 4);
        Stack<Integer> stack = new Stack<>();
        Queue<Integer> queue = new Queue<>();
        for (Integer i : list) {
            stack.push(i);
            queue.enqueue(i);
        }
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
        }
        while (!queue.isEmpty()) {
            System.out.println(queue.dequeue());
        }
    }
}
