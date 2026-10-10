package DynamicProgramming.DP45;

import java.util.*;

public class Solution {
    private static boolean compareStrings(String s1, String s2) {
        if (s1.length() != s2.length() + 1) return false;
        int first = 0, second = 0;
        while (first < s1.length()) {
            if (second < s2.length() && s1.charAt(first) == s2.charAt(second)) {
                first += 1;
                second += 1;
            } else {
                first += 1;
            }
        }
        if (first == s1.length() && second == s2.length()) return true;
        return false;
    }

    public static List<String> getLongestStringChain(List<String> strings) {
        strings.sort(Comparator.comparingInt(String::length));
        Map<Integer, Integer> dp = new HashMap<>();
        Map<Integer, Integer> parent = new HashMap<>();
        for (int i = 0; i < strings.size(); i += 1) {
            dp.put(i, 1);
            parent.put(i, i);
        }
        for (int i = 1; i < strings.size(); i += 1) {
            for (int j = 0; j < i; j += 1) {
                if (compareStrings(strings.get(i), strings.get(j)) && dp.get(j) + 1 > dp.get(i)) {
                    dp.put(i, dp.get(j) + 1);
                    parent.put(i, j);
                }
            }
        }
        int indexOfLongest = getIndexOfLongest(dp);
        int startIndex = indexOfLongest;
        List<String> result = new ArrayList<>();
        while (startIndex != parent.get(startIndex)) {
            result.add(strings.get(startIndex));
            startIndex = parent.get(startIndex);
        }
        result.add(strings.get(startIndex));
        return result.reversed();
    }

    private static int getIndexOfLongest(Map<Integer, Integer> dp) {
        int result = 0;
        for (Integer key : dp.keySet()) {
            if (dp.get(key) > dp.get(result)) {
                result = key;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getLongestStringChain(
                Arrays.asList("x", "xx", "y", "xyx")));

        System.out.println(getLongestStringChain(
                Arrays.asList("m", "nm", "mmm")));

        System.out.println(getLongestStringChain(
                Arrays.asList("a", "bc", "ad", "adc", "bcd")));

        System.out.println(getLongestStringChain(
                Arrays.asList("a", "b", "ba", "bca", "bda", "bdca")));

        System.out.println(getLongestStringChain(
                Arrays.asList("xbc", "pcxbcf", "xb", "cxbc", "pcxbc")));
    }
}
