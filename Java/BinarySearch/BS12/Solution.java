// Problem link - https://www.naukri.com/code360/problems/minimum-rate-to-eat-bananas_7449064
// Solution - https://www.youtube.com/watch?v=qyfekrNni90&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=13


package BinarySearch.BS12;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getMinHours(Arrays.asList(3, 6, 7, 11), 8));
        System.out.println(getMinHours(Arrays.asList(3, 6, 2, 8), 7));
        System.out.println(getMinHours(Arrays.asList(7, 15, 6, 3), 8));
        System.out.println(getMinHours(Arrays.asList(25, 12, 8, 14, 19), 5));
        System.out.println(getMinHours(Arrays.asList(30, 11, 23, 4, 20), 5));
        System.out.println(getMinHours(Arrays.asList(30, 11, 23, 4, 20), 6));
    }

    public static Integer getMinHours(List<Integer> bananas, Integer maxHoursAllowed) {
        /*
            Time complexity is O(n*log(max(arr))) and space complexity is O(1).
         */
        int low = 1, high = Collections.max(bananas);
        while (low <= high) {
            int mid = (low + (high - low)/2);
            boolean isPossible = ifEatingPossible(bananas, maxHoursAllowed, mid);
            if (isPossible) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private static boolean ifEatingPossible(List<Integer> bananas, Integer maxHoursAllowed, int mid) {
        double hoursTaken = 0;
        for (Integer stack : bananas) {
            hoursTaken += (int) Math.ceil((double) stack /mid);
            if (hoursTaken > maxHoursAllowed) return false;
        }
        return true;
    }
}
