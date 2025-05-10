// Problem link - https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/#better-approach-1-using-maxheap-n-log-n-time-and-on-space


package Heap.Problem3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class HeapObject implements Comparable<HeapObject> {
    private Integer element;
    private Integer index;

    public HeapObject(Integer element, Integer index) {
        this.element = element;
        this.index = index;
    }

    public Integer getElement() {
        return element;
    }

    public Integer getIndex() {
        return index;
    }

    @Override
    public int compareTo(HeapObject o) {
        return this.element.compareTo(o.getElement());
    }
}

public class Solution {
    private static List<Integer> getSlidingWindowMaximum(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */

        // edge case
        if (k <= 0 || k > arr.size()) return null;

        // define a max heap which can store at max `n` elements.
        MaxHeap<HeapObject> maxHeap = new MaxHeap<>();
        List<Integer> result = new ArrayList<>();
        int n = arr.size();

        for (int i = 0; i < n; i += 1) {
            // push the current element into the max heap
            maxHeap.insert(new HeapObject(arr.get(i), i));

            // Remove elements outside the window
            while (maxHeap.getHeap().getFirst().getIndex() <= i - k) {
                maxHeap.pop();
            }

            // Append current max to result once the first window is completed
            if (i >= k - 1) {
                result.add(maxHeap.getHeap().getFirst().getElement());
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1, 2, 3, 1, 4, 5, 2, 3, 6), 3));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(5, 1, 3, 4, 2, 6), 1));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1, 3, 2, 1, 7, 3), 3));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1, 3, -1, -3, 5, 3, 6, 7), 3));
    }
}
