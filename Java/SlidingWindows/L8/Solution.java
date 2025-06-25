// Problem link - https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1
// Solution - https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8

package SlidingWindows.L8;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String longestCharacterReplacement(String string, Integer k) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */

        // define window variables
        int n = string.length();
        int left = 0, right = 0;

        // define result variables
        int longestLength = 0;
        int startIndex = -1;

        // define tracking variables
        Map<Character, Integer> d = getCounter(string);

        // while there is ground to cover...
        while (right < n) {
            // increment the right indexed value
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);

            // if the replacement count is greater than k
            if (right - left + 1 - Collections.max(d.values()) > k) {
                // decrement only one unit from left
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }

            // if the replacement count is within k, update the result variables
            if (right - left + 1 - Collections.max(d.values()) <= k) {
                longestLength = Math.max(longestLength, right - left + 1);
                startIndex = left;
            }

            // increment the right index
            right += 1;
        }

        // return the substring
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
