// Problem link - https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/


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
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */

        // get the frequencies of the characters in the string in O(n) time and O(n) space.
        Map<Character, Integer> characterCounts = getCharacterCount(string);

        // initialize a max heap and push the characters with their frequencies into it. This
        // will take O(n * log(n)) time and O(n) space.
        MaxHeap<HeapElement> maxHeap = new MaxHeap<>();
        for (Character character : characterCounts.keySet()) {
            maxHeap.insert(new HeapElement(character, characterCounts.get(character)));
        }

        // store a prev element to avoid adding adjacent duplicates into result string.
        HeapElement prev = null;
        StringBuilder result = new StringBuilder();

        // start popping elements from max heap. This will take n iterations.
        while (!maxHeap.isEmpty()) {
            // This will take O(log(n)) time.
            HeapElement poppedElement = maxHeap.pop();

            // add the character to the result string.
            result.append(poppedElement.getCharacter());

            // if there is a prev character with still having frequency > 0, push it to max heap
            // in O(log(n)) time.
            if (prev != null && prev.getCount() > 0) {
                maxHeap.insert(prev);
            }

            // update the prev element with new frequency by replacing it with current character.
            prev = new HeapElement(poppedElement.getCharacter(), poppedElement.getCount() - 1);
        }

        // if some character is still left even after emptying the max heap, then it means no valid
        // result exists.
        if (prev != null && prev.getCount() > 0) return "";

        // else return the result.
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
        System.out.println(reorganizeStrings("address"));
        System.out.println(reorganizeStrings("mississippi"));
        System.out.println(reorganizeStrings("aaabc"));
        System.out.println(reorganizeStrings("aaabb"));
        System.out.println(reorganizeStrings("aa"));
        System.out.println(reorganizeStrings("aaaabc"));
        System.out.println(reorganizeStrings("abaab"));
        System.out.println(reorganizeStrings("bbbbbb"));
    }
}
