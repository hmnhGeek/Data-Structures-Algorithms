// Problem link - https://www.geeksforgeeks.org/problems/aggressive-cows/0
// Solution - https://www.youtube.com/watch?v=R_Mfw4ew-Vo&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=18


package PracticeSet1.BinarySearch.BS17;

import PracticeSet1.BinarySearch.BS17.Sorting.*;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(aggressiveCows(Arrays.asList(0, 3, 4, 7, 9, 10), 4));
        System.out.println(aggressiveCows(Arrays.asList(1, 2, 3), 2));
        System.out.println(aggressiveCows(Arrays.asList(4, 2, 1, 3, 6), 2));
        System.out.println(aggressiveCows(Arrays.asList(1, 2, 4, 8, 9), 3));
        System.out.println(aggressiveCows(Arrays.asList(10, 1, 2, 7, 5), 3));
        System.out.println(aggressiveCows(Arrays.asList(2, 12, 11, 3, 26, 7), 5));
        System.out.println(aggressiveCows(Arrays.asList(6, 7, 9, 11, 13, 15), 4));
    }

    public static Integer aggressiveCows(List<Integer> arr, Integer cowsCount) {
        /*
            Time complexity is O(n * log(n) + n * log(max(arr))) and space complexity is O(1).
         */
        if (cowsCount <= 0 || arr.isEmpty()) return null;
        Sort<Integer> quickSort = new QuickSort<>();
        quickSort.sort(arr);
        int low = 0, high = arr.getLast();
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (placingAllCowsPossible(arr, mid, cowsCount)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high;
    }

    private static boolean placingAllCowsPossible(List<Integer> arr, int mid, Integer cowsCount) {
        int placedCows = 1;
        int lastCowPlacedAt = 0;
        for (int i = 1; i < arr.size(); i += 1) {
            if (arr.get(i) - arr.get(lastCowPlacedAt) >= mid) {
                placedCows += 1;
                lastCowPlacedAt = i;
            }
            if (placedCows == cowsCount) return true;
        }
        return false;
    }
}
