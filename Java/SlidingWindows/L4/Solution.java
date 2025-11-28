// Problem link - https://leetcode.com/problems/max-consecutive-ones-iii/description/
// Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


package SlidingWindows.L4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getMaxConsecutiveOnes(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = arr.size();
        int left = 0, right = 0;
        int zerosUsed = 0;
        int startIndex = -1;
        int length = 0;

        while (right < n) {
            if (arr.get(right).equals(0)) {
                zerosUsed += 1;
            }
            if (zerosUsed > k) {
                if (arr.get(left).equals(0)) {
                    zerosUsed -= 1;
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
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println((Solution.getMaxConsecutiveOnes(Arrays.asList(1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0), 2)));
        System.out.println((Solution.getMaxConsecutiveOnes(Arrays.asList(0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1), 3)));
        System.out.println((Solution.getMaxConsecutiveOnes(Arrays.asList(0, 1, 1, 0, 1, 0, 1, 1), 2)));
        System.out.println((Solution.getMaxConsecutiveOnes(Arrays.asList(1, 1, 1, 0, 0, 1, 1, 1, 0, 1), 1)));
    }
}
