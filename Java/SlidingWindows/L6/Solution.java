// Problem link - https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
// Solution - https://www.youtube.com/watch?v=teM9ZsVRQyc&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=6

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
        /*
            Time complexity is O(26 * n) and space complexity is O(26).
         */

        // define window variables
        int n = string.length();
        int left = 0, right = 0;

        // define tracking variable
        Map<Character, Integer> d = new HashMap<>();
        for (Character c : string.toCharArray()) {
            d.put(c, 0);
        }

        // define result variables
        int longestLength = 0;
        int startIndex = -1;

        // while there is ground to cover...
        while (right < n) {
            // increment the right indexed value
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);

            // if the unique characters > k, then shrink from left but just 1 unit.
            if (getDistinctCharactersCount(d) > k) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }

            // else update the resulting variables.
            if (getDistinctCharactersCount(d) <= k) {
                startIndex = left;
                longestLength = Math.max(longestLength, right - left + 1);
            }

            // increment right index
            right += 1;
        }

        // return the substring.
        return startIndex != -1 ? string.substring(startIndex, startIndex + longestLength) : "";
    }

    public static void main(String[] args) {
        System.out.println(getLongestSubstring("aaabbccd", 2));
        System.out.println(getLongestSubstring("abbbbbbc", 2));
        System.out.println(getLongestSubstring("abcddefg", 3));
        System.out.println(getLongestSubstring("aaaaaaaa", 3));
        System.out.println(getLongestSubstring("abcefg", 1));
        System.out.println(getLongestSubstring("aabbcc", 1));
        System.out.println(getLongestSubstring("aabbcc", 2));
        System.out.println(getLongestSubstring("aabbcc", 3));
        System.out.println(getLongestSubstring("aaabbb", 3));
    }
}
