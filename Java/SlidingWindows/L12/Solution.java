package SlidingWindows.L12;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String getMinWindowSubstring(String s, String t) {
        Map<Character, Integer> d = getCharacterMap(s);
        Map<Character, Integer> d0 = getCharacterMap(t);
        for (Character c : t.toCharArray()) {
            d0.put(c, d0.get(c) + 1);
        }
        int n = s.length();
        int length = 0;
        int left = 0, right = 0;
        int startIndex = -1;
        while (right < n) {
            d.put(s.charAt(right), d.get(s.charAt(right)) + 1);
            while (matchesPresent(d, d0)) {
                length = right - left + 1;
                startIndex = left;
                d.put(s.charAt(left), d.get(s.charAt(left)) - 1);
                left += 1;
            }
            right += 1;
        }
        if (startIndex != -1) {
            return s.substring(startIndex, startIndex + length);
        }
        return "";
    }

    private static boolean matchesPresent(Map<Character, Integer> d, Map<Character, Integer> t) {
        for (Character c : t.keySet()) {
            if (d.get(c) < t.get(c)) {
                return false;
            }
        }
        return true;
    }

    private static Map<Character, Integer> getCharacterMap(String s) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character character : s.toCharArray()) {
            d.putIfAbsent(character, 0);
        }
        return d;
    }

    public static void main(String[] args) {
        System.out.println(Solution.getMinWindowSubstring("ddaaabbca", "abc"));
        System.out.println(Solution.getMinWindowSubstring("timetopractice", "toc"));
        System.out.println(Solution.getMinWindowSubstring("zoomlazapzo", "oza"));
        System.out.println(Solution.getMinWindowSubstring("ADOBECODEBANC", "ABC"));
        System.out.println(Solution.getMinWindowSubstring("a", "a"));
        System.out.println(Solution.getMinWindowSubstring("a", "aa"));
        System.out.println(Solution.getMinWindowSubstring("ABBXC", "BXC"));
    }
}
