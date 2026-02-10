// Problem link - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
// Solution - https://www.youtube.com/watch?v=xtqN4qlgr8s&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=7


package PracticeSet1.SlidingWindows.L7;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(allThreeCharacters("bbacba"));
        System.out.println(allThreeCharacters("abcabc"));
        System.out.println(allThreeCharacters("aaacb"));
        System.out.println(allThreeCharacters("abc"));
        System.out.println(allThreeCharacters("aabbabab"));
    }

    public static Integer allThreeCharacters(String string) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        Map<Character, Integer> d = new HashMap<>();
        d.put('a', 0);
        d.put('b', 0);
        d.put('c', 0);
        int left = 0, right = 0;
        int result = 0;
        int n = string.length();
        while (right < n) {
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);
            while (d.get('a') > 0 && d.get('b') > 0 && d.get('c') > 0) {
                result += (n - right);
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            right += 1;
        }
        while (d.get('a') > 0 && d.get('b') > 0 && d.get('c') > 0) {
            result += (n - right);
            d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
            left += 1;
        }
        return result;
    }
}
