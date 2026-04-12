package PracticeSet1.SlidingWindows.L9;

import java.util.List;

public class Solution {
    private static Integer getLessThanEqualToCount(List<Integer> arr, Integer k) {
        if (k < 0) return 0;
        int n = arr.size();
        int left = 0, right = 0;
        int count = 0, sum = 0;
        while (right < n) {
            sum += arr.get(right);
            while (sum > k) {
                sum -= arr.get(left);
                left += 1;
            }
            count += (right - left + 1);
            right += 1;
        }
        return count;
    }

    public static Integer getSubArrayCount(List<Integer> arr, Integer k) {
        int x = getLessThanEqualToCount(arr, k);
        int y = getLessThanEqualToCount(arr, k - 1);
        return  x - y;
    }

    public static void main(String[] args) {
        System.out.println(Solution.getSubArrayCount(List.of(1, 0, 1, 0, 1), 2));
        System.out.println(Solution.getSubArrayCount(List.of(0, 0, 0, 0, 0), 0));
        System.out.println(Solution.getSubArrayCount(List.of(1, 0, 1, 1, 0, 1), 2));
        System.out.println(Solution.getSubArrayCount(List.of(1, 1, 0, 1, 1), 5));
        System.out.println(Solution.getSubArrayCount(List.of(1, 0, 1, 1, 1, 0, 1), 3));
    }
}
