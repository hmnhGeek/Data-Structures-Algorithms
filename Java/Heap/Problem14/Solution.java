// Problem link - https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1


package Heap.Problem14;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(connectRopes(Arrays.asList(4, 3, 2, 6)));
        System.out.println(connectRopes(Arrays.asList(4, 2, 7, 6, 9)));
        System.out.println(connectRopes(Arrays.asList(1, 2, 3)));
        System.out.println(connectRopes(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(connectRopes(Arrays.asList(10)));
        System.out.println(connectRopes(List.of()));
    }

    public static Integer connectRopes(List<Integer> ropes) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        MinHeap<Integer> minHeap = new MinHeap<>();
        for (Integer ropeLength : ropes) {
            minHeap.insert(ropeLength);
        }
        int cost = 0;
        while (minHeap.getHeap().size() > 1) {
            Integer rope1 = minHeap.pop(), rope2 = minHeap.pop();
            cost += (rope1 + rope2);
            minHeap.insert(rope1 + rope2);
        }
        return cost;
    }
}
