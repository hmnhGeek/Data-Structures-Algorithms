package Strings;

import java.util.HashMap;

class Solution {
    public static void main(String[] args) {
        System.out.println(stepsToTransform("ABD", "BAD"));
        System.out.println(stepsToTransform("EACBD", "EABCD"));
    }

    /**
     *
     * @param s A string whose frequency map needs to be created.
     * @return A frequency map of the string.
     */
    private static HashMap<Character, Integer> counter(String s) {
        /*
        * Time complexity is O(n) and space complexity is O(n).
        * */

        HashMap<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }
        return frequencyMap;
    }

    private static Integer stepsToTransform(String s1, String s2) {
        // check if both the strings are permutations of each other or not.
        HashMap<Character, Integer> map1 = counter(s1);
        HashMap<Character, Integer> map2 = counter(s2);
        if (!map1.equals(map2)) {
            return -1;
        }

        // store the count of swaps in a variable.
        int count = 0;

        // start looping in the string from the last indices of both the strings.
        int i = s1.length() - 1;
        int j = s2.length() - 1;

        // while string1 is still left...
        while (i >= 0) {
            // if the characters don't match, increment the count but keep `j` at its place.
            if (s1.charAt(i) != s2.charAt(j)) {
                count += 1;
                i -= 1;
            }
            else {
                i -= 1;
                j -= 1;
            }
        }

        // return the count of swaps needed.
        return count;
    }
}