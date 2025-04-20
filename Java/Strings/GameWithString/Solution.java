// https://www.geeksforgeeks.org/problems/game-with-string4100/1


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
        /*
            Time complexity is O({n + k} * log(n)) and space complexity is O(n).
         */

        // if `k` is not in bounds, return null.
        if (k < 0 || k > string.length()) return null;

        // create a max heap
        MaxHeap<HeapElement> maxHeap = new MaxHeap<>();

        // create a frequency map for the characters of the string in O(n) time.
        Map<Character, Integer> d = counter(string);

        // insert the frequencies into the max heap.
        for (Map.Entry<Character, Integer> entry : d.entrySet()) {
            maxHeap.insert(new HeapElement(entry.getKey(), entry.getValue()));
        }

        // reduce `k` counts...
        while (k != 0) {
            // pop the current element in O(log(n)) time.
            HeapElement element = maxHeap.pop();

            // decrement `k`.
            k -= 1;

            // reduce the count of this max frequency character and insert back into the max heap.
            element.setCount(element.getCount() - 1);

            // this will take O(log(n)) time.
            maxHeap.insert(element);
        }

        // initialize a sum variable
        Integer sum = 0;

        // completely empty the max heap in n iterations...
        while (!maxHeap.isEmpty()) {
            // pop the element in O(log(n)) time.
            HeapElement heapElement = maxHeap.pop();
            // update the sum
            sum += (heapElement.getCount() * heapElement.getCount());
        }

        // return the sum.
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(Solution.gameWithString("abccc", 1));
        System.out.println(Solution.gameWithString("aabcbcbcabcc", 3));
    }
}
