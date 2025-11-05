// Problem link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
// Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


package SlidingWindows.L3;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String longestSubstring(String string) {
        /*
            Time complexity is O(26*n) and space complexity is O(26).
         */
        int n = string.length();
        int left = 0, right = 0;
        int length = 0;
        int startIndex = -1;
        Map<Character, Integer> d = getCharacterMap(string);
        while (right < n) {
            Character character = string.charAt(right);
            d.put(character, d.get(character) + 1);
            if (anyDuplicatesFound(d)) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            if (right - left + 1 > length) {
                length = right - left + 1;
                startIndex = left;
            }
            right += 1;
        }
        if (startIndex != -1) {
            return string.substring(startIndex, startIndex + length);
        }
        return "";
    }

    private static boolean anyDuplicatesFound(Map<Character, Integer> d) {
        for (Character character : d.keySet()) {
            if (d.get(character) > 1) {
                return true;
            }
        }
        return false;
    }

    private static Map<Character, Integer> getCharacterMap(String string) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character character : string.toCharArray()) {
            d.put(character, 0);
        }
        return d;
    }

    public static void main(String[] args) {
        System.out.println(longestSubstring("cadbzabcd"));
        System.out.println(longestSubstring("abcabcbb"));
        System.out.println(longestSubstring("bbbbb"));
        System.out.println(longestSubstring("pwwkew"));
        System.out.println(longestSubstring("ABCBC"));
        System.out.println(longestSubstring("GEEKSFORGEEKS"));
        System.out.println(longestSubstring("mississippi"));
    }
}
