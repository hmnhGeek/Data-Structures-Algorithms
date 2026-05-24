// Problem link - https://www.geeksforgeeks.org/dsa/heap-sort/


package PracticeSet1.Heap.Problem2;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T extends Comparable<T>> void sort(List<T> arr) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        MinHeap<T> minHeap = new MinHeap<>();
        for (T x : arr) {
            minHeap.insert(x);
        }
        int counter = 0;
        while (!minHeap.isEmpty()) {
            T x = minHeap.pop();
            arr.set(counter, x);
            counter += 1;
        }
    }

    public static void test(List<Integer> arr) {
        sort(arr);
        System.out.println(arr);
    }

    public static void main(String[] args) {
        test(Arrays.asList(9, 4, 3, 8, 10, 2, 5));
    }
}
