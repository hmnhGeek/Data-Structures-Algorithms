package StacksAndQueues.Problem36;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    private static Integer gameWithString(String string, Integer k) {
        Map<Character, Integer> d = getFrequencyMap(string);
        MaxHeap<HeapObject> maxHeap = new MaxHeap<>();
        for (Map.Entry<Character, Integer> entry : d.entrySet()) {
            HeapObject heapObject = new HeapObject(entry.getKey(), entry.getValue());
            maxHeap.insert(heapObject);
        }
        Integer counter = 0;
        while (counter != k) {
            HeapObject heapObject = maxHeap.pop();
            heapObject.setCount(heapObject.getCount() - 1);
            counter += 1;
            if (heapObject.getCount() > 0) {
                maxHeap.insert(heapObject);
            }
        }
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
    }
}
