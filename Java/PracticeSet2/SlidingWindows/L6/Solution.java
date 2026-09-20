package PracticeSet2.SlidingWindows.L6;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String longestSubstring(String string, int k) {
        int left = 0, right = 0;
        int length = 0, startIndex = -1;
        Map<Character, Integer> d = new HashMap<>();
        for (Character c : string.toCharArray()) {
            d.put(c, 0);
        }
        while (right < string.length()) {
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);
            int count = countUniques(d);
            if (count > k) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            if (count <= k) {
                if (right - left + 1 > length) {
                    length = right - left + 1;
                    startIndex = left;
                }
            }
            right += 1;
        }
        if (startIndex != -1) {
            return string.substring(startIndex, startIndex + length);
        }
        return "";
    }

    private static int countUniques(Map<Character, Integer> d) {
        int count = 0;
        for (Character c : d.keySet()) {
            if (d.get(c) > 0) {
                count += 1;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(longestSubstring("aaabbccd", 2));
        System.out.println(longestSubstring("abbbbbbc", 2));
        System.out.println(longestSubstring("abcddefg", 3));
        System.out.println(longestSubstring("aaaaaaaa", 3));
        System.out.println(longestSubstring("abcefg", 1));
        System.out.println(longestSubstring("aabbcc", 1));
        System.out.println(longestSubstring("aabbcc", 2));
        System.out.println(longestSubstring("aabbcc", 3));
        System.out.println(longestSubstring("aaabbb", 3));
    }
}
