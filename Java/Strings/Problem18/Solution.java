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
        int textLength = text.length(), patternLength = pattern.length();
        List<Integer> matches = new ArrayList<>();
        int patternHash = computeHash(pattern, Boolean.FALSE);
        for (int i = 0; i <= textLength - patternLength; i += 1) {
            String currentWindow = text.substring(i, i + patternLength);
            int currentWindowHash = computeHash(currentWindow, Boolean.FALSE);
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
