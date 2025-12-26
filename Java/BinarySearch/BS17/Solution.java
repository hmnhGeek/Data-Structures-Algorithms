package BinarySearch.BS17;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer aggressiveCows(List<Integer> arr, Integer cows) {
        if (cows <= 0) return null;
        QuickSort.sort(arr);
        int low = 0, high = arr.getLast() - arr.getFirst();
        while (low <= high) {
            int mid = (low + (high - low)/2);
            Boolean isPossible = canAllCowsBePlaced(arr, mid, cows);
            if (isPossible) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high;
    }

    private static Boolean canAllCowsBePlaced(List<Integer> arr, int mid, int numCows) {
        int lastCowPlacedAtIndex = 0;
        int numCowsPlaced = 1;
        int i = 1;
        while (i < arr.size()) {
            if (arr.get(i) - arr.get(lastCowPlacedAtIndex) >= mid) {
                lastCowPlacedAtIndex = i;
                numCowsPlaced += 1;
            }
            i += 1;
        }
        return numCowsPlaced >= numCows;
    }

    public static void main(String[] args) {
        System.out.println(Solution.aggressiveCows(Arrays.asList(0, 3, 4, 7, 9, 10), 4));
        System.out.println(Solution.aggressiveCows(Arrays.asList(1, 2, 3), 2));
        System.out.println(Solution.aggressiveCows(Arrays.asList(4, 2, 1, 3, 6), 2));
        System.out.println(Solution.aggressiveCows(Arrays.asList(1, 2, 4, 8, 9), 3));
        System.out.println(Solution.aggressiveCows(Arrays.asList(10, 1, 2, 7, 5), 3));
        System.out.println(Solution.aggressiveCows(Arrays.asList(2, 12, 11, 3, 26, 7), 5));
        System.out.println(Solution.aggressiveCows(Arrays.asList(6, 7, 9, 11, 13, 15), 4));
    }
}
