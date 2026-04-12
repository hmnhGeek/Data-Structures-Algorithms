package PracticeSet1.SlidingWindows.L10;

import java.util.List;

public class Solution {
    public static Integer getCountLessThanEqualTo(List<Integer> arr, Integer k) {
        if (k < 0) return 0;
        int left = 0, right = 0;
        int count = 0, sum = 0;
        int n = arr.size();
        while (right < n) {
            sum += (arr.get(right) % 2);
            while (sum > k) {
                sum -= (arr.get(left) % 2);
                left += 1;
            }
            count += (right - left + 1);
            right += 1;
        }
        return count;
    }

    public static Integer getNiceSubArraysCount(List<Integer> arr, Integer k) {
        return getCountLessThanEqualTo(arr, k) - getCountLessThanEqualTo(arr, k - 1);
    }

    public static void main(String[] args) {
        System.out.println(Solution.getNiceSubArraysCount(List.of(1, 5, 2, 1, 1), 3));
        System.out.println(Solution.getNiceSubArraysCount(List.of(2, 4, 6), 1));
        System.out.println(Solution.getNiceSubArraysCount(List.of(2, 2, 2, 1, 2, 2, 1, 2, 2, 2), 2));
        System.out.println(Solution.getNiceSubArraysCount(List.of(2, 5, 6, 9), 2));
        System.out.println(Solution.getNiceSubArraysCount(List.of(2, 2, 5, 6, 9, 2, 11), 2));
    }
}
