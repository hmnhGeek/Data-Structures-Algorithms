// Problem link - https://leetcode.com/problems/fruit-into-baskets/
// Solution - https://www.youtube.com/watch?v=e3bs0uA1NhQ&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=5

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
        /*
            Time complexity is O(n) and space complexity is O(n) for the baskets map.
         */

        // get the window variables
        int n = trees.size();
        int left = 0, right = 0;

        // get the result variables
        Integer startIndex = -1;
        int numCollected = 0;

        // define the tracking variable
        Map<T, Integer> baskets = new HashMap<>();

        // while there is ground to cover...
        while (right < n) {
            // get the element at right index to add.
            T fruitToAdd = trees.get(right);

            // increment the count of this element in the baskets variable.
            baskets.put(fruitToAdd, baskets.getOrDefault(fruitToAdd, 0) + 1);

            // if we have breached the basket's allowed size, decrement 1 unit from left.
            if (baskets.size() > numBasketsAllowed) {
                T fruitToRemove = trees.get(left);
                baskets.put(fruitToRemove, baskets.get(fruitToRemove) - 1);
                if (baskets.get(fruitToRemove).equals(0)) {
                    baskets.remove(fruitToRemove);
                }
                left += 1;
            }

            // else update the resultant variables.
            if (baskets.size() <= numBasketsAllowed) {
                numCollected = Math.max(numCollected, right - left + 1);
                startIndex = left;
            }

            // increment right index.
            right += 1;
        }

        // return the sublist if start index is not -1.
        if (startIndex != -1) {
            return trees.subList(startIndex, startIndex + numCollected);
        }

        // else return a blank list.
        return new ArrayList<>();
    }
}