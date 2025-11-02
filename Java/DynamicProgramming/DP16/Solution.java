package DynamicProgramming.DP16;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getMinAbsDiff(Arrays.asList(1, 2, 3, 4)));
        System.out.println(getMinAbsDiff(Arrays.asList(3, 1, 5, 2, 8)));
        System.out.println(getMinAbsDiff(Arrays.asList(8, 6, 5)));
        System.out.println(getMinAbsDiff(Arrays.asList(3, 9, 7, 3)));
        System.out.println(getMinAbsDiff(Arrays.asList(1, 6, 11, 5)));
        System.out.println(getMinAbsDiff(Arrays.asList(1, 5, 11, 5)));
    }

    public static void recursive() {
        System.out.println(RecursiveSolution.subsetSum(List.of(1, 2, 3, 4), 4));
        System.out.println(RecursiveSolution.subsetSum(List.of(4, 3, 2, 1), 5));
        System.out.println(RecursiveSolution.subsetSum(List.of(2, 5, 1, 6, 7), 4));
        System.out.println(RecursiveSolution.subsetSum(List.of(6, 1, 2, 1), 4));
        System.out.println(RecursiveSolution.subsetSum(List.of(1, 7, 2, 9, 10), 6));
        System.out.println(RecursiveSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 9));
        System.out.println(RecursiveSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 30));
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.subsetSum(List.of(1, 2, 3, 4), 4));
        System.out.println(MemoizedSolution.subsetSum(List.of(4, 3, 2, 1), 5));
        System.out.println(MemoizedSolution.subsetSum(List.of(2, 5, 1, 6, 7), 4));
        System.out.println(MemoizedSolution.subsetSum(List.of(6, 1, 2, 1), 4));
        System.out.println(MemoizedSolution.subsetSum(List.of(1, 7, 2, 9, 10), 6));
        System.out.println(MemoizedSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 9));
        System.out.println(MemoizedSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 30));
    }

    public static void tabulation() {
        System.out.println(TabulationSolution.subsetSum(List.of(1, 2, 3, 4), 4));
        System.out.println(TabulationSolution.subsetSum(List.of(4, 3, 2, 1), 5));
        System.out.println(TabulationSolution.subsetSum(List.of(2, 5, 1, 6, 7), 4));
        System.out.println(TabulationSolution.subsetSum(List.of(6, 1, 2, 1), 4));
        System.out.println(TabulationSolution.subsetSum(List.of(1, 7, 2, 9, 10), 6));
        System.out.println(TabulationSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 9));
        System.out.println(TabulationSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 30));
    }

    public static void spaceOptimizedSolution() {
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(1, 2, 3, 4), 4));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(4, 3, 2, 1), 5));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(2, 5, 1, 6, 7), 4));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(6, 1, 2, 1), 4));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(1, 7, 2, 9, 10), 6));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 9));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 30));
    }

    public static Integer getMinAbsDiff(List<Integer> arr) {
        Integer sum = getSum(arr);
        Integer minSum = Integer.MAX_VALUE;
        for (int target = 0; target <= (int) Math.floor(sum/2) + 1; target += 1) {
            if (SpaceOptimizedSolution.subsetSum(arr, target)) {
                minSum = Math.min(minSum, Math.abs(sum - 2*target));
            }
        }
        return minSum;
    }

    private static Integer getSum(List<Integer> arr) {
        Integer sum = 0;
        for (Integer i : arr) {
            sum += i;
        }
        return sum;
    }
}
