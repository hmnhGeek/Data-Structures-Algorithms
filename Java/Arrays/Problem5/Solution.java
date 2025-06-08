package Arrays.Problem5;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void moveNegatives(List<Integer> arr) {
        int n = arr.size();
        int i = 0;

        // make low to point to the first positive integer.
        while (i < n && arr.get(i) < 0) {
            i += 1;
        }
        int low = i;

        // make mid to point to low + 1.
        int mid = i + 1;

        // while mid is within bounds...
        while (mid < n) {
            // if the mid-element is negative...
            if (arr.get(mid) < 0) {
                // swap with the first positive at low.
                Collections.swap(arr, low, mid);

                // move low to the next first positive
                while (low < n && arr.get(low) < 0) {
                    low += 1;
                }
                // again, move mid to low + 1.
                mid = low + 1;
                continue;
            }
            // else, if mid element is already positive, increment mid only.
            mid += 1;
        }
    }

    public static void helper(List<Integer> arr) {
        moveNegatives(arr);
        System.out.println(arr);
    }

    public static void main(String[] args) {
        helper(Arrays.asList(-12, 11, -13, -5, 6, -7, 5, -3, -6));
        helper(Arrays.asList(-5, 7, -3, -4, 9, 10, -1, 11));
        helper(Arrays.asList(1, -1, 3, 2, -7, -5, 11, 6));
        helper(Arrays.asList(3,1,-2,-5,2,-4));
        helper(Arrays.asList(-1, 1));
        helper(Arrays.asList(-2, -5, -1));
        helper(Arrays.asList(2,1,7,4,9,0,3,2));
    }
}
