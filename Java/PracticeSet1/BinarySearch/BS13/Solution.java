package PracticeSet1.BinarySearch.BS13;

import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getMinDayToBloom(
                List.of(7, 7, 7, 7, 13, 11, 12, 7), 2, 3));

        System.out.println(getMinDayToBloom(
                List.of(1, 10, 3, 10, 2), 3, 2));

        System.out.println(getMinDayToBloom(
                List.of(1, 2, 1, 2, 7, 2, 2, 3, 1), 2, 3));

        System.out.println(getMinDayToBloom(
                List.of(1, 1, 1, 1), 1, 1));

        System.out.println(getMinDayToBloom(
                List.of(3, 4, 2, 7, 13, 8, 5), 3, 2));

        System.out.println(getMinDayToBloom(
                List.of(5, 5, 5, 5, 10, 5, 5), 2, 3));
    }

    public static Integer getMinDayToBloom(List<Integer> arr, int m, int k) {
        if (m * k > arr.size()) return -1;
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

    private static boolean checkIfPossible(List<Integer> arr, int mid, int m, int k) {
        int countOfBouquetsFormed = 0;
        boolean bouquetFormingRightNow = false;
        int i = 0;
        while (i < arr.size()){
            if (arr.get(i) <= mid) {
                if (!bouquetFormingRightNow) {
                    bouquetFormingRightNow = true;
                    int flowersUsed = 1;
                    i += 1;
                    while (flowersUsed != k && i < arr.size() && arr.get(i) <= mid) {
                        flowersUsed += 1;
                        i += 1;
                    }
                    if (flowersUsed == k) {
                        countOfBouquetsFormed += 1;
                        bouquetFormingRightNow = false;
                        continue;
                    } else {
                        bouquetFormingRightNow = false;
                    }
                }
            }
            i += 1;
        }
        return countOfBouquetsFormed >= m;
    }
}
