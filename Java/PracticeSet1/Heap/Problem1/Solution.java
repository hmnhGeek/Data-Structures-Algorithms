// Problem link - https://www.geeksforgeeks.org/dsa/building-heap-from-array/


package PracticeSet1.Heap.Problem1;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        test(1, 39, 7, 0, 3, 45, 3);
        test(4, 10, 3, 5, 1);
        test(1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17);
    }

    private static void test(Integer...args) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        List<Integer> arr = Arrays.asList(args);
        MaxHeap<Integer> maxHeap = new MaxHeap<>();
        for (Integer i : arr) {
            maxHeap.insert(i);
        }
        while (!maxHeap.isEmpty()) {
            System.out.print(maxHeap.pop() + " ");
        }
        System.out.println();
    }
}
