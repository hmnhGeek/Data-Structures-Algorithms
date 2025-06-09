// Problem link - https://www.geeksforgeeks.org/kth-smallest-largest-element-in-unsorted-array/

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
        /*
            Time complexity is O(n * log(k)) and space complexity is O(k).
         */

        // heap will take at max k elements and so, O(k) space.
        MaxHeap<Integer> maxHeap = new MaxHeap<>();

        // This will take k * log(k) time.
        for (int i = 0; i < k; i += 1) {
            maxHeap.insert(arr.get(i));
        }

        // loop on the remaining items in n - k iterations.
        int i = k;
        while (i < arr.size()) {
            // if top element is larger than ith element, pop the top and insert this ith element into the heap.
            // this is a log(k) operation.
            if (arr.get(i).compareTo(maxHeap.getHeap().getFirst()) < 0) {
                maxHeap.pop();
                maxHeap.insert(arr.get(i));
            }
            i += 1;
        }
        return maxHeap.getHeap().getFirst();
    }
}
