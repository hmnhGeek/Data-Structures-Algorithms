// Problem link - https://leetcode.com/problems/longest-common-prefix/description/


package Strings.Problem27;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static String getLCP(List<String> strings) {
        /*
            Time complexity is O(minLength * n) and space complexity is O(1).
         */
        int minLength = strings.stream()
                .mapToInt(String::length)
                .min()
                .orElse(0);
        int j = 0;
        StringBuilder result = new StringBuilder();
        Character curr = null;
        while (j < minLength) {
            for (int i = 0; i < strings.size(); i += 1) {
                // for current string, get the character at index j.
                char temp = strings.get(i).charAt(j);

                // if this is a new character, set curr value to it.
                if (curr == null) {
                    curr = temp;
                } else if (curr != temp) {
                    // if it's not a new character, but it does not match with previous characters at j index, return
                    return result.toString();
                }

                // if at the last string, reset curr (for next j) and add temp to result.
                if (i == strings.size() - 1) {
                    result.append(temp);
                    curr = null;
                }
            }
            j += 1;
        }

        return result.toString();
    }

    public static void main(String[] args) {
        System.out.println(getLCP(Arrays.asList("flower","flow","flight")));
        System.out.println(getLCP(Arrays.asList("dog","racecar","car")));
        System.out.println(getLCP(Arrays.asList("abcdefgh", "aefghijk", "abcefgh")));
        System.out.println(getLCP(Arrays.asList("abab", "ab", "abcd")));
    }
}
