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
        if (k < 0) return 0;
        int n = string.length();
        int left = 0, right = 0;
        Map<Character, Integer> d = new HashMap<>();
        d.put('a', 0);
        d.put('b', 0);
        d.put('c', 0);
        int count = 0;
        while (right < n) {
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);
            while (characterCount(d) > k) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            if (characterCount(d) <= k) {
                count += (right - left + 1);
            }
            right += 1;
        }
        return count;
    }


    public static Integer allThreeCharacters(String string) {
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
