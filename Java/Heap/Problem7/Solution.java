// Problem link - https://www.geeksforgeeks.org/problems/merge-two-binary-max-heap0144/1

package Heap.Problem7;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        MaxHeap<Integer> m1 = buildHeap(Arrays.asList(10, 5, 6, 2));
        MaxHeap<Integer> m2 = buildHeap(Arrays.asList(12, 7, 9));
        mergeHeaps(m1, m2);
        while (!m1.isEmpty()) {
            System.out.println(m1.pop());
        }
    }

    public static <T extends Comparable<T>> MaxHeap<T> buildHeap(List<T> arr) {
        MaxHeap<T> maxHeap = new MaxHeap<>();
        arr.forEach(maxHeap::insert);
        return maxHeap;
    }

    public static <T extends Comparable<T>> void mergeHeaps(MaxHeap<T> h1, MaxHeap<T> h2) {
        /*
            Time complexity is O(m * (log(m) + log(n))) and space complexity is O(1).
         */
        while (!h2.isEmpty()) {
            h1.insert(h2.pop());
        }
    }
}
