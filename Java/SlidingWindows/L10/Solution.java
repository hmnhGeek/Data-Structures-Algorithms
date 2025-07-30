package SlidingWindows.L10;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static Integer countLessThanEqualTo(List<Integer> arr, Integer sum) {
        if (sum < 0) return 0;
        int left = 0, right = 0;
        int n = arr.size();
        int tracker = 0, count = 0;
        while (right < n) {
            tracker += (arr.get(right) % 2);
            while (tracker > sum) {
                tracker -= (arr.get(left) % 2);
                left += 1;
            }
            count += (right - left + 1);
            right += 1;
        }
        return count;
    }

    public static Integer getCountNiceSubArrays(List<Integer> arr, Integer sum) {
        return countLessThanEqualTo(arr, sum) - countLessThanEqualTo(arr, sum - 1);
    }

    public static void main(String[] args) {
        System.out.println(Solution.getCountNiceSubArrays(Arrays.asList(1, 1, 2, 1, 1), 3));
        System.out.println(Solution.getCountNiceSubArrays(Arrays.asList(2, 4, 6), 1));
        System.out.println(Solution.getCountNiceSubArrays(Arrays.asList(2, 2, 2, 1, 2, 2, 1, 2, 2, 2), 2));
        System.out.println(Solution.getCountNiceSubArrays(Arrays.asList(2, 2, 5, 6, 9, 2, 11), 2));
        System.out.println(Solution.getCountNiceSubArrays(Arrays.asList(2, 5, 6, 9), 2));
    }
}
