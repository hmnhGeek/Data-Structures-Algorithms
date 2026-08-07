package PracticeSet1.SlidingWindows.L4;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getMaxConsecutiveOnes(List<Integer> arr, int k) {
        if (k < 0) return null;
        int n = arr.size();
        int left = 0, right = 0, length = 0, startIndex = -1, countZeros = 0;
        while (right < n) {
            if (arr.get(right) == 0) {
                countZeros += 1;
            }
            while (countZeros > k) {
                if (arr.get(left) == 0) {
                    countZeros -= 1;
                }
                left += 1;
            }
            if (right - left + 1 > length) {
                length = right - left + 1;
                startIndex = left;
            }
            right += 1;
        }
        if (startIndex != -1) {
            return arr.subList(startIndex, startIndex + length);
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(getMaxConsecutiveOnes(Arrays.asList(1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0), 2));
        System.out.println(getMaxConsecutiveOnes(Arrays.asList(0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1), 3));
        System.out.println(getMaxConsecutiveOnes(Arrays.asList(0, 1, 1, 0, 1, 0, 1, 1), 2));
        System.out.println(getMaxConsecutiveOnes(Arrays.asList(1, 1, 1, 0, 0, 1, 1, 1, 0, 1), 1));
    }
}
