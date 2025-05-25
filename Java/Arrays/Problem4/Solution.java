package Arrays.Problem4;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void dnfSort(List<Integer> arr) {
        int n = arr.size();

        // initialize low, mid and high pointers
        int low = 0, mid = 0, high = n - 1;

        /*
            The idea is that all elements from 0 to low - 1 will be 0s.
            All elements from mid to high - 1 will be 1s.
            All elements from high till end will be 2s.
         */

        // run a loop till mid <= high...
        while (mid <= high) {
            // if a 0 is encountered at mid.
            if (arr.get(mid) == 0) {
                // swap with low and increment both mid and low.
                Collections.swap(arr, low, mid);
                low += 1;
                mid += 1;
            } else if (arr.get(mid) == 1) {
                // if mid-element is 1, then simply increment mid.
                mid += 1;
            } else {
                // swap mid and high element and decrement only high; don't change mid.
                Collections.swap(arr, mid, high);
                high -= 1;
            }
        }
        System.out.println(arr);
    }

    public static void main(String[] args) {
        dnfSort(Arrays.asList(0, 1, 2, 0, 1, 2));
        dnfSort(Arrays.asList(0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1));
        dnfSort(Arrays.asList(2, 1, 2, 0, 1, 2));
        dnfSort(Arrays.asList(0, 1, 0));
        dnfSort(Arrays.asList(1, 1, 2, 2, 1));
    }
}
