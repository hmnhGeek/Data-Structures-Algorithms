// Problem link - https://leetcode.com/problems/fruit-into-baskets/description/
// Solution - https://www.youtube.com/watch?v=e3bs0uA1NhQ&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=5


package PracticeSet1.SlidingWindows.L5;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<T> getMaxFruits(List<T> arr, int k) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        if (k <= 0) return null;
        Map<T, Integer> basketsRequired = getRequiredBaskets(arr);
        int left = 0, right = 0, collectedFruitsCount = 0, startIndex = -1;
        while (right < arr.size()) {
            T currFruit = arr.get(right);
            basketsRequired.put(currFruit, basketsRequired.get(currFruit) + 1);
            if (getUsedBaskets(basketsRequired) > k) {
                basketsRequired.put(arr.get(left), basketsRequired.get(arr.get(left)) - 1);
                left += 1;
            }
            if (right - left + 1 > collectedFruitsCount) {
                collectedFruitsCount = right - left + 1;
                startIndex = left;
            }
            right += 1;
        }
        if (startIndex != -1) {
            return arr.subList(startIndex, startIndex + collectedFruitsCount);
        }
        return null;
    }

    private static <T> int getUsedBaskets(Map<T, Integer> basketsRequired) {
        int count = 0;
        for (T fruit : basketsRequired.keySet()) {
            if (basketsRequired.get(fruit) > 0) {
                count += 1;
            }
        }
        return count;
    }

    private static <T> Map<T, Integer> getRequiredBaskets(List<T> arr) {
        Map<T, Integer> d = new HashMap<>();
        for (T elem : arr) {
            d.put(elem, 0);
        }
        return d;
    }

    public static void main(String[] args) {
        System.out.println(getMaxFruits(Arrays.asList(3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4), 2));
        System.out.println(getMaxFruits(Arrays.asList(1, 2, 1), 2));
        System.out.println(getMaxFruits(Arrays.asList(0, 1, 2, 2), 2));
        System.out.println(getMaxFruits(Arrays.asList(1, 2, 3, 2, 2), 2));
        System.out.println(getMaxFruits(Arrays.asList(3, 1, 2, 2, 2, 2), 2));
        System.out.println(getMaxFruits(Arrays.asList(1, 1, 2, 3), 2));
        System.out.println(getMaxFruits(Arrays.asList(1, 2, 3, 4), 2));
    }
}
