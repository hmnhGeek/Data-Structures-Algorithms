package SlidingWindows.L6;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    private static Integer getDistinctCharactersCount(Map<Character, Integer> d) {
        Integer count = 0;
        for (Character c : d.keySet()) {
            if (d.get(c) > 0) {
                count += 1;
            }
        }
        return count;
    }

    public static String getLongestSubstring(String string, Integer k) {
        int n = string.length();
        Map<Character, Integer> d = new HashMap<>();
        for (Character c : string.toCharArray()) {
            d.put(c, 0);
        }
        int left = 0, right = 0;

        int longestLength = 0;
        int startIndex = -1;

        while (right < n) {
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);
            if (getDistinctCharactersCount(d) > k) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            if (getDistinctCharactersCount(d) <= k) {
                startIndex = left;
                longestLength = Math.max(longestLength, right - left + 1);
            }
            right += 1;
        }

        return startIndex != -1 ? string.substring(startIndex, startIndex + longestLength) : "";
    }

    public static void main(String[] args) {
        System.out.println(getLongestSubstring("aaabbccd", 2));
    }
}
