package StacksAndQueues.Problem5;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        NStacks<Integer> stacks = new NStacks<>(9, 3);
        stacks.push(10, 2);
        stacks.push(20, 2);
        stacks.push(30, 2);
        stacks.push(100, 1);
        stacks.push(200, 1);
        System.out.println(stacks.pop(2));
        System.out.println(stacks.pop(2));
        System.out.println(stacks.pop(1));
        stacks.push(2, 3);
    }
}
