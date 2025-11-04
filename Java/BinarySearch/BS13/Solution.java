package BinarySearch.BS13;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(Solution.getMinDays(Arrays.asList(7, 7, 7, 7, 13, 11, 12, 7), 2, 3));
        System.out.println(Solution.getMinDays(Arrays.asList(1, 2, 1, 2, 7, 2, 2, 3, 1), 2, 3));
        System.out.println(Solution.getMinDays(Arrays.asList(1, 1, 1, 1), 1, 1));
        System.out.println(Solution.getMinDays(Arrays.asList(1, 10, 3, 10, 2), 3, 1));
        System.out.println(Solution.getMinDays(Arrays.asList(1, 10, 3, 10, 2), 3, 2));
        System.out.println(Solution.getMinDays(Arrays.asList(5, 5, 5, 12, 10, 5, 5), 2, 3));
        System.out.println(Solution.getMinDays(Arrays.asList(7, 7, 3, 7, 7, 7), 1, 4));
    }

    public static Integer getMinDays(List<Integer> arr, Integer m, Integer k) {
        int n = arr.size();
        if (n < m * k) return -1;
        int low = 0, high = Collections.max(arr);
        while (low <= high) {
            int mid = (low + (high - low)/2);
            boolean isPossible = canBouquetBeMade(arr, mid, m, k);
            if (isPossible) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private static boolean canBouquetBeMade(List<Integer> arr, int mid, Integer m, Integer k) {
        int bouquetsMade = 0;
        int flowersCollected = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            if (arr.get(i) <= mid) {
                flowersCollected += 1;
            } else {
                if (flowersCollected < k) {
                    flowersCollected = 0;
                    continue;
                }
            }
            if (flowersCollected == k) {
                bouquetsMade += 1;
                flowersCollected = 0;
            }
        }
        return bouquetsMade >= m;
    }
}
