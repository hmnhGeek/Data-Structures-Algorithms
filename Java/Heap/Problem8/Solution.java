package Heap.Problem8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    private static List<Integer> generatePrefixSums(List<Integer> arr) {
        List<Integer> prefixSums = new ArrayList<>();
        prefixSums.add(0);
        for (int i = 0; i < arr.size(); i += 1) {
            prefixSums.add(arr.get(i) + prefixSums.get(i));
        }
        return prefixSums;
    }

    public static Integer getKthLargest(List<Integer> arr, Integer k) {
        List<Integer> prefixSums = generatePrefixSums(arr);
        MinHeap<Integer> minHeap = new MinHeap<>();
        for (int i = 1; i < arr.size() + 1; i += 1) {
            for (int j = i; j < arr.size() + 1; j += 1) {
                Integer x = prefixSums.get(j) - prefixSums.get(i - 1);
                if (minHeap.getHeap().size() < k) {
                    minHeap.insert(x);
                } else {
                    if (minHeap.getHeap().getFirst() < x) {
                        minHeap.pop();
                        minHeap.insert(x);
                    }
                }
            }
        }
        return minHeap.getHeap().getFirst();
    }

    public static void main(String[] args) {
        System.out.println(getKthLargest(Arrays.asList(20, -5, -1), 3));
    }
}
