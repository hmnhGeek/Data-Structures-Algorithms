package PracticeSet1.BinarySearch.BS14;

import java.util.Collections;
import java.util.List;

public class Solution {
    public static Integer getSmallestDivisor(List<Integer> arr, int threshold) {
        int low = 1, high = Collections.max(arr);
        while (low <= high) {
            int mid = (low + (high - low)/2);
            boolean isPossible = checkPossible(arr, mid, threshold);
            if (isPossible) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
