// Problem link - https://www.naukri.com/code360/problems/longest-bitonic-sequence_1062688?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=y4vN0WNdrlg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=47


package DynamicProgramming.DP46;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    private static List<List<Integer>> getDpAndParentInfo(List<Integer> arr) {
        List<Integer> dp = new ArrayList<>();
        List<Integer> parent = new ArrayList<>();
        for (int i = 0; i < arr.size(); i += 1) {
            dp.add(1);
            parent.add(i);
        }
        for (int i = 0; i < arr.size(); i += 1) {
            for (int prev = 0; prev < i; prev += 1) {
                if (arr.get(prev) < arr.get(i) && dp.get(prev) + 1 > dp.get(i)) {
                    dp.set(i, 1 + dp.get(prev));
                    parent.set(i, prev);
                }
            }
        }
        return List.of(dp, parent);
    }

    public static List<Integer> getLongestBitonicSequence(List<Integer> arr) {
        /*
            Time complexity is O(n^2) and space complexity is O(n).
         */

        // This takes O(n^2) time and O(n) space.
        List<List<Integer>> info1 = getDpAndParentInfo(arr);
        List<Integer> dp1 = info1.getFirst(), parent1 = info1.getLast();

        // This takes O(n^2) time and O(n) space.
        List<Integer> reversed = arr.reversed();
        List<List<Integer>> info2 = getDpAndParentInfo(reversed);
        List<Integer> dp2 = info2.getFirst(), parent2 = info2.getLast();
        dp2 = dp2.reversed();
        parent2 = parent2.reversed();
        for (int i = 0; i < arr.size(); i += 1) {
            parent2.set(i, arr.size() - parent2.get(i) - 1);
        }

        // This takes O(n) time and O(n) space.
        List<Integer> dp = getBitonicDp(arr, dp1, dp2);
        int indexOfMax = dp.indexOf(Collections.max(dp));
        List<Integer> increasingSequence = getIncreasingSequence(arr, indexOfMax, parent1);
        List<Integer> decreasingSequence = getDecreasingSequence(arr, parent2, indexOfMax);
        List<Integer> bitonicSequence = new ArrayList<>();
        bitonicSequence.addAll(increasingSequence);
        bitonicSequence.addAll(decreasingSequence);
        return bitonicSequence;
    }

    private static List<Integer> getDecreasingSequence(List<Integer> arr, List<Integer> parent2, int indexOfMax) {
        int startIndex = parent2.get(indexOfMax);
        List<Integer> decreasingSequence = new ArrayList<>();
        boolean emptySequence = true;
        while (startIndex != parent2.get(startIndex)) {
            emptySequence = false;
            decreasingSequence.add(arr.get(startIndex));
            startIndex = parent2.get(startIndex);
        }
        if (!emptySequence) {
            decreasingSequence.add(arr.get(startIndex));
        }
        return decreasingSequence;
    }

    private static List<Integer> getIncreasingSequence(List<Integer> arr, int indexOfMax, List<Integer> parent1) {
        List<Integer> increasingSequence = new ArrayList<>();
        int startIndex = indexOfMax;
        while (startIndex != parent1.get(startIndex)) {
            increasingSequence.add(arr.get(startIndex));
            startIndex = parent1.get(startIndex);
        }
        increasingSequence.add(arr.get(startIndex));
        increasingSequence = increasingSequence.reversed();
        return increasingSequence;
    }

    private static List<Integer> getBitonicDp(List<Integer> arr, List<Integer> dp1, List<Integer> dp2) {
        List<Integer> dp = new ArrayList<>();
        for (int i = 0; i < arr.size(); i += 1) {
            dp.add(dp1.get(i) + dp2.get(i) - 1);
        }
        return dp;
    }

    public static void main(String[] args) {
        System.out.println(getLongestBitonicSequence(Arrays.asList(1, 11, 2, 10, 4, 5, 2, 1)));
        System.out.println(getLongestBitonicSequence(Arrays.asList(1, 2, 1, 2, 1)));
        System.out.println(getLongestBitonicSequence(Arrays.asList(1, 2, 1, 3, 4)));
        System.out.println(getLongestBitonicSequence(Arrays.asList(12, 11, 40, 5, 3, 1)));
        System.out.println(getLongestBitonicSequence(Arrays.asList(80, 60, 30)));
        System.out.println(getLongestBitonicSequence(Arrays.asList(10, 10, 10)));
    }
}
