package Strings.Problem7;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getLongestRepeatingSubsequence("axxxy"));
        System.out.println(getLongestRepeatingSubsequence("axxzxy"));
        System.out.println(getLongestRepeatingSubsequence("abc"));
        System.out.println(getLongestRepeatingSubsequence("aab"));
        System.out.println(getLongestRepeatingSubsequence("abcab"));
        System.out.println(getLongestRepeatingSubsequence("ABCBDCD"));
        System.out.println(getLongestRepeatingSubsequence("BCCB"));
    }

    public static Integer getLongestRepeatingSubsequence(String s) {
        /*
            Time complexity is O(mn) and space complexity is O(m).
         */
        int n1 = s.length(), n2 = s.length();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = -1; j < n2; j += 1) {
            prev.put(j, 0);
        }

        for (int i = 0; i < n1; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = -1; j < n2; j += 1) {
                curr.put(j, 0);
            }
            for (int j = 0; j < n2; j += 1) {
                if (s.charAt(i) == s.charAt(j) && i != j) {
                    curr.put(j, 1 + prev.get(j - 1));
                } else {
                    curr.put(j, Math.max(prev.get(j), curr.get(j - 1)));
                }
            }
            prev = curr;
        }

        return prev.get(n2 - 1);
    }
}
