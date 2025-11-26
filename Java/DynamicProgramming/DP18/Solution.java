package DynamicProgramming.DP18;


import java.util.List;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getCount(List.of(1, 2, 2, 3), 3));
        System.out.println(RecursiveSolution.getCount(List.of(1, 1, 4, 5), 5));
        System.out.println(RecursiveSolution.getCount(List.of(1, 1, 1), 2));
        System.out.println(RecursiveSolution.getCount(List.of(2, 34, 5), 40));
        System.out.println(RecursiveSolution.getCount(List.of(1, 2, 3, 3), 6));
        System.out.println(RecursiveSolution.getCount(List.of(1, 1, 1, 1), 1));
        System.out.println(RecursiveSolution.getCount(List.of(5, 2, 3, 10, 6, 8), 10));
        System.out.println(RecursiveSolution.getCount(List.of(2, 5, 1, 4, 3), 10));
        System.out.println(RecursiveSolution.getCount(List.of(5, 7, 8), 3));
        System.out.println(RecursiveSolution.getCount(List.of(35, 2, 8, 22), 0));
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.getCount(List.of(1, 2, 2, 3), 3));
        System.out.println(MemoizedSolution.getCount(List.of(1, 1, 4, 5), 5));
        System.out.println(MemoizedSolution.getCount(List.of(1, 1, 1), 2));
        System.out.println(MemoizedSolution.getCount(List.of(2, 34, 5), 40));
        System.out.println(MemoizedSolution.getCount(List.of(1, 2, 3, 3), 6));
        System.out.println(MemoizedSolution.getCount(List.of(1, 1, 1, 1), 1));
        System.out.println(MemoizedSolution.getCount(List.of(5, 2, 3, 10, 6, 8), 10));
        System.out.println(MemoizedSolution.getCount(List.of(2, 5, 1, 4, 3), 10));
        System.out.println(MemoizedSolution.getCount(List.of(5, 7, 8), 3));
        System.out.println(MemoizedSolution.getCount(List.of(35, 2, 8, 22), 0));
    }

    public static void tabulation() {
        System.out.println(TabulationSolution.getCount(List.of(1, 2, 2, 3), 3));
        System.out.println(TabulationSolution.getCount(List.of(1, 1, 4, 5), 5));
        System.out.println(TabulationSolution.getCount(List.of(1, 1, 1), 2));
        System.out.println(TabulationSolution.getCount(List.of(2, 34, 5), 40));
        System.out.println(TabulationSolution.getCount(List.of(1, 2, 3, 3), 6));
        System.out.println(TabulationSolution.getCount(List.of(1, 1, 1, 1), 1));
        System.out.println(TabulationSolution.getCount(List.of(5, 2, 3, 10, 6, 8), 10));
        System.out.println(TabulationSolution.getCount(List.of(2, 5, 1, 4, 3), 10));
        System.out.println(TabulationSolution.getCount(List.of(5, 7, 8), 3));
        System.out.println(TabulationSolution.getCount(List.of(35, 2, 8, 22), 0));
    }

    public static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getCount(List.of(1, 2, 2, 3), 3));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(1, 1, 4, 5), 5));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(1, 1, 1), 2));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(2, 34, 5), 40));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(1, 2, 3, 3), 6));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(1, 1, 1, 1), 1));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(5, 2, 3, 10, 6, 8), 10));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(2, 5, 1, 4, 3), 10));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(5, 7, 8), 3));
        System.out.println(SpaceOptimizedSolution.getCount(List.of(35, 2, 8, 22), 0));
    }

    public static void main(String[] args) {
        System.out.println(Solution.countPartitionsWithDifference(List.of(5, 2, 6, 4), 3));
        System.out.println(Solution.countPartitionsWithDifference(List.of(1, 1, 1, 1), 0));
        System.out.println(Solution.countPartitionsWithDifference(List.of(4, 6, 3), 1));
        System.out.println(Solution.countPartitionsWithDifference(List.of(3, 1, 1, 2, 1), 0));
        System.out.println(Solution.countPartitionsWithDifference(List.of(3, 2, 2, 5, 1), 1));
        System.out.println(Solution.countPartitionsWithDifference(List.of(1, 2, 1, 0, 1, 3, 3), 11));
        System.out.println(Solution.countPartitionsWithDifference(List.of(1, 2, 3, 1, 2), 1));
    }

    public static int countPartitionsWithDifference(List<Integer> arr, Integer diff) {
        /*
            Time complexity is O(s*s1*n) and space complexity is O(s1).
         */
        Integer s = Utils.getSum(arr);
        int upLimit = (int) Math.ceil(s/2);
        int result = 0;
        // This will run for O(s) time.
        for (int s1 = s; s1 >= upLimit; s1 -= 1) {
            int s2 = s - s1;
            if (s1 >= s2 && s1 - s2 == diff) {
                // This will take O(s1 * n) time and O(s1) space.
                result += SpaceOptimizedSolution.getCount(arr, s1);
            }
        }
        return result;
    }
}
