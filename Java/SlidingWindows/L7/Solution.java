// Problem link - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
// Solution - https://www.youtube.com/watch?v=xtqN4qlgr8s&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=7

package SlidingWindows.L7;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    private static Integer characterCount(Map<Character, Integer> d) {
        int count = 0;
        for (Character c : d.keySet()) {
            if (d.get(c) > 0) count += 1;
        }
        return count;
    }

    public static Integer solve(String string, Integer k) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */

        // edge case
        if (k < 0) return 0;

        // get window variables
        int n = string.length();
        int left = 0, right = 0;

        // get tracking variable
        Map<Character, Integer> d = new HashMap<>();
        d.put('a', 0);
        d.put('b', 0);
        d.put('c', 0);

        // get result variable
        int count = 0;

        // while there is ground to cover
        while (right < n) {
            // increment right indexed count
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);

            // while count of characters exceed k, shrink from left
            while (characterCount(d) > k) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }

            // else, update the count variable
            if (characterCount(d) <= k) {
                count += (right - left + 1);
            }

            // increment right index.
            right += 1;
        }

        // return the count.
        return count;
    }


    public static Integer allThreeCharacters(String string) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */

        return solve(string, 3) - solve(string, 2);
    }

    public static void main(String[] args) {
        System.out.println(allThreeCharacters("bbacba"));
        System.out.println(allThreeCharacters("abcabc"));
        System.out.println(allThreeCharacters("aaacb"));
        System.out.println(allThreeCharacters("abc"));
        System.out.println(allThreeCharacters("aabbabab"));
    }
}
