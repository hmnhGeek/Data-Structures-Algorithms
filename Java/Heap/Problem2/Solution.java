package Heap.Problem2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T extends Comparable<T>> List<T> heapSort(List<T> arr) {
        MinHeap<T> minHeap = new MinHeap<>();
        arr.forEach(minHeap::insert);
        List<T> result = new ArrayList<>();
        while (!minHeap.isEmpty()) {
            result.add(minHeap.pop());
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(heapSort(Arrays.asList(9, 4, 3, 8, 10, 2, 5)));
    }
}
