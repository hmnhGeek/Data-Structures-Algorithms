// Problem link - https://www.geeksforgeeks.org/dsa/rabin-karp-algorithm-for-pattern-searching/


package Strings.Problem18;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    private static Integer computeHash(String string, Boolean useBasic) {
        if (useBasic) {
            int hashValue = 0;
            for (int i = 0; i < string.length(); i += 1) {
                hashValue += (string.charAt(i) - 'a');
            }
            return hashValue;
        }
        int hashValue = 0, base = 26, prime = 101, pow = 0;
        for (int i = string.length() - 1; i >= 0; i -= 1) {
            hashValue += (int) (((string.charAt(i) - 'a') * Math.pow(base, pow)) % prime);
            pow += 1;
        }
        return hashValue;
    }

    public static List<Integer> rabinKarp(String text, String pattern) {
        /*
            Time complexity is O(nm) and space complexity is O(m).
         */

        // get the lengths of text and pattern for later use.
        int textLength = text.length(), patternLength = pattern.length();

        // we will store the start index of every match in a list and return it.
        List<Integer> matches = new ArrayList<>();

        // compute the pattern hash which will remain the same for entire run.
        int patternHash = computeHash(pattern, Boolean.FALSE);

        // starting from 0th index, go up till text_length - pattern_length in the text for computing
        // window hashes.
        for (int i = 0; i <= textLength - patternLength; i += 1) {
            // extract the window and compute its hash value.
            String currentWindow = text.substring(i, i + patternLength);
            int currentWindowHash = computeHash(currentWindow, Boolean.FALSE);

            // if the hash value matches and the window matches with pattern, add it to the result list.
            if (currentWindowHash == patternHash) {
                if (currentWindow.equals(pattern)) {
                    matches.add(i);
                }
            }
        }
        return matches;
    }

    public static void main(String[] args) {
        System.out.println(rabinKarp("ababdabacdababcabab", "ababcabab"));
        System.out.println(rabinKarp("geeksforgeeks", "geek"));
        System.out.println(rabinKarp("aabaacaadaabaaba", "aaba"));
        System.out.println(rabinKarp("ababcabcababc", "abc"));
        System.out.println(rabinKarp("hello", "ll"));
    }
}
