package SlidingWindows;


import java.util.*;

class SolutionL5 {
    public static void main(String[] args) {
        System.out.println(getMaxFruitsCollected(Arrays.asList(3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4), 2));
        System.out.println(getMaxFruitsCollected(Arrays.asList(1, 2, 1), 2));
        System.out.println(getMaxFruitsCollected(Arrays.asList(0, 1, 2, 2), 2));
        System.out.println(getMaxFruitsCollected(Arrays.asList(1, 2, 3, 2, 2), 2));
        System.out.println(getMaxFruitsCollected(Arrays.asList(3, 1, 2, 2, 2, 2), 2));
        System.out.println(getMaxFruitsCollected(Arrays.asList(1, 1, 2, 3), 2));
        System.out.println(getMaxFruitsCollected(Arrays.asList(1, 2, 3, 4), 2));
    }

    private static <T> List<T> getMaxFruitsCollected(List<T> trees, Integer numBasketsAllowed) {
        int n = trees.size();
        int left = 0, right = 0;
        Integer startIndex = -1;
        int numCollected = 0;
        Map<T, Integer> baskets = new HashMap<>();

        while (right < n) {
            T fruitToAdd = trees.get(right);
            baskets.put(fruitToAdd, baskets.getOrDefault(fruitToAdd, 0) + 1);
            if (baskets.size() > numBasketsAllowed) {
                T fruitToRemove = trees.get(left);
                baskets.put(fruitToRemove, baskets.get(fruitToRemove) - 1);
                if (baskets.get(fruitToRemove).equals(0)) {
                    baskets.remove(fruitToRemove);
                }
                left += 1;
            }
            if (baskets.size() <= numBasketsAllowed) {
                numCollected = Math.max(numCollected, right - left + 1);
                startIndex = left;
            }
            right += 1;
        }
        if (startIndex != -1) {
            return trees.subList(startIndex, startIndex + numCollected);
        }
        return new ArrayList<>();
    }
}