// Problem link - https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1
// Solution - https://www.youtube.com/watch?v=oO5uLE7EUlM


package Arrays.Problem24;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
    public static Integer getLongestConsecutiveSequence(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Set<Integer> set = new HashSet<>(arr);
        Integer longestLength = Integer.MIN_VALUE;
        for (Integer i : set) {
            if (set.contains(i - 1)) {
                continue;
            }
            int count = 1;
            while (set.contains(i + 1)) {
                count += 1;
                i += 1;
            }
            longestLength = Math.max(longestLength, count);
        }
        return longestLength;
    }

    public static void main(String[] args) {
        System.out.println(getLongestConsecutiveSequence(Arrays.asList(2, 6, 1, 9, 4, 5, 3)));
        System.out.println(getLongestConsecutiveSequence(Arrays.asList(1, 9, 3, 10, 4, 20, 2)));
        System.out.println(getLongestConsecutiveSequence(Arrays.asList(15, 13, 12, 14, 11, 10, 9)));
    }
}
