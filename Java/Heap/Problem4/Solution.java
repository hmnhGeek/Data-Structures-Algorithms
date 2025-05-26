// Problem link - https://www.geeksforgeeks.org/problems/k-largest-elements4206/1


package Heap.Problem4;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getKLargestElements(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n * log(k)) and space complexity is O(k).
         */
        if (k <= 0 || k >= arr.size()) return null;

        // create a new min heap
        MinHeap<Integer> minHeap = new MinHeap<>();

        // insert first k elements into this heap in O(k * log(k)) time and O(k) space.
        for (int i = 0; i < k; i += 1) {
            minHeap.insert(arr.get(i));
        }

        // loop on the remaining array in n - k iterations.
        int i = k;
        while (i < arr.size()) {
            // if the top element of the heap is less than current element, insert current element at its place in O(log(k)) time.
            if (minHeap.getHeap().getFirst() < arr.get(i)) {
                minHeap.pop();
                minHeap.insert(arr.get(i));
            }
            i += 1;
        }

        // return the k sized array.
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
