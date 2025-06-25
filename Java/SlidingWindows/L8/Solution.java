package SlidingWindows.L8;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String longestCharacterReplacement(String string, Integer k) {
        int n = string.length();
        int left = 0, right = 0;
        int longestLength = 0;
        int startIndex = -1;
        Map<Character, Integer> d = getCounter(string);
        while (right < n) {
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);
            if (right - left + 1 - Collections.max(d.values()) > k) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            if (right - left + 1 - Collections.max(d.values()) <= k) {
                longestLength = Math.max(longestLength, right - left + 1);
                startIndex = left;
            }
            right += 1;
        }
        return startIndex != -1 ? string.substring(startIndex, startIndex + longestLength) : "";
    }

    private static Map<Character, Integer> getCounter(String string) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character character : string.toCharArray()) {
            d.put(character, 0);
        }
        return d;
    }

    public static void main(String[] args) {
        System.out.println(longestCharacterReplacement("AABABBA", 2));
        System.out.println(longestCharacterReplacement("ABAB", 2));
        System.out.println(longestCharacterReplacement("AABABBA", 1));
        System.out.println(longestCharacterReplacement("ADBD", 1));
        System.out.println(longestCharacterReplacement("AAABBCCD", 2));
        System.out.println(longestCharacterReplacement("ABABA", 2));
        System.out.println(longestCharacterReplacement("HHHHHH", 4));
    }
}
