package Heap.Problem4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getKLargestElements(List<Integer> arr, Integer k) {
        if (k <= 0 || k >= arr.size()) return null;
        MinHeap<Integer> minHeap = new MinHeap<>();
        for (int i = 0; i < k; i += 1) {
            minHeap.insert(arr.get(i));
        }
        int i = k;
        while (i < arr.size()) {
            if (minHeap.getHeap().getFirst() < arr.get(i)) {
                minHeap.pop();
                minHeap.insert(arr.get(i));
            }
            i += 1;
        }
        return minHeap.getHeap();
    }

    public static void main(String[] args) {
        List<Integer> arr1 = Arrays.asList(12, 5, 787, 1, 23);
        System.out.println(getKLargestElements(arr1, 2));
    }
}
