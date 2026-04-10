package PracticeSet1.BinarySearch.BS23;

import java.util.List;

public class Utils {
    public static Integer getOnesCount(List<Integer> row) {
        /*
            Time complexity is O(log(m)) and space complexity is O(1).
         */
        int m = row.size(), low = 0, high = m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (row.get(mid).equals(1)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return m - low;
    }
}
