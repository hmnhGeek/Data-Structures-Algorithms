package Arrays.Problem4;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void dnfSort(List<Integer> arr) {
        int n = arr.size();
        int low = 0, mid = 0, high = n - 1;
        while (mid <= high) {
            if (arr.get(mid) == 0) {
                Collections.swap(arr, low, mid);
                low += 1;
                mid += 1;
            } else if (arr.get(mid) == 1) {
                mid += 1;
            } else {
                Collections.swap(arr, mid, high);
                high -= 1;
            }
        }
        System.out.println(arr);
    }

    public static void main(String[] args) {
        dnfSort(Arrays.asList(0, 1, 2, 0, 1, 2));
    }
}
