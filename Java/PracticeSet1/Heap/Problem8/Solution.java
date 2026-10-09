package PracticeSet1.Heap.Problem8;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getKthSmallest(Arrays.asList(20, -5, -1), 3));
        System.out.println(getKthSmallest(Arrays.asList(10, -10, 20, -40), 6));
        System.out.println(getKthSmallest(Arrays.asList(2, 6, 4, 1), 3));
        System.out.println(getKthSmallest(Arrays.asList(3, 2, 1), 2));
    }

    private static List<Integer> getSubArraySums(List<Integer> arr) {
        List<Integer> sum = new ArrayList<>();
        for (int i = 0; i < arr.size(); i += 1) {
            sum.add(arr.get(i));
            int s = arr.get(i);
            for (int j = i + 1; j < arr.size(); j += 1) {
                s += arr.get(j);
                sum.add(s);
            }
        }
        return sum;
    }

    public static Integer getKthSmallest(List<Integer> arr, Integer k) {
        List<Integer> sums = getSubArraySums(arr);
        MinHeap<Integer> minHeap = new MinHeap<>();
        for (int i = 0; i < k; i += 1) {
            minHeap.insert(sums.get(i));
        }
        int i = k;
        while (i < sums.size()) {
            if (sums.get(i) > minHeap.getHeap().getFirst()) {
                minHeap.pop();
                minHeap.insert(sums.get(i));
            }
            i += 1;
        }
        return minHeap.getHeap().getFirst();
    }
}
