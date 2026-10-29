// Problem link - https://www.naukri.com/code360/problems/capacity-to-ship-packages-within-d-days_1229379
// Solution - https://www.youtube.com/watch?v=MG-Ac4TAvTY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17


package PracticeSet1.BinarySearch.BS15;

import java.util.Collections;
import java.util.List;

public class Solution {
    public static Integer getShipCapacity(List<Integer> weights, Integer numDaysThreshold) {
        /*
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
         */
        int low = Collections.max(weights), high = weights.stream()
                .mapToInt(Integer::intValue)
                .sum();
        
        while (low <= high) {
            int mid = (low + (high - low)/2);
            boolean isPossibleToShipWithinThresholdDays = checkIfPossible(weights, mid, numDaysThreshold);
            if (isPossibleToShipWithinThresholdDays) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return low;
    }

    private static boolean checkIfPossible(List<Integer> weights, int mid, Integer numDaysThreshold) {
        int daysUsed = 0;
        int weightShipped = 0;
        for (int i = 0; i < weights.size(); i += 1) {
            weightShipped += weights.get(i);
            if (weightShipped > mid) {
                daysUsed += 1;
                weightShipped = weights.get(i);
            }
        }
        if (weightShipped > 0) {
            daysUsed += 1;
            weightShipped = 0;
        }
        return daysUsed <= numDaysThreshold;
    }

    public static void main(String[] args) {
        System.out.println(getShipCapacity(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 5));
        System.out.println(getShipCapacity(List.of(5, 4, 5, 2, 3, 4, 5, 6), 5));
        System.out.println(getShipCapacity(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 1));
        System.out.println(getShipCapacity(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 0));
        System.out.println(getShipCapacity(List.of(3, 2, 2, 4, 1, 4), 3));
        System.out.println(getShipCapacity(List.of(1, 2, 3, 1, 1), 4));
    }
}
