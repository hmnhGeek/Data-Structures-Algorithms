// Problem link - https://www.geeksforgeeks.org/dsa/k-th-largest-sum-contiguous-subarray/#naive-approach-2-using-prefix-sum-and-sorting-on2-log-n-time-and-on-2-space
// Solution - https://www.youtube.com/watch?v=xhAL9uxUhGw
// Prefix sum logic - https://www.youtube.com/watch?v=PhgtNY_-CiY


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
        /*
            Time complexity is O(n^2 * log(k)) and space complexity is O(n).
         */

        List<Integer> prefixSums = generatePrefixSums(arr);
        MinHeap<Integer> minHeap = new MinHeap<>();

        // loop to calculate the contiguous subarray sums position-wise. This will take n^2 iterations.
        for (int i = 1; i < arr.size() + 1; i += 1) {
            // loop to traverse all positions that
            // form contiguous subarray
            for (int j = i; j < arr.size() + 1; j += 1) {
                // calculates the contiguous subarray
                // sums from j to i index
                Integer x = prefixSums.get(j) - prefixSums.get(i - 1);

                // The following ops are of order log(k).

                // if min heap has less than k elements,
                // then simply push it
                if (minHeap.getHeap().size() < k) {
                    minHeap.insert(x);
                } else {
                    // it the min heap has equal to
                    // k elements then just check
                    // if the largest kth element is
                    // smaller than x then insert
                    // else its of no use
                    if (minHeap.getHeap().getFirst() < x) {
                        minHeap.pop();
                        minHeap.insert(x);
                    }
                }
            }
        }
        // the top element will be then kth
        // largest element
        return minHeap.getHeap().getFirst();
    }

    public static void main(String[] args) {
        System.out.println(getKthLargest(Arrays.asList(20, -5, -1), 3));
    }
}
