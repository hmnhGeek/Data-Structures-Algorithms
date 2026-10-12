package PracticeSet1.BinarySearch.BS13;

import java.util.Collections;
import java.util.List;

public class Solution {
    public static Integer getMinDayToBloom(List<Integer> arr, int m, int k) {
        int low = Collections.min(arr), high = Collections.max(arr);
        while (low <= high) {
            int mid = (low + (high - low)/2);
            boolean isPossible = checkIfPossible(arr, mid, m, k);
            if (isPossible) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
