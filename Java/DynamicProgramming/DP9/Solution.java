// Problem link - https://leetcode.com/problems/unique-paths-ii/description/
// Solution - https://www.youtube.com/watch?v=TmhpgXScLyY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=10


package DynamicProgramming.DP9;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }

    private static void recursive() {
        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, 0),
                                Arrays.asList(0, -1, 0),
                                Arrays.asList(0, 0, 0)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(-1, 0)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, -1, 0, -1),
                                Arrays.asList(0, 0, 0, -1, 0),
                                Arrays.asList(-1, 0, 0, -1, 0),
                                Arrays.asList(0, 0, 0, 0, 0)
                        )
                )
        );

        System.out.println();
    }

    private static void memoized() {
        System.out.println(
                MemoizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, 0),
                                Arrays.asList(0, -1, 0),
                                Arrays.asList(0, 0, 0)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(-1, 0)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, -1, 0, -1),
                                Arrays.asList(0, 0, 0, -1, 0),
                                Arrays.asList(-1, 0, 0, -1, 0),
                                Arrays.asList(0, 0, 0, 0, 0)
                        )
                )
        );

        System.out.println();
    }

    private static void tabulation() {
        System.out.println(
                TabulationSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, 0),
                                Arrays.asList(0, -1, 0),
                                Arrays.asList(0, 0, 0)
                        )
                )
        );

        System.out.println(
                TabulationSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                TabulationSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                TabulationSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(-1, 0)
                        )
                )
        );

        System.out.println(
                TabulationSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, -1, 0, -1),
                                Arrays.asList(0, 0, 0, -1, 0),
                                Arrays.asList(-1, 0, 0, -1, 0),
                                Arrays.asList(0, 0, 0, 0, 0)
                        )
                )
        );

        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(
                SpaceOptimizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, 0),
                                Arrays.asList(0, -1, 0),
                                Arrays.asList(0, 0, 0)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(-1, 0)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, -1, 0, -1),
                                Arrays.asList(0, 0, 0, -1, 0),
                                Arrays.asList(-1, 0, 0, -1, 0),
                                Arrays.asList(0, 0, 0, 0, 0)
                        )
                )
        );

        System.out.println();
    }
}
