// Problem link - https://www.geeksforgeeks.org/dsa/merge-two-binary-max-heaps/#expected-approach-using-build-heap-function-on-m-time-and-on-m-space


package PracticeSet1.Heap.Problem7;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        MaxHeap<Integer> h1 = new MaxHeap<>();
        for (Integer i : Arrays.asList(10, 5, 6, 2)) {
            h1.insert(i);
        }
        MaxHeap<Integer> h2 = new MaxHeap<>();
        for (Integer i : Arrays.asList(12, 7, 9)) {
            h2.insert(i);
        }
        MaxHeap<Integer> merged = merge(h1, h2);
        while (!merged.isEmpty()) {
            System.out.println(merged.pop());
        }
    }

    public static MaxHeap<Integer> merge(MaxHeap<Integer> h1, MaxHeap<Integer> h2) {
        MaxHeap<Integer> merged = new MaxHeap<>();
        while (!h1.isEmpty()) {
            merged.insert(h1.pop());
        }
        while (!h2.isEmpty()) {
            merged.insert(h2.pop());
        }
        return merged;
    }
}
