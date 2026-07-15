package PracticeSet1.Heap.Problem4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getKLargest(Arrays.asList(12, 5, 787, 1, 23), 2));
        System.out.println(getKLargest(Arrays.asList(1, 23, 12, 9, 30, 2, 50), 3));
        System.out.println(getKLargest(Arrays.asList(12, 23), 1));
    }

    public static List<Integer> getKLargest(List<Integer> arr, int k) {
        MinHeap<Integer> pq = new MinHeap<>();
        for (int i = 0; i < k; i += 1) {
            pq.push(arr.get(i));
        }
        int i = k;
        while (i < arr.size()) {
            if (arr.get(i) > pq.getHeap().getFirst()) {
                pq.pop();
                pq.push(arr.get(i));
            }
            i += 1;
        }
        List<Integer> result = new ArrayList<>();
        while (!pq.isEmpty()) {
            result.add(pq.pop());
        }
        return result;
    }
}
