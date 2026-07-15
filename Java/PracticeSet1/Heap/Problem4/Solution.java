// Problem link - https://www.geeksforgeeks.org/problems/k-largest-elements4206/1
// Solution - https://www.youtube.com/watch?v=3DdP6Ef8YZM


package PracticeSet1.Heap.Problem4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getKLargest(Arrays.asList(12, 5, 787, 1, 23), 2));
        System.out.println(getKLargest(Arrays.asList(1, 23, 12, 9, 30, 2, 50), 3));
        System.out.println(getKLargest(Arrays.asList(12, 23), 1));
        System.out.println(getKLargest(Arrays.asList(3,2,1,5,6,4), 2));
        System.out.println(getKLargest(Arrays.asList(3,2,3,1,2,4,5,5,6), 4));
    }

    public static List<Integer> getKLargest(List<Integer> arr, int k) {
        /*
            Time complexity is O(n*log(k)) and space complexity is O(k).
         */
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
