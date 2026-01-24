package DynamicProgramming.DP23;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
        System.out.println();
        memoized();
        System.out.println();
        tabulation();
        System.out.println();
        spaceOptimized();
        System.out.println();
    }

    private static void recursive() {
        System.out.println(
                RecursiveSolution.getUnboundedKnapsack(
                        Arrays.asList(2, 4, 6),
                        Arrays.asList(5, 11, 13),
                        10
                )
        );

        System.out.println(
                RecursiveSolution.getUnboundedKnapsack(
                        Arrays.asList(5, 10, 20),
                        Arrays.asList(7, 2, 4),
                        15
                )
        );

        System.out.println(
                RecursiveSolution.getUnboundedKnapsack(
                        Arrays.asList(6, 12),
                        Arrays.asList(4, 17),
                        3
                )
        );

        System.out.println(
                RecursiveSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 50),
                        Arrays.asList(1, 30),
                        100
                )
        );

        System.out.println(
                RecursiveSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 3, 4, 5),
                        Arrays.asList(10, 40, 50, 70),
                        8
                )
        );

        System.out.println(
                RecursiveSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 3, 4, 5),
                        Arrays.asList(6, 1, 7, 7),
                        8
                )
        );

        System.out.println(
                RecursiveSolution.getUnboundedKnapsack(
                        Arrays.asList(2, 3, 4, 5),
                        Arrays.asList(6, 8, 7, 100),
                        1
                )
        );
    }

    private static void memoized() {
        System.out.println(
                MemoizedSolution.getUnboundedKnapsack(
                        Arrays.asList(2, 4, 6),
                        Arrays.asList(5, 11, 13),
                        10
                )
        );

        System.out.println(
                MemoizedSolution.getUnboundedKnapsack(
                        Arrays.asList(5, 10, 20),
                        Arrays.asList(7, 2, 4),
                        15
                )
        );

        System.out.println(
                MemoizedSolution.getUnboundedKnapsack(
                        Arrays.asList(6, 12),
                        Arrays.asList(4, 17),
                        3
                )
        );

        System.out.println(
                MemoizedSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 50),
                        Arrays.asList(1, 30),
                        100
                )
        );

        System.out.println(
                MemoizedSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 3, 4, 5),
                        Arrays.asList(10, 40, 50, 70),
                        8
                )
        );

        System.out.println(
                MemoizedSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 3, 4, 5),
                        Arrays.asList(6, 1, 7, 7),
                        8
                )
        );

        System.out.println(
                MemoizedSolution.getUnboundedKnapsack(
                        Arrays.asList(2, 3, 4, 5),
                        Arrays.asList(6, 8, 7, 100),
                        1
                )
        );
    }

    private static void tabulation() {
        System.out.println(
                TabulationSolution.getUnboundedKnapsack(
                        Arrays.asList(2, 4, 6),
                        Arrays.asList(5, 11, 13),
                        10
                )
        );

        System.out.println(
                TabulationSolution.getUnboundedKnapsack(
                        Arrays.asList(5, 10, 20),
                        Arrays.asList(7, 2, 4),
                        15
                )
        );

        System.out.println(
                TabulationSolution.getUnboundedKnapsack(
                        Arrays.asList(6, 12),
                        Arrays.asList(4, 17),
                        3
                )
        );

        System.out.println(
                TabulationSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 50),
                        Arrays.asList(1, 30),
                        100
                )
        );

        System.out.println(
                TabulationSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 3, 4, 5),
                        Arrays.asList(10, 40, 50, 70),
                        8
                )
        );

        System.out.println(
                TabulationSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 3, 4, 5),
                        Arrays.asList(6, 1, 7, 7),
                        8
                )
        );

        System.out.println(
                TabulationSolution.getUnboundedKnapsack(
                        Arrays.asList(2, 3, 4, 5),
                        Arrays.asList(6, 8, 7, 100),
                        1
                )
        );
    }

    private static void spaceOptimized() {
        System.out.println(
                SpaceOptimizedSolution.getUnboundedKnapsack(
                        Arrays.asList(2, 4, 6),
                        Arrays.asList(5, 11, 13),
                        10
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getUnboundedKnapsack(
                        Arrays.asList(5, 10, 20),
                        Arrays.asList(7, 2, 4),
                        15
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getUnboundedKnapsack(
                        Arrays.asList(6, 12),
                        Arrays.asList(4, 17),
                        3
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 50),
                        Arrays.asList(1, 30),
                        100
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 3, 4, 5),
                        Arrays.asList(10, 40, 50, 70),
                        8
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getUnboundedKnapsack(
                        Arrays.asList(1, 3, 4, 5),
                        Arrays.asList(6, 1, 7, 7),
                        8
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getUnboundedKnapsack(
                        Arrays.asList(2, 3, 4, 5),
                        Arrays.asList(6, 8, 7, 100),
                        1
                )
        );
    }
}
