// Problem link - https://www.geeksforgeeks.org/dsa/efficiently-implement-k-stacks-single-array/
// Solution - https://www.youtube.com/watch?v=lrSXKLmnMV8


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

        System.out.println();
        System.out.println();

        // Example 2
        NStacks<Integer> stacks1 = new NStacks<>(5, 4);
        stacks1.push(15, 1);
        stacks1.push(25, 2);
        stacks1.push(35, 3);
        stacks1.push(45, 4);
        stacks1.push(55, 1);
        System.out.println(stacks1.pop(1));
        System.out.println(stacks1.pop(2));
        stacks1.push(55, 1);
        System.out.println(stacks1.pop(4));
    }
}
