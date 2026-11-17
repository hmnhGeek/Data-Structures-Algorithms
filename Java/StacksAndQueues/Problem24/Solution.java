// Problem link - https://www.geeksforgeeks.org/dsa/efficiently-implement-k-queues-single-array/


package StacksAndQueues.Problem24;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        int n = 10, k = 3;
        KQueues<Integer> queues = new KQueues<>(k, n);
        queues.enqueue(0, 10);
        queues.enqueue(1, 20);
        queues.enqueue(0, 30);
        queues.enqueue(2, 40);
        System.out.println(queues.dequeue(0));
        System.out.println(queues.dequeue(1));
        System.out.println(queues.dequeue(2));
        System.out.println(queues.dequeue(0));
        System.out.println(queues.dequeue(0));
        System.out.println(queues.getArr());

        // Example 2
        n = 9;
        k = 4;
        queues = new KQueues<>(k, n);
        queues.enqueue(0, 10);
        queues.enqueue(0, 20);
        queues.enqueue(0, 30);
        queues.enqueue(3, 100);
        queues.enqueue(1, -10);
        queues.enqueue(2, -20);
        queues.enqueue(2, -30);
        queues.enqueue(2, -40);
        System.out.println(queues.dequeue(0));
        System.out.println(queues.dequeue(0));
        System.out.println(queues.dequeue(0));
        System.out.println(queues.dequeue(3));
        System.out.println(queues.dequeue(2));
        System.out.println(queues.getArr());
    }
}
