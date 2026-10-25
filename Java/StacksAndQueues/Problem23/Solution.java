package StacksAndQueues.Problem23;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        Queue<Integer> q1 = new Queue<>();
        q1.enqueue(5);
        q1.enqueue(3);
        q1.enqueue(4);
        System.out.println(q1.front());
        q1.dequeue();
        System.out.println(q1.size());
        System.out.println(q1.front());

        // Example 2
        Queue<Integer> q2 = new Queue<>();
        System.out.println(q2.front());
        System.out.println(q2.size());
        q2.enqueue(10);
        System.out.println(q2.front());
    }
}
