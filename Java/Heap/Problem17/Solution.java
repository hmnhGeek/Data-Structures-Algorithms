// Problem link - https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/


package Heap.Problem17;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("aab", "aaab", "address", "mississippi", "aaabc", "aaabb", "aa", "aaaabc", "abaab", "bbbbbb");
        for (String str : strings) {
            System.out.println(rearrangeCharacters(str));
        }
    }

    public static String rearrangeCharacters(String string) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */

        // takes O(n) time and O(n) space.
        Map<Character, Integer> d = new HashMap<>();
        getFrequencies(string, d);

        // takes O(n * log(n)) time and O(n) space.
        MaxHeap<HeapElement> maxHeap = new MaxHeap<>();
        for (Character c : d.keySet()) {
            maxHeap.insert(new HeapElement(c, d.get(c)));
        }

        // takes O(n * log(n)) time
        HeapElement prev = null;
        StringBuilder result = new StringBuilder();
        while (!maxHeap.isEmpty()) {
            HeapElement heapElement = maxHeap.pop();
            result.append(heapElement.character);
            heapElement.count -= 1;
            if (prev != null && prev.count > 0) {
                maxHeap.insert(new HeapElement(prev.character, prev.count));
            }
            prev = heapElement;
        }
        if (prev != null && prev.count != 0) return "";
        return result.toString();
    }

    private static void getFrequencies(String string, Map<Character, Integer> d) {
        for (Character character : string.toCharArray()) {
            d.put(character, d.getOrDefault(character, 0) + 1);
        }
    }
}
