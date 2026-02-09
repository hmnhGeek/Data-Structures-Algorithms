// Problem link - https://www.geeksforgeeks.org/convert-min-heap-to-max-heap/


package Heap.Problem16;

public class Solution {
    public static void main(String[] args) {
        show(3, 5, 9, 6, 8, 20, 10, 12, 18, 9);
        show(3, 4, 8, 11, 13);
    }

    private static <T extends Comparable<T>> void show(T...args) {
        MinHeap<T> minHeap = new MinHeap<>();
        for (T x : args) {
            minHeap.insert(x);
        }
        MaxHeap<T> maxHeap = convertToMaxHeap(minHeap);
        while (!minHeap.isEmpty()) {
            System.out.println(minHeap.pop());
        }
        System.out.println();
        while (!maxHeap.isEmpty()) {
            System.out.println(maxHeap.pop());
        }
        System.out.println();
        System.out.println();
    }

    public static <T extends Comparable<T>> MaxHeap<T> convertToMaxHeap(MinHeap<T> minHeap) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        MaxHeap<T> maxHeap = new MaxHeap<>();
        for (T i : minHeap.getHeap()) {
            maxHeap.insert(i);
        }
        return maxHeap;
    }
}
