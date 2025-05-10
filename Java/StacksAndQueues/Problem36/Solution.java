// Problem link - https://www.geeksforgeeks.org/problems/game-with-string4100/1

package StacksAndQueues.Problem36;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    private static Integer gameWithString(String string, Integer k) {
        /*
            Overall time complexity is O({n + k} * log(n)) and space complexity is O(n).
         */

        // This will take O(n) time and O(n) space.
        Map<Character, Integer> d = getFrequencyMap(string);

        // This will take O(n * log(n)) time and O(n) space.
        MaxHeap<HeapObject> maxHeap = new MaxHeap<>();
        for (Map.Entry<Character, Integer> entry : d.entrySet()) {
            HeapObject heapObject = new HeapObject(entry.getKey(), entry.getValue());
            maxHeap.insert(heapObject);
        }

        // This will take O(k * log(n)) time
        Integer counter = 0;
        while (counter != k) {
            HeapObject heapObject = maxHeap.pop();
            heapObject.setCount(heapObject.getCount() - 1);
            counter += 1;
            if (heapObject.getCount() > 0) {
                maxHeap.insert(heapObject);
            }
        }

        // This will take O(n * log(n)) time.
        Integer result = 0;
        while (!maxHeap.isEmpty()) {
            HeapObject heapObject = maxHeap.pop();
            result += (heapObject.getCount() * heapObject.getCount());
        }
        return result;
    }

    private static Map<Character, Integer> getFrequencyMap(String string) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character character : string.toCharArray()) {
            d.put(character, d.getOrDefault(character, 0) + 1);
        }
        return d;
    }

    public static void main(String[] args) {
        // Example 1
        System.out.println(gameWithString("abccc", 1));

        // Example 2
        System.out.println(gameWithString("aabcbcbcabcc", 3));
    }
}
