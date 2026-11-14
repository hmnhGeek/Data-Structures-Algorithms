package Strings.Problem27;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static String getLCP(List<String> strings) {
        int minLength = strings.stream()
                .mapToInt(String::length)
                .min()
                .orElse(0);
        int j = 0;
        StringBuilder result = new StringBuilder();
        Character curr = null;
        while (j < minLength) {
            for (int i = 0; i < strings.size(); i += 1) {
                char temp = strings.get(i).charAt(j);
                if (curr == null) {
                    curr = temp;
                } else {
                    if (curr != temp) {
                        break;
                    }
                }
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
