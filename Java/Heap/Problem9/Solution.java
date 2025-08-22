package Heap.Problem9;


import Heap.Problem9.MaxHeap.MaxHeap;

import java.util.HashMap;
import java.util.Map;

class HeapElement implements Comparable<HeapElement> {
    private Character character;
    private Integer count;

    public HeapElement(Character character, Integer count) {
        this.character = character;
        this.count = count;
    }

    public Character getCharacter() {
        return character;
    }

    public void setCharacter(Character character) {
        this.character = character;
    }

    public Integer getCount() {
        return count;
    }

    public void setCount(Integer count) {
        this.count = count;
    }

    @Override
    public int compareTo(HeapElement o) {
        return this.count.compareTo(o.getCount());
    }
}


public class Solution {
    public static String reorganizeStrings(String string) {
        Map<Character, Integer> characterCounts = getCharacterCount(string);
        MaxHeap<HeapElement> maxHeap = new MaxHeap<>();
        for (Character character : characterCounts.keySet()) {
            maxHeap.insert(new HeapElement(character, characterCounts.get(character)));
        }
        HeapElement prev = null;
        StringBuilder result = new StringBuilder();
        while (!maxHeap.isEmpty()) {
            HeapElement poppedElement = maxHeap.pop();
            result.append(poppedElement.getCharacter());
            if (prev != null && prev.getCount() > 0) {
                maxHeap.insert(prev);
            }
            prev = new HeapElement(poppedElement.getCharacter(), poppedElement.getCount() - 1);
        }
        if (prev != null && prev.getCount() > 0) return "";
        return result.toString();
    }

    private static Map<Character, Integer> getCharacterCount(String string) {
        Map<Character, Integer> d = new HashMap<>();
        for (Character character : string.toCharArray()) {
            d.put(character, d.getOrDefault(character, 0) + 1);
        }
        return d;
    }

    public static void main(String[] args) {
        System.out.println(reorganizeStrings("aab"));
        System.out.println(reorganizeStrings("aaab"));
    }
}
