// Problem link - https://www.geeksforgeeks.org/dsa/rearrange-array-alternating-positive-negative-items-o1-extra-space/
// Problem link - https://leetcode.com/problems/rearrange-array-elements-by-sign/


package Arrays.Problem20;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void alternateNumbers(List<Integer> arr) {
        int i = 0, j = 0, n = arr.size();
        boolean placePositive = true;
        while (i < n) {
            if (arr.get(i) >= 0) {
                if (placePositive) {
                    i += 1;
                    j += 1;
                } else {
                    while (j < n && arr.get(j) >= 0) {
                        j += 1;
                    }
                    if (j < n) {
                        Collections.swap(arr, i, j);
                    }
                    i += 1;
                    j = i;
                }
            } else {
                if (placePositive) {
                    while (j < n && arr.get(j) < 0) {
                        j += 1;
                    }
                    if (j < n) {
                        Collections.swap(arr, i, j);
                    }
                    i += 1;
                    j = i;
                } else {
                    i += 1;
                    j += 1;
                }
            }
            placePositive = !placePositive;
        }
        System.out.println(arr);
    }

    public static void main(String[] args) {
        alternateNumbers(Arrays.asList(1, 2, 3, -4, -1, 4));
        alternateNumbers(Arrays.asList(-5, -2, 5, 2, 4, 7, 1, 8, 0, -8));
        alternateNumbers(Arrays.asList(3,1,-2,-5,2,-4));
        alternateNumbers(Arrays.asList(-1,1));
        alternateNumbers(Arrays.asList(1,2,-4,-5));
        alternateNumbers(Arrays.asList(1,2,3,-1,-2,-3));
    }
}
