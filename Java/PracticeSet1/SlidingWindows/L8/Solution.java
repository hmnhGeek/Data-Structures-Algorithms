// Problem link - https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1
// Solution - https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8


package PracticeSet1.SlidingWindows.L8;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getLongestRepeating("AABABBA", 2));
        System.out.println(getLongestRepeating("ABAB", 2));
        System.out.println(getLongestRepeating("AABABBA", 1));
        System.out.println(getLongestRepeating("ADBD", 1));
        System.out.println(getLongestRepeating("AAABBCCD", 2));
        System.out.println(getLongestRepeating("ABABA", 2));
        System.out.println(getLongestRepeating("HHHHHH", 4));
    }

    private static Integer getMaxFromValues(Map<Character, Integer> d) {
        return Collections.max(d.values());
    }

    private static Map<Character, Integer> getFreqMap(String string) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character character : string.toCharArray()) {
            d.put(character, 0);
        }
        return d;
    }

    public static String getLongestRepeating(String string, Integer k) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        if (k < 0) return null;
        Map<Character, Integer> freqMap = getFreqMap(string);
        Integer length = 0;
        Integer startIndex = -1;
        int left = 0, right = 0;
        int n = string.length();
        while (right < n) {
            Character character = string.charAt(right);
            freqMap.put(character, freqMap.get(character) + 1);
            if (right - left + 1 - getMaxFromValues(freqMap) > k) {
                freqMap.put(string.charAt(left), freqMap.get(string.charAt(left)) - 1);
                left += 1;
            } else {
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
}
