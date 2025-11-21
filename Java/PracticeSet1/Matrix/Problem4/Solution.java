package PracticeSet1.Matrix.Problem4;

import java.util.List;

public class Solution {
    public static int getCountOfOnes(List<Integer> arr, Integer m) {
        /*
            Time complexity is O(log(m)) and space complexity is O(1).
         */
        int low = 0, high = m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) == 1) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return m - low;
    }
}
