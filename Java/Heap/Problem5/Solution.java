package Heap.Problem5;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(kSmallest(Arrays.asList(7, 10, 4, 3, 20, 15), 3));
        System.out.println(kSmallest(Arrays.asList(7, 10, 4, 3, 20, 15), 4));
        System.out.println(kSmallest(Arrays.asList(4, 2, 68, 99, 3, 4), 5));
    }

    public static Integer kSmallest(List<Integer> arr, Integer k) {
        MaxHeap<Integer> maxHeap = new MaxHeap<>();
        for (int i = 0; i < k; i += 1) {
            maxHeap.insert(arr.get(i));
        }
        int i = k;
        while (i < arr.size()) {
            if (arr.get(i).compareTo(maxHeap.getHeap().getFirst()) < 0) {
                maxHeap.pop();
                maxHeap.insert(arr.get(i));
            }
            i += 1;
        }
        return maxHeap.getHeap().getFirst();
    }
}
