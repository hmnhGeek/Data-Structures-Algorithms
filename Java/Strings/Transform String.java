package Strings;

import java.util.HashMap;

class Solution {
    public static void main(String[] args) {
        System.out.println(stepsToTransform("ABD", "BAD"));
        System.out.println(stepsToTransform("EACBD", "EABCD"));
    }

    private static HashMap<Character, Integer> counter(String s) {
        HashMap<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }
        return frequencyMap;
    }

    private static Integer stepsToTransform(String s1, String s2) {
        HashMap<Character, Integer> map1 = counter(s1);
        HashMap<Character, Integer> map2 = counter(s2);
        if (!map1.equals(map2)) {
            return -1;
        }
        int count = 0;
        int i = s1.length() - 1;
        int j = s2.length() - 1;
        while (i >= 0) {
            if (s1.charAt(i) != s2.charAt(j)) {
                count += 1;
                i -= 1;
            }
            else {
                i -= 1;
                j -= 1;
            }
        }
        return count;
    }
}