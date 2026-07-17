// Problem link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
// Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


package PracticeSet1.SlidingWindows.L3;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String getLongestSubstring(String string) {
        /*
            Time complexity is O(26*n) and space complexity is O(26).
         */
        int left = 0, right = 0;
        int startIndex = -1;
        int length = 0;
        Map<Character, Integer> d = getFreqMap(string);
        int n = string.length();
        while (right < n) {
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);
            while (!allUniques(d)) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            if (right - left + 1 > length) {
                length = right - left + 1;
                startIndex = left;
            }
            right += 1;
        }
        if (startIndex == -1) return "";
        return string.substring(startIndex, startIndex + length);
    }

    private static boolean allUniques(Map<Character, Integer> d) {
        for (Character c : d.keySet()) {
            if (d.get(c) > 1) {
                return false;
            }
        }
        return true;
    }

    private static Map<Character, Integer> getFreqMap(String string) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character c : string.toCharArray()) {
            d.put(c, 0);
        }
        return d;
    }

    public static void main(String[] args) {
        System.out.println(getLongestSubstring("cadbzabcd"));
        System.out.println(getLongestSubstring("abcabcbb"));
        System.out.println(getLongestSubstring("bbbbb"));
        System.out.println(getLongestSubstring("pwwkew"));
        System.out.println(getLongestSubstring("ABCBC"));
        System.out.println(getLongestSubstring("GEEKSFORGEEKS"));
        System.out.println(getLongestSubstring("mississippi"));
    }
}
