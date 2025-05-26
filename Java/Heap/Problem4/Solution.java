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

        List<Integer> arr2 = Arrays.asList(1, 23, 12, 9, 30, 2, 50);
        System.out.println(getKLargestElements(arr2, 3));

        List<Integer> arr3 = Arrays.asList(12, 23);
        System.out.println(getKLargestElements(arr3, 1));

        List<Integer> arr4 = Arrays.asList(11, 5, 12, 9, 44, 17, 2);
        System.out.println(getKLargestElements(arr4, 2));

        List<Integer> arr5 = Arrays.asList(11, 3, 4, 6);
        System.out.println(getKLargestElements(arr5, 3));
    }
}
