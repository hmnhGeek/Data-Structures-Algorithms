package PracticeSet1.Heap.Problem5;


import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getKthSmallest(Arrays.asList(10, 5, 4, 3, 48, 6, 2, 33, 53, 10), 4));
    }

    public static Integer getKthSmallest(List<Integer> arr, Integer k) {
        MaxHeap<Integer> maxHeap = new MaxHeap<>();
        for (int i = 0; i < k; i += 1) {
            maxHeap.insert(arr.get(i));
        }
        for (int i = k; i < arr.size(); i += 1) {
            Integer element = arr.get(i);
            if (element < maxHeap.getHeap().getFirst()) {
                maxHeap.pop();
                maxHeap.insert(element);
            }
        }
        return maxHeap.pop();
    }
}
