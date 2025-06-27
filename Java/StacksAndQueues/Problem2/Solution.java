// Problem link - https://www.geeksforgeeks.org/dsa/introduction-and-array-implementation-of-queue/

package StacksAndQueues.Problem2;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        Queue<Integer> queue = new Queue<>();
        for (Integer i : Arrays.asList(1, 2, 3, 4)) {
            queue.push(i);
        }
        while (!queue.isEmpty()) {
            System.out.println(queue.pop());
        }
    }
}
