// Problem link - https://www.naukri.com/code360/problems/divisible-set_3754960?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=gDuZwBW9VvM&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=45


package DynamicProgramming.DP44;

import java.util.*;

public class Solution {
    private static void recursive() {
        System.out.println(RecursiveSolution.getLDSLength(Arrays.asList(1, 16, 7, 8, 4)));
        System.out.println(RecursiveSolution.getLDSLength(Arrays.asList(1, 2, 5)));
        System.out.println(RecursiveSolution.getLDSLength(Arrays.asList(3, 3, 3)));
        System.out.println(RecursiveSolution.getLDSLength(Arrays.asList(1, 2, 4, 8)));
        System.out.println(RecursiveSolution.getLDSLength(Arrays.asList(1, 2, 3)));
        System.out.println(RecursiveSolution.getLDSLength(Arrays.asList(2, 4, 3, 8)));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getLDSLength(Arrays.asList(1, 16, 7, 8, 4)));
        System.out.println(MemoizedSolution.getLDSLength(Arrays.asList(1, 2, 5)));
        System.out.println(MemoizedSolution.getLDSLength(Arrays.asList(3, 3, 3)));
        System.out.println(MemoizedSolution.getLDSLength(Arrays.asList(1, 2, 4, 8)));
        System.out.println(MemoizedSolution.getLDSLength(Arrays.asList(1, 2, 3)));
        System.out.println(MemoizedSolution.getLDSLength(Arrays.asList(2, 4, 3, 8)));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getLDSLength(Arrays.asList(1, 16, 7, 8, 4)));
        System.out.println(TabulationSolution.getLDSLength(Arrays.asList(1, 2, 5)));
        System.out.println(TabulationSolution.getLDSLength(Arrays.asList(3, 3, 3)));
        System.out.println(TabulationSolution.getLDSLength(Arrays.asList(1, 2, 4, 8)));
        System.out.println(TabulationSolution.getLDSLength(Arrays.asList(1, 2, 3)));
        System.out.println(TabulationSolution.getLDSLength(Arrays.asList(2, 4, 3, 8)));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getLDSLength(Arrays.asList(1, 16, 7, 8, 4)));
        System.out.println(SpaceOptimizedSolution.getLDSLength(Arrays.asList(1, 2, 5)));
        System.out.println(SpaceOptimizedSolution.getLDSLength(Arrays.asList(3, 3, 3)));
        System.out.println(SpaceOptimizedSolution.getLDSLength(Arrays.asList(1, 2, 4, 8)));
        System.out.println(SpaceOptimizedSolution.getLDSLength(Arrays.asList(1, 2, 3)));
        System.out.println(SpaceOptimizedSolution.getLDSLength(Arrays.asList(2, 4, 3, 8)));
        System.out.println();
    }

    public static List<Integer> getLDS(List<Integer> arr) {
        /*
            Time complexity is O(n^2) and space complexity is O(n).
         */
        int n = arr.size();
        Map<Integer, Integer> size = new HashMap<>();
        Map<Integer, Integer> parent = new HashMap<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < n; i += 1) {
            size.put(i, 1);
            parent.put(i, i);
        }

        for (int i = 0; i < n; i += 1) {
            for (int prev = 0; prev < i; prev += 1) {
                if (arr.get(prev) % arr.get(i) == 0 || arr.get(i) % arr.get(prev) == 0) {
                    size.put(i, size.get(prev) + 1);
                    parent.put(i, prev);
                }
            }
        }

        Integer idxOfMaxLength = getIndexOfLongest(size, n);
        int start = idxOfMaxLength;
        while (parent.get(start) != start) {
            result.add(arr.get(start));
            start = parent.get(start);
        }
        result.add(arr.get(start));
        return result;
    }

    private static Integer getIndexOfLongest(Map<Integer, Integer> size, int n) {
        int length = 0;
        Integer idx = null;
        for (Integer i : size.keySet()) {
            if (size.get(i) > length) {
                length = size.get(i);
                idx = i;
            }
        }
        return idx;
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
        System.out.println(Solution.getLDS(Arrays.asList(1, 16, 7, 8, 4)));
        System.out.println(Solution.getLDS(Arrays.asList(1, 2, 5)));
        System.out.println(Solution.getLDS(Arrays.asList(3, 3, 3)));
        System.out.println(Solution.getLDS(Arrays.asList(1, 2, 4, 8)));
        System.out.println(Solution.getLDS(Arrays.asList(1, 2, 3)));
        System.out.println(Solution.getLDS(Arrays.asList(2, 4, 3, 8)));
    }
}
