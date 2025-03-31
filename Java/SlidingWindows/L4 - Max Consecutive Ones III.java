// Problem link - https://www.naukri.com/code360/problems/maximum-consecutive-ones_3843993
// Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


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
        /**
         * Time complexity is O(n) and space complexity is O(1).
         */

        // edge case
        if (k < 0 || k > arr.size()) {
            return new ArrayList<>();
        }

        // define the window variables
        int n = arr.size();
        int left = 0, right = 0;

        // define tracking variables
        int zeroCount = 0;

        // define result variables
        int longestLength = 0;
        int startIndex = -1;

        // while there is ground to cover...
        while (right < n) {
            // if the right-indexed value is a 0, increment the zero-count.
            if (arr.get(right).equals(0)) {
                zeroCount += 1;
            }

            // if the zero count has exceeded the prescribed limit, shrink just one unit from left.
            if (zeroCount > k) {
                // also decrement 0 count if a 0 is removed from the window.
                if (arr.get(left).equals(0)) {
                    zeroCount -= 1;
                }
                left += 1;
            }

            // if the zero count is within limit, then update the result variables.
            if (zeroCount <= k) {
                if (longestLength < right - left + 1) {
                    longestLength = right - left + 1;
                    startIndex = left;
                }
            }

            // increment the right index.
            right += 1;
        }

        // return the sublist.
        return startIndex != -1 ? arr.subList(startIndex, startIndex + longestLength) : new ArrayList<>();
    }
}