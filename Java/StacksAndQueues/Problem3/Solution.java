// Problem link - https://www.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1

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

        TwoStacks<Integer> stacks1 = new TwoStacks<>();
        stacks1.push1(1);
        stacks1.push2(2);
        System.out.println(stacks1.pop1());
        stacks1.push1(3);
        System.out.println(stacks1.pop1());
        System.out.println(stacks1.pop1());

        TwoStacks<Integer> stacks2 = new TwoStacks<>();
        stacks2.push1(2);
        stacks2.push1(3);
        stacks2.push1(4);
        System.out.println(stacks2.pop2());
        System.out.println(stacks2.pop2());
        System.out.println(stacks2.pop2());
    }
}
