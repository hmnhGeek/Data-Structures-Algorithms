package PracticeSet1.BinarySearch.BS14;

import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getSmallestDivisor(List.of(1, 2, 5, 9), 6));
        System.out.println(getSmallestDivisor(List.of(1, 2, 3, 4, 5), 8));
        System.out.println(getSmallestDivisor(List.of(8, 4, 2, 3), 10));
        System.out.println(getSmallestDivisor(List.of(2, 3, 5, 7, 11), 11));
        System.out.println(getSmallestDivisor(List.of(44, 22, 33, 11, 1), 5));
        System.out.println(getSmallestDivisor(List.of(1, 1, 1, 1), 4));
    }

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

    private static boolean checkPossible(List<Integer> arr, int mid, int threshold) {
        int sum = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            sum += (int) Math.ceil((double) arr.get(i) /mid);
        }
        return sum <= threshold;
    }
}
