// Problem link - https://leetcode.com/problems/minimum-path-sum/description/
// Solution - https://www.youtube.com/watch?v=_rgTlyky1uQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=11


package DynamicProgramming.DP10;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static void recursive() {
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 9, 6),
                                Arrays.asList(11, 5, 2)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        List.of(List.of(5))
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 4),
                                Arrays.asList(7, 5, 9)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 6),
                                Arrays.asList(1, 2)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 3, 1),
                                Arrays.asList(1, 5, 1),
                                Arrays.asList(4, 2, 1)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 6)
                        )
                )
        );
    }

    private static void memoized() {
        System.out.println(
                MemoizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 9, 6),
                                Arrays.asList(11, 5, 2)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.minPathSum(
                        List.of(List.of(5))
                )
        );
        System.out.println(
                MemoizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 4),
                                Arrays.asList(7, 5, 9)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 6),
                                Arrays.asList(1, 2)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 3, 1),
                                Arrays.asList(1, 5, 1),
                                Arrays.asList(4, 2, 1)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 6)
                        )
                )
        );
    }

    private static void tabulation() {
        System.out.println(
                TabulationSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 9, 6),
                                Arrays.asList(11, 5, 2)
                        )
                )
        );
        System.out.println(
                TabulationSolution.minPathSum(
                        List.of(List.of(5))
                )
        );
        System.out.println(
                TabulationSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 4),
                                Arrays.asList(7, 5, 9)
                        )
                )
        );
        System.out.println(
                TabulationSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 6),
                                Arrays.asList(1, 2)
                        )
                )
        );
        System.out.println(
                TabulationSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 3, 1),
                                Arrays.asList(1, 5, 1),
                                Arrays.asList(4, 2, 1)
                        )
                )
        );
        System.out.println(
                TabulationSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 6)
                        )
                )
        );
    }

    private static void spaceOptimized() {
        System.out.println(
                SpaceOptimizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 9, 6),
                                Arrays.asList(11, 5, 2)
                        )
                )
        );
        System.out.println(
                SpaceOptimizedSolution.minPathSum(
                        List.of(List.of(5))
                )
        );
        System.out.println(
                SpaceOptimizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 4),
                                Arrays.asList(7, 5, 9)
                        )
                )
        );
        System.out.println(
                SpaceOptimizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 6),
                                Arrays.asList(1, 2)
                        )
                )
        );
        System.out.println(
                SpaceOptimizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 3, 1),
                                Arrays.asList(1, 5, 1),
                                Arrays.asList(4, 2, 1)
                        )
                )
        );
        System.out.println(
                SpaceOptimizedSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 6)
                        )
                )
        );
    }

    public static void main(String[] args) {
        System.out.println("Recursive Solution");
        recursive();
        System.out.println();
        System.out.println("Memoized Solution");
        memoized();
        System.out.println();
        System.out.println("Tabulation Solution");
        tabulation();
        System.out.println();
        System.out.println("Space Optimized Solution");
        spaceOptimized();
        System.out.println();
    }
}
