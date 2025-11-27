// Problem link - https://www.naukri.com/code360/problems/smallest-divisor-with-the-given-limit_1755882
// Solution - https://www.youtube.com/watch?v=UvBKTVaG6U8&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=15


package BinarySearch.BS14;

import java.util.Collections;
import java.util.List;

public class Solution {
    public static Integer getSmallestDivisor(List<Integer> arr, Integer threshold) {
        /*
            Time complexity is O(n * log(max)) and space complexity is O(1).
         */
        int low = 1, high = Collections.max(arr);
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int value = (int) getQuotients(arr, mid);
            if (value <= threshold) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private static double getQuotients(List<Integer> arr, Integer mid) {
        double result = 0;
        for (Integer integer : arr) {
            result += Math.ceil((double) integer /mid);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(Solution.getSmallestDivisor(List.of(1, 2, 5, 9), 6));
        System.out.println(Solution.getSmallestDivisor(List.of(1, 2, 3, 4, 5), 8));
        System.out.println(Solution.getSmallestDivisor(List.of(8, 4, 2, 3), 10));
        System.out.println(Solution.getSmallestDivisor(List.of(2, 3, 5, 7, 11), 11));
        System.out.println(Solution.getSmallestDivisor(List.of(44, 22, 33, 11, 1), 5));
        System.out.println(Solution.getSmallestDivisor(List.of(1, 1, 1, 1), 4));
    }
}
