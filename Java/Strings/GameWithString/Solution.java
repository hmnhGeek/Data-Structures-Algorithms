package Strings.GameWithString;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    private static Map<Character, Integer> counter(String s) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character c : s.toCharArray()) {
            d.put(c, d.getOrDefault(c, 0) + 1);
        }
        return d;
    }

    public static Integer gameWithString(String string, Integer k) {
        if (k < 0 || k > string.length()) return null;
        MaxHeap<HeapElement> maxHeap = new MaxHeap<>();
        Map<Character, Integer> d = counter(string);
        for (Map.Entry<Character, Integer> entry : d.entrySet()) {
            maxHeap.insert(new HeapElement(entry.getKey(), entry.getValue()));
        }
        while (k != 0) {
            HeapElement element = maxHeap.pop();
            k -= 1;
            element.setCount(element.getCount() - 1);
            maxHeap.insert(element);
        }
        Integer sum = 0;
        while (!maxHeap.isEmpty()) {
            HeapElement heapElement = maxHeap.pop();
            sum += (heapElement.getCount() * heapElement.getCount());
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(Solution.gameWithString("abccc", 1));
        System.out.println(Solution.gameWithString("aabcbcbcabcc", 3));
    }
}
