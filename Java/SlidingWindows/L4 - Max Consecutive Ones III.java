package SlidingWindows;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public static void main(String[] args) {
        System.out.println(getMaxConsecutiveOnes(Arrays.asList(1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0), 2));
        System.out.println(getMaxConsecutiveOnes(Arrays.asList(0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1), 3));
        System.out.println(getMaxConsecutiveOnes(Arrays.asList(0, 1, 1, 0, 1, 0, 1, 1), 2));
        System.out.println(getMaxConsecutiveOnes(Arrays.asList(1, 1, 1, 0, 0, 1, 1, 1, 0, 1), 1));
    }

    private static List<Integer> getMaxConsecutiveOnes(List<Integer> arr, Integer k) {
        if (k < 0 || k > arr.size()) {
            return new ArrayList<>();
        }
        int n = arr.size();
        int left = 0, right = 0;
        int zeroCount = 0;
        int longestLength = 0;
        int startIndex = -1;
        while (right < n) {
            if (arr.get(right).equals(0)) {
                zeroCount += 1;
            }
            if (zeroCount > k) {
                if (arr.get(left).equals(0)) {
                    zeroCount -= 1;
                }
                left += 1;
            }
            if (zeroCount <= k) {
                if (longestLength < right - left + 1) {
                    longestLength = right - left + 1;
                    startIndex = left;
                }
            }
            right += 1;
        }
        return startIndex != -1 ? arr.subList(startIndex, startIndex + longestLength) : new ArrayList<>();
    }
}