package SlidingWindows.L5;

import java.util.*;

public class Solution {
    private static <T> Integer countCollectedFruits(Map<T, Integer> baskets) {
        int count = 0;
        for (T basket : baskets.keySet()) {
            if (baskets.get(basket) > 0) {
                count += 1;
            }
        }
        return count;
    }

    public static <T> List<T> fruitsIntoBasket(List<T> fruits) {
        Map<T, Integer> baskets = new HashMap<>();
        for (int i = 0; i < fruits.size(); i += 1) {
            baskets.putIfAbsent(fruits.get(i), 0);
        }
        int left = 0, right = 0;
        int startIndex = -1, length = 0;
        while (right < fruits.size()) {
            baskets.put(fruits.get(right), baskets.get(fruits.get(right)) + 1);
            while (countCollectedFruits(baskets) > 2) {
                baskets.put(fruits.get(left), baskets.get(fruits.get(left)) - 1);
                left += 1;
            }
            if (right - left + 1 > length) {
                startIndex = left;
                length = right - left + 1;
            }
            right += 1;
        }
        if (startIndex != -1) {
            return fruits.subList(startIndex, startIndex + length);
        }
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println(fruitsIntoBasket(Arrays.asList(3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4)));
        System.out.println(fruitsIntoBasket(Arrays.asList(1, 2, 1)));
        System.out.println(fruitsIntoBasket(Arrays.asList(0, 1, 2, 2)));
        System.out.println(fruitsIntoBasket(Arrays.asList(1, 2, 3, 2, 2)));
        System.out.println(fruitsIntoBasket(Arrays.asList(3, 1, 2, 2, 2, 2)));
        System.out.println(fruitsIntoBasket(Arrays.asList(1, 1, 2, 3)));
        System.out.println(fruitsIntoBasket(Arrays.asList(1, 2, 3, 4)));
    }
}
