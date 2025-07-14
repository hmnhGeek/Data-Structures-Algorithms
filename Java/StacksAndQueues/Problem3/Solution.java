package StacksAndQueues.Problem3;

public class Solution {
    public static void main(String[] args) {
        TwoStacks<Integer> stacks = new TwoStacks<>();
        stacks.push1(2);
        stacks.push1(3);
        stacks.push2(4);
        System.out.println(stacks.pop1());
        System.out.println(stacks.pop2());
        System.out.println(stacks.pop2());
    }
}
