package PracticeSet1.Heap.Problem9;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(reorganizeString("aab"));
        System.out.println(reorganizeString("aaab"));
        System.out.println(reorganizeString("address"));
        System.out.println(reorganizeString("mississippi"));
        System.out.println(reorganizeString("aaabc"));
        System.out.println(reorganizeString("aaabb"));
        System.out.println(reorganizeString("aa"));
        System.out.println(reorganizeString("aaaabc"));
        System.out.println(reorganizeString("abaab"));
        System.out.println(reorganizeString("bbbbbb"));
    }

    public static String reorganizeString(String string) {
        MaxHeap<Element> pq = new MaxHeap<>();
        populatePriorityQueue(pq, string);
        Element prev = null;
        StringBuilder result = new StringBuilder();
        while (!pq.isEmpty()) {
            Element element = pq.pop();
            result.append(element.character);
            element.count -= 1;
            if (prev != null) {
                pq.insert(prev);
            }
            if (element.count > 0) {
                prev = element;
            } else {
                prev = null;
            }
        }
        if (prev != null && prev.count > 0) return "";
        return result.toString();
    }

    private static void populatePriorityQueue(MaxHeap<Element> pq, String string) {
        Map<Character, Integer> freqMap = new HashMap<>();
        for (Character character : string.toCharArray()) {
            freqMap.put(character, freqMap.getOrDefault(character, 0) + 1);
        }
        for (Character character : freqMap.keySet()) {
            pq.insert(new Element(character, freqMap.get(character)));
        }
    }
}
