// Problem link - https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

package Strings.Problem3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static List<Character> getDuplicates(String string) {
        /*
            Time complexity is O(n) and space complexity is O(26).
         */
        List<Character> result = new ArrayList<>();
        Map<Character, Integer> counter = new HashMap<>();
        for (Character character : string.toCharArray()) {
            counter.put(character, counter.getOrDefault(character, 0) + 1);
        }
        for (Character character : counter.keySet()) {
            if (counter.get(character) > 1) {
                result.add(character);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getDuplicates("geeksforgeeks"));
    }
}
