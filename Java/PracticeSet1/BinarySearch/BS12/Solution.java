package PracticeSet1.BinarySearch.BS12;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static Integer getMinHours(List<Integer> bananas, Integer maxHoursAllowed) {
        int low = 1, high = Collections.max(bananas);
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int hoursConsumed = getConsumedHours(bananas, mid);
            if (hoursConsumed <= maxHoursAllowed) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private static int getConsumedHours(List<Integer> bananas, int mid) {
        int count = 0;
        for (int i = 0; i < bananas.size(); i += 1) {
            count += (int) Math.ceil((double) bananas.get(i) / mid);
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(getMinHours(Arrays.asList(3, 6, 7, 11), 8));
        System.out.println(getMinHours(Arrays.asList(3, 6, 2, 8), 7));
        System.out.println(getMinHours(Arrays.asList(7, 15, 6, 3), 8));
        System.out.println(getMinHours(Arrays.asList(25, 12, 8, 14, 19), 5));
        System.out.println(getMinHours(Arrays.asList(30, 11, 23, 4, 20), 5));
        System.out.println(getMinHours(Arrays.asList(30, 11, 23, 4, 20), 6));
    }
}
