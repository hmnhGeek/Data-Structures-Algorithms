package StacksAndQueues.Problem20;

public class Solution {
    public static void main(String[] args) {
        Stack<Integer> stack1 = new Stack<>();
        stack1.push(5);
        stack1.push(3);
        stack1.push(4);
        System.out.println(stack1.top());
        System.out.println(stack1.pop());
        System.out.println(stack1.size());
        System.out.println();

        Stack<Integer> stack2 = new Stack<>();
        System.out.println(stack2.size());
        System.out.println(stack2.top());
        stack2.push(10);
        System.out.println(stack2.top());
    }
}
