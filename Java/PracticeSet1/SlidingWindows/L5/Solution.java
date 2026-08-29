package PracticeSet1.SlidingWindows.L5;

import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<T> getMaxFruits(List<T> arr, int k) {
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
}
