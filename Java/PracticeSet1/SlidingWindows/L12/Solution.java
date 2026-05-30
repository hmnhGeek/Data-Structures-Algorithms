// Problem link - https://leetcode.com/problems/minimum-window-substring/description/
// Solution - https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12


package PracticeSet1.SlidingWindows.L12;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String getMinWindowSubstring(String string, String pattern) {
        /*
            Overall time complexity is O(26n) and space complexity is O(26).
         */
        Map<Character, Integer> t = getDictionary(pattern, Boolean.TRUE);
        Map<Character, Integer> d = getDictionary(string, Boolean.FALSE);
        Integer startIndex = -1, left = 0, right = 0, length = 0;
        int n = string.length();
        while (right < n) {
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);
            while (thereIsAMatch(d, t)) {
                length = right - left + 1;
                startIndex = left;
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            right += 1;
        }
        if (startIndex != -1) {
            return string.substring(startIndex, startIndex + length);
        }
        return "";
    }

    private static boolean thereIsAMatch(Map<Character, Integer> d, Map<Character, Integer> t) {
        for (Character c : t.keySet()) {
            if (d.get(c) < t.get(c)) return false;
        }
        return true;
    }

    private static Map<Character, Integer> getDictionary(String string, Boolean mapValues) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character character : string.toCharArray()) {
            d.put(character, 0);
        }
        if (!mapValues) {
            return d;
        }
        for (Character c : string.toCharArray()) {
            d.put(c, d.get(c) + 1);
        }
        return d;
    }

    public static void main(String[] args) {
        System.out.println(SlidingWindows.L12.Solution.getMinWindowSubstring("ddaaabbca", "abc"));
        System.out.println(SlidingWindows.L12.Solution.getMinWindowSubstring("timetopractice", "toc"));
        System.out.println(SlidingWindows.L12.Solution.getMinWindowSubstring("zoomlazapzo", "oza"));
        System.out.println(SlidingWindows.L12.Solution.getMinWindowSubstring("ADOBECODEBANC", "ABC"));
        System.out.println(SlidingWindows.L12.Solution.getMinWindowSubstring("a", "a"));
        System.out.println(SlidingWindows.L12.Solution.getMinWindowSubstring("a", "aa"));
        System.out.println(SlidingWindows.L12.Solution.getMinWindowSubstring("ABBXC", "BXC"));
    }
}
